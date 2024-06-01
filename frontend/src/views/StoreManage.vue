<template>
  <div class="all">
    <side-bar class="sideBar" />

    <div class="content">
      <store-nav class="nav" :action="firstStep" :item="secondStep" />
      <div class="con"><router-view></router-view></div>
    </div>
  </div>
</template>

<script>
  import { ref } from "vue";
  import SideBar from "../components/SideBar.vue";
  import StoreNav from "../components/StoreNav.vue";

  export default {
    components: {
      SideBar,
      StoreNav,
    },
    setup() {
      // 要透過 Vuex 綁定他現在是在哪個步驟
      const firstStep = ref("商品管理");
      const secondStep = ref("香帥芋泥蛋糕");

      return {
        firstStep,
        secondStep,
      };
    },
  };
</script>

<style scoped>
  .all {
    width: 100%;
    height: 100vh;
    /* display: flex; */
  }
  .content {
    display: flex;
    flex-direction: column;
    /* flex-grow: 1; */
    position: relative;
    left: 256px;
    /* height: calc(100% - 80px); */
    width: calc(100% - 256px);
    /* background-color: #FAFAFA; */
    height: 100%;
  }
  .sideBar {
    position: fixed;
    top: 0;
    left: 0;
  }
  .con {
    position: relative;
    height: 100%;
    flex-grow: 1;
  }
  .nav {
    position: relative;
    top: 0;
    right: 0;
    height: 80px;
    width: 100%;
    display: flex;
    align-items: center;
  }
</style>
