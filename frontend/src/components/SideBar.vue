<template>
  <div class="sideBar">
    <h1>團購系統</h1>
    <el-row class="tac">
      <el-col>
        <el-menu
          default-active="1"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          background-color="#0E1B6B"
        >
          <el-sub-menu index="1">
            <template #title>
              <i class="bi bi-gear"></i>
              <span>商品管理</span>
            </template>
            <el-menu-item
              class="item"
              v-for="(item, index) in 4"
              :key="index"
              :index="`1-${index + 1}`"
              @click="toItem"
              >{{ itemName }}</el-menu-item
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
          <el-menu-item index="4">
            <template #title>
              <i class="bi bi-shield-check"></i>
              <span>銷售數據</span>
            </template>
          </el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
    <div class="managerName">
      <img src="../assets/user.jpg">
      <div><span>{{ managerName }}</span><span>{{ managerMail }}</span></div> 
    </div>
  </div>
</template>

<script>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  export default {
    setup(props, { emit }) {
      const managerName = ref("賴巧忍");
      const managerMail = ref("choco@gmail.com");
      const router = useRouter();
      const itemName = ref("香帥芋泥蛋糕");
      const itemList = ref([]);
      const toItem = () => {
        emit("tellName", itemName.value);
        router.push("/manager/itemManager");
      };
      const toOrder = () => {
        router.push("/manager/orderManager");
      };
      const toUpload = () => {
        router.push("/manager/upLoadItem");
      };
      return {
        itemName,
        itemList,
        toItem,
        toOrder,
        toUpload,
        managerName,
        managerMail,
      };
    },
  };
</script>

<style scoped>
  .sideBar {
    color: white;
    height: 100vh;
    width: 256px;
    background-color: #0e1b6b;

    /* position: relative;
    left: 0;
    top: 0; */
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

  ::v-deep .el-icon.el-sub-menu__icon-arrow {
    color: white;
    font-weight: 900;
    font-size: 15px;
  }

  :root {
    --active-color: #fff;
  }

  :deep(.el-menu-item){
    color: white;
    font-weight: 200;
    padding: 0;
    /* height: 35px; */
  }

  :deep(.el-menu-item.is-active){
    color: white;
    font-weight: 700;
    background-color: #4256d0;
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
  .managerName img{
    border-radius: 50%;
    width: 40px;
    height: 40px;
  }
  .managerName div{
    display:flex;
    flex-direction: column;
    color: #fff;
  }
</style>
