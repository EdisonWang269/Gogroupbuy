import { createStore } from "vuex";

export default createStore({
  state: {
    items: [],
    orders: [],
    storeID: "store1", // for testing TODO: how to get these two?
    userID: "customer1", // for testing
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
    setOrders(state, orders) {
      state.orders = orders;
    },
    setUserPhone(state, userPhone) {
      state.userPhone = userPhone;
    },
    setItems(state, items) {
      state.items = items;
    },
    setStoreID(state, storeID) {
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
      const response = await fetch(`/api/${this.state.storeID}/product`);
      const data = await response.json();
      commit("setItems", data);
    },

    async fetchOrders({ commit }) {
      const response = await fetch(
        `/api/${this.state.storeID}/order/${this.state.userID}`
      );
      const data = await response.json();
      commit("setOrders", data);
    }
  },
  modules: {}
});
