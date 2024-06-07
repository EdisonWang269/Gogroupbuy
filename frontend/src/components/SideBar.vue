<template>
  <div class="sideBar">
    <h1>團購系統</h1>
    <el-row class="tac">
      <el-col>
        <el-menu
          default-active="1"
          class="el-menu-vertical-demo"
          background-color="#0E1B6B"
          :style="{ '--bg-color': isSubMenuOn ? '#0e1b6b' : '#4256d0' }"
        >
          <el-sub-menu
            index="1"
            :style="{ 'background-color': isSubMenuOn ? '#4256d0' : '#0e1b6b' }"
          >
            <template #title>
              <i class="bi bi-gear"></i>
              <span>商品管理</span>
            </template>
            <el-menu-item
              class="item"
              v-for="item in items"
              :key="item.product_name"
              @click="toItem(item)"
              >{{ item.product_name }}</el-menu-item
            >
          </el-sub-menu>

          <el-menu-item index="2" @click="toOrder">
            <template #title>
              <i class="bi bi-file-earmark-text"></i>
              <span>訂單管理</span>
            </template>
          </el-menu-item>

          <el-menu-item index="3" @click="toUpload">
            <template #title>
              <i class="bi bi-laptop"></i>
              <span>上架商品</span>
            </template>
          </el-menu-item>

          <el-menu-item index="4" @click="toChart">
            <template #title>
              <i class="bi bi-shield-check"></i>
              <span>銷售數據</span>
            </template>
          </el-menu-item>
        </el-menu>
      </el-col>
    </el-row>

    <div class="managerName">
      <img src="../assets/user.jpg" />
      <div>
        <span>{{ managerName }}</span
        ><span>{{ managerMail }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, defineEmits, computed, watch } from "vue";
  import { useStore } from "vuex";
  import { useRouter } from "vue-router";

  const store = useStore();
  const router = useRouter();
  const emit = defineEmits(["start"]);
  const isSubMenuOn = ref(false);

  const managerName = ref("賴巧忍");
  const managerMail = ref("choco@gmail.com");
  const items = computed(() => store.getters["manager/getItems"]);

  watch(items, (newItems) => {
    if (items.value !== newItems) {
      items.value = [...newItems]; 
    } 
  }, { immediate: true });

  const toItem = (item) => {
    isSubMenuOn.value = true;
    store.commit("manager/setStep", "商品管理");
    store.commit("manager/setCurrItem", item);
    router.push("/manager/itemManager");
  };
  const toOrder = () => {
    isSubMenuOn.value = false;
    store.commit("manager/setStep", "訂單管理");
    router.push("/manager/orderManager");
  };
  const toUpload = () => {
    isSubMenuOn.value = false;
    store.commit("manager/setStep", "上架商品");
    router.push("/manager/upLoadItem");
  };

  const toChart = () => {
    isSubMenuOn.value = false;
    store.commit("manager/setStep", "銷售數據");
  };
</script>

<style scoped>
  .sideBar {
    color: white;
    height: 100vh;
    width: 256px;
    background-color: #0e1b6b;
  }
  h1 {
    color: white;
    text-align: center;
    font-weight: 700;
    padding: 25px 0 0 0;
  }
  i {
    margin-right: 10px;
  }
  .item {
    height: 32px;
    width: 90%;
    margin: 0 auto;
    border-radius: 10px;
  }
  span,
  i {
    color: lightgray;
    font-size: 16px;
  }
  el-sub-menu__title {
    background-color: #0e1b6b;
  }

  :deep(.el-icon.el-sub-menu__icon-arrow) {
    color: white;
    font-weight: 900;
    font-size: 15px;
  }

  :root {
    --active-color: #fff;
  }

  :deep(.el-menu-item) {
    color: white;
    font-weight: 200;
    padding: 0;
  }

  :deep(.el-menu-item.is-active) {
    color: white;
    font-weight: 700;
    background-color: var(--bg-color);
  }

  :deep(.el-menu.el-menu--inline) {
    height: 128px;
    overflow: scroll;
    overflow-x: hidden;
  }
  :deep(.el-menu.el-menu--inline)::-webkit-scrollbar {
    width: 0;
    height: 0;
  }
  .managerName {
    width: 100%;
    z-index: 5;
    display: flex;
    /* justify-content: center; */
    align-items: center;
    gap: 8px;
    position: absolute;
    bottom: 32px;
    left: 20px;
  }
  .managerName img {
    border-radius: 50%;
    width: 40px;
    height: 40px;
  }
  .managerName div {
    display: flex;
    flex-direction: column;
    color: #fff;
  }
</style>
