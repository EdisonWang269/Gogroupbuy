import { createStore } from "vuex";

export default createStore({
  state: {
    items: [],
    currStoreID: "store1",
    currItemID: "",
    currItemNum: 0,
    userPhone: "",
    keyword: ""
  },

  getters: {
    // eslint-disable-next-line no-unused-vars
    changeDate: (state) => (oldDate) => {
      const date = new Date(oldDate);
      const year = date.getFullYear();
      const month = ("0" + (date.getMonth() + 1)).slice(-2);
      const day = ("0" + date.getDate()).slice(-2);

      return `${year}/${month}/${day}`;
    },

    filteredItems(state, getters) {
      return state.items.filter((item) => {
        item.arrival_date = getters.changeDate(item.arrival_date);
        item.launch_date = getters.changeDate(item.launch_date);
        item.statement_date = getters.changeDate(item.statement_date);

        return item.product_name
          .toLowerCase()
          .includes(state.keyword.toLowerCase());
      });
    },

    currItem(state) {
      return state.items.find((item) => item.product_id == state.currItemID);
    }
  },

  mutations: {
    setUserPhone(state, userPhone) {
      state.userPhone = userPhone;
    },
    setItems(state, items) {
      state.items = items;
    },
    setCurrStoreID(state, storeID) {
      state.currStoreID = storeID;
    },
    setCurrItemID(state, itemID) {
      state.currItemID = itemID;
    },
    setCurrItemNum(state, itemNum) {
      state.currItemNum = itemNum;
    },
    setKeyword(state, keyword) {
      state.keyword = keyword;
    }
  },

  actions: {
    async fetchItems({ commit }) {
      const response = await fetch(`/api/${this.state.currStoreID}/product`);
      const data = await response.json();
      commit("setItems", data);
    }
  },
  modules: {}
});
