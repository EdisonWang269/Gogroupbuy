import { createStore } from "vuex";
import user from "./modules/user";
import manager from "./modules/manager";

export default createStore({
  state: { token: "" },

  mutations: {
    setToken(state, token) {
      state.token = token;
    },
  },

  actions: {
    async fetchToken({ commit, state }) {
      const response = await fetch(`/api/user`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          userid: state.user.userID,
          store_id: state.user.storeID,
        }),
      });
      const data = await response.json();
      commit("setToken", data.access_token);
    },

    async fetchInit({ dispatch }) {
      try {
        await dispatch("fetchToken");
        await Promise.all([
          dispatch("user/fetchItems"),
          dispatch("user/fetchOrders"),
        ]);
      } catch (error) {
        console.error("Error in fetchInit:", error);
      }
    },
  },

  modules: {
    user,
    manager,
  },
});
