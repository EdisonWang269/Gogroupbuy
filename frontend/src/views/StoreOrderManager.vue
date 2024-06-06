<template>
  <div class="all">
    <div class="header">
      <h1>顧客訂單管理與查詢</h1>
    </div>
    <div class="searchBar">
      <el-input
        v-model="searchInput"
        id="search"
        placeholder="搜尋手機、訂購商品"
      >
        <template #prefix>
          <i class="bi bi-search"></i>
        </template>
      </el-input>
    </div>

    <order-table :searchInput="searchInput" />

    <div class="num">
      <span>已領取： {{ checkedNum }}</span>
      <span>未領取： {{ uncheckedNum }}</span>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed } from "vue";
  import { useStore } from "vuex";
  import OrderTable from "@/components/OrderTable.vue";

  const store = useStore();
  const searchInput = ref("");
  const checkedNum = computed(() => store.state.manager.checkedNum);
  const uncheckedNum = computed(() => store.state.manager.uncheckedNum);
</script>

<style scoped>
  .all {
    background-color: #fafafa;
    width: 100%;
    height: 100%;
  }
  .header {
    display: flex;
    gap: 30px;
    align-items: baseline;
  }
  .bi.bi-pencil {
    color: #5c73db;
    cursor: pointer;
  }
  h1 {
    font-weight: 700;
    font-size: 32px;
    margin-left: 5%;
    padding-top: 20px;
  }
  .searchBar {
    border-radius: 10px;
    width: 90%;
    text-align: center;
    margin: 0 auto;
  }
  #search {
    margin: 0 auto;
    padding: 16px 0;
  }
  i {
    color: black;
  }
  :deep(.el-input__wrapper) {
    padding: 8px 16px;
    border-radius: 10px;
    border: 1px solid #4763e4;
  }
  .bi.bi-bell {
    cursor: pointer;
    font-size: 20px;
  }
  .pages {
    display: flex;
    width: 100%;
    /* position: absolute; */
    justify-content: center;
    /* margin: 0 auto; */
    position: absolute;
    bottom: 0;
  }

  .num {
    color: #a1a1aa;
    margin-top: 20px;
    display: flex;
    gap: 50px;
    width: 100%;
    justify-content: center;
  }

  .table {
    max-height: 55%;
  }

  .table::-webkit-scrollbar {
    width: 0;
    height: 0;
  }
</style>
