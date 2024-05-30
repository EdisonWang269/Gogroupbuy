import { createStore } from "vuex";

export default createStore({
  state: {
    items: [],
    orders: [],
    storeID: "store1", // TODO: liff 接收 store_id, userID
    userID: "customer1",
    currItemID: "",
    currItemNum: 0,
    userPhone: "",
    keyword: "",
    token: "",
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
    },
  },

  mutations: {
    setUserID(state, userID) {
      state.userID = userID;
    },
    setStoreID(state, storeID) {
      state.storeID = storeID;
    },
    setToken(state, token) {
      state.token = token;
    },
    setOrders(state, orders) {
      state.orders = orders;
    },
    setUserPhone(state, userPhone) {
      state.userPhone = userPhone;
    },
    setItems(state, items) {
      state.items = items;
    },
    setCurrItemID(state, itemID) {
      state.currItemID = itemID;
    },
    setCurrItemNum(state, itemNum) {
      state.currItemNum = itemNum;
    },
    setKeyword(state, keyword) {
      state.keyword = keyword;
    },
  },

  actions: {
    async fetchItems({ commit }) {
      const response = await fetch(`/api/product`, {
        headers: {
          Authorization: `Bearer ${this.state.token}`,
        },
      });
      const data = await response.json();
      commit("setItems", data);
    },

    async fetchOrders({ commit }) {
      const response = await fetch(`/api/order/${this.state.userID}`, {
        headers: {
          Authorization: `Bearer ${this.state.token}`,
        },
      });
      const data = await response.json();
      commit("setOrders", data);
    },

    async fetchToken({ commit }) {
      const response = await fetch(`/api/user`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          userid: this.state.userID,
          store_id: this.state.storeID,
        }),
      });
      const data = await response.json();
      commit("setToken", data.access_token);
    },

    async fetchInit({ dispatch }) {
      try {
        await dispatch("fetchToken");
        await Promise.all([dispatch("fetchItems"), dispatch("fetchOrders")]);
      } catch (error) {
        console.error("Error in fetchInit:", error);
      }
    },
  },
  modules: {},
});
