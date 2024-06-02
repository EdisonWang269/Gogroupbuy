import { changeDate } from "../utils";

const state = {
  storeID: "store1",
  userID: "manager1",
  items: [],
  ordersAll: [],
  token: "",
};

const getters = {};

const mutations = {
  setToken(state, token) {
    state.token = token;
  },

  setItems(state, items) {
    state.items = items;
  },

  setOrderByProductNames(state, orderByProductNames) {
    state.orderByProductNames = orderByProductNames;
  },

  setOrdersAll(state, ordersAll) {
    state.ordersAll = ordersAll;
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
      await Promise.all(dispatch("fetchItems"));
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
