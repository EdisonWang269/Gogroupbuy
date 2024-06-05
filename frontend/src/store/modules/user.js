import { formatOrder, changeDate } from "../utils";
import { base64ToBlob, getImgURL } from "../utils";
import { Base64 } from "js-base64";
const state = {
  items: [],
  orders: [],
  storeID: "store1",
  userID: "customer1",
  currItemID: "",
  currItemNum: 0,
  userPhone: "",
  keyword: "",
  token: "",
  userName: "",
  userImg: "",
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
  setUserImg(state, userImg) {
    state.userImg = userImg;
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
    items.forEach(item => {
      item.product_picture = "data:image/png;base64,"+ item.product_picture;
      // item.product_picture = "data:application/octet-stream;base64," + item.product_picture;
      // const blob = base64ToBlob(item.product_picture, "image/png");
      // item.product_picture = getImgURL(blob);
      // console.log(item.product_picture);
      // item.product_picture = "data:application/octet-stream;base64,LzlqLzRBQVFTa1pKUmdBQkFRQUFBUUFCQUFELzJ3Q0VBQWtHQndjTkJ3Y05DQWdIQndnSEJ3MEhDQWdIQnhzSUNRY05JQjBXSWlBUkV4OGtLRFFzSkJveEhCOGJMVDB0SlRVNk16b3VIQjg3U2pNc1BDczVMamNCQ2dvS0RRME5EZzBORGk0bEZSazNLemN5Tnk0M0xUY3ZOemNyS3pjckt5c3JOeTAzTnpjck55czNLeXMzS3lzckt5MHRLeXMzTnpjd055NHROeTRySy8vQUFCRUlBS2dCTEFNQkVRQUNFUUVERVFIL3hBQWJBQUVCQVFFQkFRRUJBQUFBQUFBQUFBQUFBUU1DQmdVSEJQL0VBRGdRQVFFQkFBRURBUVFGQ1FnREFBQUFBQUFCQWdNRUJSRUdFaE1VWVNFeFFWRnhGUmNpZ1pHVW9iSFNNak5WWW5OMG9zSUhGamIveEFBYUFRRUJBUUVCQVFFQUFBQUFBQUFBQUFBQkFBSUdBd1FGLzhRQUxoRUJBUUFCQXdJQ0J3a0JBQUFBQUFBQUFBRUNBd1FSSVRFU1VSTVVJa0Z4c2ZBRkZUSXpVbUdCb2NFMC85b0FEQU1CQUFJUkF4RUFQd0R6bGpEdGthU0pJMGhJS0NBZ0tHZ2hRMGxJQ2hwQlNrSTBsS0drRUswZ2dhUVVFSzBnb0tVb0tDQklLQ2hJU0Vsc2NxK2x6WVVqU1JKR2tKQlFRRUJRMEVLR2twQVVOSUtVaEdwVXBRMGdoV2tFRFNDZ2hXa0ZCU2xCUVFKQlFVSkNUcXh5ajZVc0tjMkZJMGtTUnBDUVVFQkFVTkJDZ3BXZ0ZCUTBsSVJxVktVTklJVnBCQTBnb0lVb2FRVXBRVUVDUVVGQ1RXeHliNkhGaEtXRk9iQ2thU0pJMGhJS0NBZ0tHZ2hRVXJRQ2dvYVNrSTFLbEtHa0VLMGdnYVFVRUtVTklLVW9LQ0JJS0NtOWprWHU1c2FMaXdsTENuTmhTTkpFa2FRa0ZCQVFGRFFRb0tWb0JRVU5KU0VhbFNsRFNDRmFRUU5JS0NGS0drRktVRkJBa0ZQNnJISVBkeFkwbk5qUmNXRXBZVTVzS1JwSWtqU0VrS1VnSUNob0lVRkswZ2dLR2twQ05SS1VOSUlWcEJBMGdvSVVvYVFVcFFVRUNUKzJ4eUQyY1dFdUxHazVzYUxpd2xLVTVzS1JwSWtqU0VrS1VnSUNob0lVRkswQW9LR2twQ05KU2hwQkN0SUlHa0ZCQ2xEU0NsS0NncDlHeHh6MFoyTkZ4WVM0c2FUbXhvdUxDVXBUbXdwR2tpU05JU1FwU0FnS0dnaFFVclNDQW9hU2tJMGxLR2tFSzBnZ2FRVUVLVU5JS1VvS2ZWMWx4c3JiT3hvczdHaTRzSmNXTkp6WVM0c2FLVXB6WVVqU1JKR2tKSVVwQVFGUG85cDdGM2pyYnI4bjlEejlWbkY5bmZMUEhIdzR2M2UxZkU4L0w2enpJOGRYY2FXbCtabncrdCtiL3dCV2Y0Zm45KzQvNmw0NCtmN3gyMzYvNnJQbjlDK3E4WXVyMnZmSk16elp3OVRqbDEreVh6K3d6UEh6T08vMjF2SHBQbTg3dkc4NzFua3h2ajVNYXVONDVNZXh2Ris2ejdLOUgxeXk5WlVLQ2hwS1FqU1VvYVFRclNDQnBCUVFwUTBncFNuMmRaY1pLMHoxR3BTenNhTE94b3VMQ1hGalNjMkV1TEdpbEtjMkZJMGtTUnBDU0ZLUWVOWDZNK1BhMStqbno5WGtqdDFyM1ByL0FMajFYUTh2UTlyN2IxSE4yL29PM2R0NDk4bnd2TGVEZlVjbDgrYnV6NmZzOC9qYU1mTitYc05MSFZtZTQxTWVjc3I3MkhRK2t2VS9MMDNGemRWM1hQYWM5VFBQQnhkejdydmk1K1g5WDJmeitSOFVudWExTjV0OGNyampwZUxqeWs0T1BwdXQ3Wnk5em5lKzhkNzdiMS9EMGZ2K3lhNkxxdGRUMHZjdVQ2ZlAzeXp6N004YThmUnErV3UvSEVWeXcxNXAzUjBzYmpiN1hQRXMrdXZXY3VmWDB4MUhTZW11NWU3NCtMcWU4OXRzNjJjYzhaM3labVAwdjQyZmhKOXl3NmN3N0gyTXRmUTU2WVhvOGU5WDZBUUZEU1VoR2twUTBnaFdrRURTQ2doU2hwQlQ3MnN1TFRQV1dwV21lbzFLV2RqUloyTkZ4WVM0c2FUbXdseFkwVXBUbXdwR2tpU05JU1FwcHcvM3ZGL3E1L21XY3UxZTY5WWZEL25FNkQ0cjJmaC9mZEQ3MzIvN1Bqejl2eVU3UHl0cDR2VWMvRDM5cDhUL0FNamZGLzhBcy9jdmp2Yit2UHdudmY3SHcvaWVQWS95L1g1K2Z0SEhzK243UDhQcStIZy9uNC92OWRuMHU3ZSsvTjcyVDQvMi9pUHlycjhuZSsvdnZodkcvd0RqNCtyNWV3cCtLdkRTNDllMWZSOXVPdngrdjlaK3F2OEE1RDBSL3QrZi9xY2Z4WkhiZjlXNi9oNDU2UDBWYVFRRkRTVWhHa3BRMGdoV2tFRFNDZ2hTZ3A2TFdYRmhuckxSWjZ5MUswejFHcFV6MUdvMHpzYUxpd2x4WTBuTmhMaXhvcFNuTmhTTkpFa2FRa2VkVDZjK1Bheitsbno5WGtqdjByM1ByL3QzVmRkeTlEM1R0dlQ4M2NPZzdqMjNqeHlmQzhWNTk5UHlUejVtNVBwKzN4K01xbDl6OHZZYXVPbE05dnFaY1pZMjkySFErcmZVL0YwM0Z3OVYyclBkcDAwOGNITDNQdFcrWG40dnh2Mi96K1o0bm0xcWJQYjVaWExIVjhQUGxadytYM1BmcWp1dlhZMzFIUmR3Nm5tOGU2NE9IaTZEWEQwL1RUN3MrZm9rK2R2Ni9vYW5FZStuTnR0OExNYzVKOFp5K2w2K3VPRHBQVFhiZmVjZkwxSForMjI5YmVPK2M0NU5USDZQOExmd3MrOVkrK3ZEWSszbHI2L0hUTzlIam0zNkFVclNDQW9hU2tJMGxLR2tFSzBnZ2FRVUVLVTlQckxpcFdHZXN0Tk10WmFMUFdXcFdtZW8xS21lbzAwenNhTGl3bHhZMG5OaExpeG9wU25OaFNOSkVrYVFrK2oybnZ2ZU9pdXZ5ZjEzUDB1ZDMydDhjOGNuRHUvZjdOOHp6OC9yTHcxZHZwYXY1bUhMNjM1d1BWbitJWi9jZVA4QXBYRWZQOTI3YjlIOTFueit1dlZlOFhON3B2am1wNHQ0ZW14eGEvYko1bjZqeERQcy9iUzgraitienU5NzF2V3VUZStUazNxNzN5Y20vYjN5WDc3ZnRyVDY1Skp4SWpTUW9LVnBCQVVOSlNFYVNsRFNDRktHZ05JS0NucmRaY1RLOG1Xc3RTbG5yTFJaYXkwMHoxbHFWcG5xTlNwbnFOUnBuWTBYRmhMaXhwT2JDWEZqU1NrdWJDa2FTSkkwaEpDbElDQW9hQ0ZCU3RJSUNocEtRalNVb2FRUXBRMEJwQlQyT3N1SmVEUFdUSzB5MWxxVXM5WmFMTFdXbW1lc3RTdE05UnFWTTlScVZwblkwWEZoTGl4cE9iQ1hGalNTd2x6WVVqU1JKR2tKSVVwQVFGRFFRb0tWcEJBVU5KU0VhU2xEU0NGS0dnTko3YldYRVN2blpheTBXZXNtVnBsckxYSlo2eTBXV3N0Tk05WmFsYVo2alVxWjZqVXJUT3hvdUxDWEZqU2MyRXVMR2tsaExtd3BDa0tScENTRktRRUJRMEVLQ2xhUVFGRFNVaEdrcFEwZ2hTaHJrUGRheTRoOHJQV1dwV21Xc3RGbnJKbGFaYXkxS1dlc3ROTXRaYUxQV1dwV21lbzFLbWVvMUswenNhTGl3bHhZMG5OaExpeHBKWVM1c0tRcENrYVFraFNrQkFVTkJDZ3BTaG9CUTBsSVJwS1VOSUlVcDcvV1hFU3ZqWmF5MFdlc3ROTXRaYWhaNnlaV21Xc3RTbG5yTFRUTFdXaXoxbHFWcG5xTlNwbnFOU3RNN0dpNHNKY1dOSnpZUzRzYVNXRXViQ2tLUXBHa0pJVXBBUUZEUVFvS1VvYUFVTkpTRWFTbERTQ0g2SnFPSGZDejFscVZwbHJMUlo2eTAweTFscUZuckpsYVpheTFLV2VzdE5NdFphTFBXV3BXbWVvMUttZW8xSzA0c2FMT3dseFkwbk5oTGl4cEpZUzVzS1FwQ2thUWtoU2tCQVVOQkNncFNob0JRMGxJUnBLVUZQMGpXWEVQejJlb1N6MWxxVnBsckxSWjZ5MDB5MWxxRm5ySmxhWmF5MUtXZXN0Tk10WmFMUFdXcFdtZW8xS21lbzFLMDRzYUxPd2x4WTBuTmhMaXhwSllTNXNLUXBDa2FRa2hTa0JBVU5CQ2dwU2hvQlEwbElScEtVL1RkUnc3ODVsckxSWjZoTFBXV3BXbVdzdEZuckxUVExXV29XZXNtVnBsckxVcFo2eTAweTFsb3M5WmFsYVo2alVxWjZqVXJUaXhvczdDWEZqU2MyRXVMR2tsaExtd3BDa0tScENTRktRRUJRMEVLQ2xLR2dGRFNVaER5bi8vMlE9PQ==";
    });
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
