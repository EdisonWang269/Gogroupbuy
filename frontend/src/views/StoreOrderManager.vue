<template>
  <manager-pop
    :usage="topic"
    :original="endDate"
    :type="type"
    :customerName="customerName"
    @isCanceled="cancel"
    @check="setEndDate"
    @isChecked="check"
    v-show="popShow"
  />
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

    <order-table @singleNotify="notify()" class="table"/>

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
  import ManagerPop from "../components/ManagerPop.vue";

  const store = useStore();
  const topic = ref("");
  const popShow = ref(false);
  const type = ref("");
  const searchInput = ref("");
  const customerName = ref("");

  const checkedNum = computed(() => store.state.manager.checkedNum);
  const uncheckedNum = computed(() => store.state.manager.uncheckedNum);

  const notify = (value) => {
    topic.value = "通知";
    popShow.value = true;
    type.value = "notify";
    customerName.value = value;
  };
  const cancel = (value) => {
    popShow.value = value;
  };
</script>

<style scoped>
  .all {
    background-color: #fafafa;
    width: 100%;
    height: 80%;
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
  .noti {
    padding: 8px 11px;
    border: none;
    background-color: #dc2626;
    border-radius: 10px;
    font-size: 12px;
    color: white;
  }
  .bi.bi-bell {
    cursor: pointer;
    font-size: 20px;
  }
  .buttonList {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    width: 85%;
    margin-left: 5%;
    margin-top: 16px;
  }
  .function {
    display: flex;
    gap: 40px;
  }
  .notify {
    display: flex;
    height: fit-content;
    gap: 10px;
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

  .table{
    max-height: 55%;
  }

  .table::-webkit-scrollbar{
    width: 0;
    height: 0;
  }
</style>
