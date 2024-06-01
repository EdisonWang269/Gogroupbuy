import { formatOrder, changeDate } from "../utils";

const state = {
  items: [],
  orders: [],
  storeID: "store1",
  userID: "customer1",
  currItemID: "",
  currItemNum: 0,
  userPhone: "09123456789",
  keyword: "",
};

const getters = {
  filteredItems(state) {
    return state.items.filter((item) => {
      item.arrival_date = changeDate(item.arrival_date);
      item.launch_date = changeDate(item.launch_date);
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
  addWaitingOrder(state, order) {
    state.orders.push(order);
  },
  setUserID(state, userID) {
    state.userID = userID;
  },
  setStoreID(state, storeID) {
    state.storeID = storeID;
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
  async fetchItems({ commit, rootState }) {
    const response = await fetch(`/api/product`, {
      headers: {
        Authorization: `Bearer ${rootState.token}`,
      },
    });
    const data = await response.json();
    commit("setItems", data);
  },

  async fetchOrders({ commit, rootState }) {
    const response = await fetch(`/api/order/${state.userID}`, {
      headers: {
        Authorization: `Bearer ${rootState.token}`,
      },
    });
    const data = await response.json();
    commit("setOrders", data);
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
