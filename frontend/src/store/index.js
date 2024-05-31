import { createStore } from "vuex";

function changeDate(oldDate) {
  const date = new Date(oldDate);
  const year = date.getFullYear();
  const month = ("0" + (date.getMonth() + 1)).slice(-2);
  const day = ("0" + date.getDate()).slice(-2);

  return `${year}/${month}/${day}`;
}

function changeStatus(status) {
  if (typeof status === "number" || Number.isInteger(status)) {
    switch (status) {
      case -1:
        return "未到貨";
      case 0:
        return "待領取";
      case 1:
        return "已領取";
      default:
        return "未到貨";
    }
  } else {
    return status;
  }
}

function formatOrder(order) {
  order.arrival_date = changeDate(order.arrival_date);
  order.launch_date = changeDate(order.launch_date);
  if (order.statement_date !== "未到貨") {
    order.statement_date = changeDate(order.statement_date);
  }
  order.receive_status = changeStatus(order.receive_status);
  return order;
}

export default createStore({
  state: {
    items: [],
    orders: [],
    storeID: "store1", // TODO: liff 接收 store_id, userID
    userID: "customer1",
    currItemID: "",
    currItemNum: 0,
    userPhone: "09123456789",
    keyword: "",
    token: "",
  },

  getters: {
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
  },

  mutations: {
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
