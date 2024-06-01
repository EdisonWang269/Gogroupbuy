import { changeDate } from "../utils";

const state = {
  storeID: "store1",
  userID: "manager1",
  token: "",
};

const getters = {};

const mutations = {
  setToken(state, token) {
    state.token = token;
  },
};

const actions = {
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
      // await Promise.all();
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
