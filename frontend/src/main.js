import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import liff from "@line/liff";
import store from "./store";

liff
  .init({ liffId: "2004368945-ZXAjYNkb" })
  .then(() => {
    //TODO: get userid (要怎麼登入?)
  })
  .catch((err) => {
    console.error("LIFF 初始化失敗", err);
  });

const app = createApp(App).use(store);
app.use(ElementPlus);
app.use(router);
app.mount("#app");
