import { formatOrder, formatItem } from "../utils";

const state = {
  storeID: "store1",
  userID: "merchant1",
  orders: [],
  items: [],
  currItem: {},
  checkedNum: 0,
  uncheckedNum: 0,
  step: "商品管理",
  token: "",
  uploadItem: {},
};

const getters = {
  getItems: (state) => {
    return state.items.map((item) => formatItem(item));
  },
};

const mutations = {
  setOrderStatus(state, payload) {
    const { order_id, status } = payload;
    const index = state.orders.findIndex(
      (order) => order.order_id === order_id
    );
    state.orders[index].receive_status = status;
  },
  setStep(state, step) {
    state.step = step;
  },
  setCurrItem(state, item) {
    state.currItem = item;
  },
  setToken(state, token) {
    state.token = token;
  },
  setOrders(state, orders) {
    orders = orders.map((order) => formatOrder(order));
    state.orders = orders;
  },
  setCheckedNum(state) {
    const checkedNum = state.orders.filter(
      (order) => order.receive_status === "已領取"
    ).length;
    state.checkedNum = checkedNum;
  },
  setUncheckedNum(state) {
    const uncheckedNum = state.orders.filter(
      (order) => order.receive_status !== "已領取"
    ).length;
    state.uncheckedNum = uncheckedNum;
  },
  setItems(state, items) {
    state.items = items;
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
    commit("setCurrItem", data[0]);
  },

  async fetchOrders({ commit, state }) {
    const response = await fetch(`/api/order`, {
      headers: {
        Authorization: `Bearer ${state.token}`,
      },
    });
    const data = await response.json();
    commit("setOrders", data);
    commit("setCheckedNum");
    commit("setUncheckedNum");
  },

  async fetchToken({ commit, state }) {
    const response = await fetch(`/api/user`, {
      method: "POST",
      headers: {
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

  async fetchManagerInit({ dispatch }) {
    try {
      await dispatch("fetchToken");
      await Promise.all([dispatch("fetchOrders"), dispatch("fetchItems")]);
    } catch (error) {
      console.error("Error in fetchManagerInit:", error);
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
