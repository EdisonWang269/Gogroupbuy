import { createStore } from "vuex";
import user from "./modules/user";
import manager from "./modules/manager";

export default createStore({
  modules: {
    user,
    manager,
  },
});
