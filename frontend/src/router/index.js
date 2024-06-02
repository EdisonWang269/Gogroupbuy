import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "userAll",
      redirect: "/home",
      component: () => import("../views/UserAll.vue"),
      children: [
        {
          path: "home",
          name: "home",
          component: () => import("../views/UserHomePage.vue"),
        },
        {
          path: "history",
          name: "historyPage",
          component: () => import("../views/UserHistoryPage.vue"),
        },
        {
          path: "userInfo",
          name: "userInfo",
          component: () => import("../views/UserInfoPage.vue"),
        },
      ],
    },
    {
      path: "/nav",
      name: "navbar",
      component: () => import("../components/NavBar.vue"),
    },
    {
      path: "/home/item/:itemID",
      name: "userItemDetail",
      component: () => import("../views/UserItemDetail.vue"),
    },
    {
      path: "/pop",
      name: "confirm",
      component: () => import("../components/ConfirmPop.vue"),
    },
    {
      path: "/home/item/confirm",
      name: "confirmPage",
      component: () => import("../views/UserConfirmPage.vue"),
    },
    {
      path: "/storeLogIn",
      name: "storeLogIn",
      component: () => import("../views/StoreLogIn.vue"),
    },
    {
      path: "/manager",
      name: "storeManage",
      redirect: "/manager/itemManager",
      component: () => import("../views/StoreManageAll.vue"),
      children: [
        {
          path: "itemManager",
          name: "itemManager",
          component: () => import("../views/StoreItemManage.vue"),
        },
        {
          path: "orderManager",
          name: "orderManager",
          component: () => import("../views/StoreOrderManager.vue"),
        },
        {
          path: "uploadItem",
          name: "uploadItem",
          component: () => import("../views/StoreUploadItem.vue"),
        },
      ],
    },
  ],
});

export default router;
