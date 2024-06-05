import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import { initializeLiff } from "./liff";
import store from "./store";
import {Base64} from 'js-base64'

// initializeLiff().then(() => {
//   // Create Vue app after LIFF initialization
//   const app = createApp(App);

  // Use plugins
  app.use(store);
  app.use(router);
  app.use(ElementPlus);
  // app.prototype.$Base64 = Base64;
  app.use(Base64);
  // Mount the app
  app.mount("#app");
}).catch(error => {
  console.error('Failed to initialize LIFF', error);
});
