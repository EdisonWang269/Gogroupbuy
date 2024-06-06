<template>
  <div class="header" @click="selected = 'all'">
    <h1><i class="bi bi-list"></i>歷史訂單</h1>
  </div>

  <div class="content">
    <div
      class="container"
      v-show="showUnshipped"
      :class="{ flip: showUnshipped }"
    >
      <p class="title">未到貨訂單</p>
      <div
        class="cards"
        @click="selected = 'unshipped'"
        :style="{
          marginBottom: selected !== 'all' ? '50px' : '0px',
          maxHeight: selected !== 'all' ? `${windowHeight - 325}px` : '200px',
          overflowY: 'auto',
        }"
      >
        <item-card-h
          v-for="item in unshippedList"
          class="item-card"
          :key="item.order_id"
          :product_picture="item.product_picture"
          :name="item.product_name"
          :dueDate="item.due_date"
          :status="item.receive_status"
        />
      </div>
    </div>

    <div class="container" v-show="showWaiting" :class="{ flip: showWaiting }">
      <p class="title">待領訂單</p>
      <div
        class="cards"
        id="wait"
        @click="selected = 'waiting'"
        :style="{
          marginBottom: selected !== 'all' ? '50px' : '0px',
          maxHeight: selected !== 'all' ? `${windowHeight - 325}px` : '200px',
          overflowY: 'auto',
        }"
      >
        <item-card-h
          v-for="item in waitingList"
          :key="item.order_id"
          :product_picture="item.product_picture"
          :name="item.product_name"
          :dueDate="item.due_date"
          :status="item.receive_status"
        />
      </div>
    </div>

    <div class="container" v-show="showHistory" :class="{ flip: showHistory }">
      <p class="title">歷史訂單</p>
      <div
        class="cards"
        id="history"
        @click="selected = 'history'"
        :style="{
          marginBottom: '50px',
          maxHeight: selected !== 'all' ? `${windowHeight - 325}px` : '200px',
          overflowY: 'auto',
        }"
      >
        <item-card-h
          v-for="item in historyList"
          :key="item.order_id"
          :product_picture="item.product_picture"
          :name="item.product_name"
          :dueDate="item.due_date"
          :status="item.receive_status"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, watch } from "vue";
  import { useStore } from "vuex";
  import ItemCardH from "../components/ItemCardH.vue";

  const store = useStore();
  const selected = ref("all");
  const windowHeight = ref(0);

  const showUnshipped = ref(true);
  const showWaiting = ref(true);
  const showHistory = ref(true);

  watch(selected, () => {
    change();
  });

  const change = () => {
    if (selected.value === "all") {
      showUnshipped.value = true;
      showWaiting.value = true;
      showHistory.value = true;
    } else if (selected.value === "unshipped") {
      showUnshipped.value = true;
      showWaiting.value = false;
      showHistory.value = false;
    } else if (selected.value === "waiting") {
      showUnshipped.value = false;
      showWaiting.value = true;
      showHistory.value = false;
    } else if (selected.value === "history") {
      showUnshipped.value = false;
      showWaiting.value = false;
      showHistory.value = true;
    }
  };

  const unshippedList = store.getters["user/getOrders"].filter(
    (item) => item.receive_status == "未到貨"
  );
  const waitingList = store.getters["user/getOrders"].filter(
    (item) => item.receive_status === "待領取"
  );
  const historyList = store.getters["user/getOrders"].filter(
    (item) => item.receive_status === "已領取"
  );

  onMounted(() => {
    windowHeight.value = window.innerHeight;
    window.addEventListener("resize", () => {
      windowHeight.value = window.innerHeight;
    });
  });
</script>

<style scoped>
  h1 {
    margin-top: 48px;
    margin-left: 5%;
    text-align: left;
    cursor: pointer;
  }

  i {
    color: #ef2a39;
    font-weight: 700;
  }

  .nav-bar {
    position: fixed;
    bottom: 0;
    width: 100%;
    z-index: 999;
  }
  .header {
    display: flex;
    margin-bottom: 7%;
  }
  .content {
    display: flex;
    flex-direction: column;
    gap: 20px;
    perspective: 1000px;
    margin-bottom: 65px;
  }

  .container {
    position: relative;
    transition: transform 0.6s;
    transform-style: preserve-3d;
  }

  .title {
    font-size: 25px;
    text-decoration: underline;
    text-align: left;
    margin-left: 5%;
  }

  .cards {
    display: flex;
    flex-direction: column;
    gap: 10px;
    transition: max-height 0.6s;
    padding-right: 10px;
    border: 1px solid lightgrey;
    /* border-right: 1px solid lightgrey; */
    border-radius: 5px;
    padding: 10px;
  }

  .cards::-webkit-scrollbar {
    width: 0px;
  }
  .cards:hover {
    box-shadow: inset 0 0 10px #c8c7c7;
    transform: scale(1.02);
  }
</style>
