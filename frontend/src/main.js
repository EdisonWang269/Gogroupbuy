import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import { initializeLiff } from "./liff";
import store from "./store";

// initializeLiff().then(() => {
//   // Create Vue app after LIFF initialization
//   const app = createApp(App);

//   // Use plugins
//   app.use(store);
//   app.use(router);
//   app.use(ElementPlus);
//   // Mount the app
//   app.mount("#app");
// }).catch(error => {
//   console.error('Failed to initialize LIFF', error);
// });

const app = createApp(App).use(store);
app.use(ElementPlus);
app.use(router);
app.mount("#app");
