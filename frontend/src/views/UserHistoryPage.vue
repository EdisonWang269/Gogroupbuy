<template>
  <h1><i class="bi bi-list"></i>歷史訂單</h1>
  <select class="form-select" v-model="selected" @change="change">
    <option selected value="all">所有訂單</option>
    <option value="history">歷史訂單</option>
    <option value="waiting">待領訂單</option>
  </select>
  <div class="content">
    <div class="wait" v-show="showWaiting">
      <p class="title">待領清單</p>
      <div class="cards">
        <item-card-h
          v-for="item in waitingList"
          :key="item.order_id"
          :img="item.product_picture"
          :name="item.product_name"
          :dueDate="item.statement_date"
          :status="item.receive_status"
        />
      </div>
    </div>

    <div class="history" v-show="showHistory">
      <p class="title">歷史清單</p>
      <div class="cards" id="history">
        <item-card-h
          v-for="item in historyList"
          :key="item.order_id"
          :img="item.product_picture"
          :name="item.product_name"
          :dueDate="item.statement_date"
          :status="item.receive_status"
        />
      </div>
    </div>
  </div>
  <nav-bar />
</template>

<script setup>
  import { ref } from "vue";
  import { useStore } from "vuex";
  import ItemCardH from "../components/ItemCardH.vue";
  import NavBar from "@/components/NavBar.vue";

  const selected = ref("all");
  const showHistory = ref(true);
  const showWaiting = ref(true);

  const store = useStore();
  const waitingList = store.getters.waitingOrders;
  const historyList = store.getters.historyOrders;

  const change = () => {
    if (selected.value == "all") {
      showHistory.value = true;
      showWaiting.value = true;
    } else if (selected.value == "history") {
      showHistory.value = true;
      showWaiting.value = false;
    } else {
      showHistory.value = false;
      showWaiting.value = true;
    }
  };
</script>

<style scoped>
  h1 {
    margin-top: 48px;
    margin-left: 5%;
    text-align: left;
  }
  i {
    /* font-size: 28px; */
    color: #ef2a39;
    font-weight: 700;
  }
  .form-select {
    width: 120px;
    margin-left: 5%;
    margin-top: 48px;
    margin-bottom: 24px;
  }
  .option {
    border-radius: 1px;
    font-size: 16px;
  }

  .cards {
    display: grid;
    row-gap: 20px;
  }

  .content {
    height: 68%;
    overflow: scroll;
    padding: 10px 0;
  }
  .content::-webkit-scrollbar {
    width: 0;
    height: 0;
  }
  .title {
    font-size: 20px;
    text-decoration: underline;
    text-align: left;
    margin-left: 5%;
  }
  .wait {
    margin-bottom: 30px;
  }
</style>
