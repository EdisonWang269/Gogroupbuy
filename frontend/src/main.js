import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import "bootstrap"
import liff from '@line/liff';

liff.init({ liffId: '2004368945-ZXAjYNkb' })
  .then(() => {
    // LIFF 初始化成功，進行其他操作，例如取得用戶資訊等
  })
  .catch((err) => {
    console.error('LIFF 初始化失敗', err);
  });

const app = createApp(App);
app.use(ElementPlus);
app.use(router);
app.mount('#app')
