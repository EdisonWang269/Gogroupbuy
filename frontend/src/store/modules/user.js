import { formatOrder, changeDate } from "../utils";

const state = {
  items: [],
  orders: [],
  storeID: "store1",
  userID: "customer1",
  currItemID: "",
  currItemNum: 0,
  userName: "",
  userPhone: "",
  keyword: "",
  token: "",
};

const getters = {
  filteredItems(state) {
    return state.items.filter((item) => {
      item.statement_date = changeDate(item.statement_date);

      return item.product_name
        .toLowerCase()
        .includes(state.keyword.toLowerCase());
    });
  },

  getOrders(state) {
    return state.orders.map((order) => formatOrder(order));
  },

  currItem(state) {
    return state.items.find((item) => item.product_id == state.currItemID);
  },
};

const mutations = {
  setUserName(state, name) {
    state.userName = name;
  },
  addWaitingOrder(state, order) {
    state.orders.push(order);
  },
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
};

const actions = {
  async fetchItems({ commit, state }) {
    const response = await fetch(`/api/product`, {
      headers: {
        Authorization: `Bearer ${state.token}`,
      },
    });
    const data = await response.json();
    commit("setItems", data);
  },

  async fetchOrders({ commit, state }) {
    const response = await fetch(`/api/order/${state.userID}`, {
      headers: {
        Authorization: `Bearer ${state.token}`,
      },
    });
    const data = await response.json();
    commit("setOrders", data);
  },

  async fetchToken({ commit, state }) {
    const response = await fetch(`/api/user`, {
      method: "POST",
      headers: {
        "ngrok-skip-browser-warning": "69420",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userid: state.userID,
        store_id: state.storeID,
      }),
    });
    const data = await response.json();
    commit("setToken", data.access_token);
  },

  async fetchUserInit({ dispatch }) {
    try {
      await dispatch("fetchToken");
      await Promise.all([dispatch("fetchItems"), dispatch("fetchOrders")]);
    } catch (error) {
      console.error("Error in fetchUserInit:", error);
    }
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
