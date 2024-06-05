import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import { initializeLiff } from "./liff";
import store from "./store";
import { Base64 } from "js-base64";
const app = createApp(App);

app.use(store);
app.use(router);
app.use(ElementPlus);
app.use(Base64);
app.mount("#app");

initializeLiff()
  .then(() => {})
  .catch((error) => {
    console.error("Failed to initialize LIFF", error);
  });
