import { createStore } from "vuex";

export default createStore({
  state: {
    items: [],
    currStoreID: "store1",
    currItemID: "",
    keyword: ""
  },

  getters: {
    filteredItems(state) {
      return state.items.filter((item) => {
        const date = new Date(item.statement_date);
        const year = date.getFullYear();
        const month = ("0" + (date.getMonth() + 1)).slice(-2);
        const day = ("0" + date.getDate()).slice(-2);

        item.statement_date = `${year}/${month}/${day}`;

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
    setItems(state, items) {
      state.items = items;
    },
    setCurrStoreID(state, storeID) {
      state.currStoreID = storeID;
    },
    setCurrItemID(state, itemID) {
      state.currItemID = itemID;
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
