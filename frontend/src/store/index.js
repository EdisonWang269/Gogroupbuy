import { createStore } from "vuex";

export default createStore({
  state: {
    items: []
  },
  getters: {},
  mutations: {
    setItems(state, items) {
      state.items = items;
    }
  },
  actions: {
    async fetchItems({ commit }) {
      const response = await fetch("/api/store1/product");
      const data = await response.json();
      console.log(data);
      commit("setItems", data);
    }
  },
  modules: {}
});
