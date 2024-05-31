<template>
  <h1><i class="bi bi-list"></i>歷史訂單</h1>
  <select
    class="form-select"
    v-model="selected"
    @change="change"
    @focus="addFocus"
    @blur="removeFocus"
  >
    <option value="all" selected>全部訂單</option>
    <option value="unshipped">未到貨訂單</option>
    <option value="waiting">待領訂單</option>
    <option value="history">歷史訂單</option>
  </select>

  <div class="content">
    <div
      class="container"
      v-show="showUnshipped"
      :class="{ flip: showUnshipped }"
    >
      <p class="title">未到貨訂單</p>
      <div
        class="cards"
        :style="{
          marginBottom: selected !== 'all' ? '50px' : '0px',
          maxHeight: selected !== 'all' ? `${windowHeight - 375}px` : '200px',
          overflowY: 'auto',
        }"
      >
        <item-card-h
          v-for="item in unshippedList"
          class="item-card"
          :key="item.order_id"
          :img="item.product_picture"
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
        :style="{
          marginBottom: selected !== 'all' ? '50px' : '0px',
          maxHeight: selected !== 'all' ? `${windowHeight - 375}px` : '200px',
          overflowY: 'auto',
        }"
      >
        <item-card-h
          v-for="item in waitingList"
          :key="item.order_id"
          :img="item.product_picture"
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
        :style="{
          marginBottom: '50px',
          maxHeight: selected !== 'all' ? `${windowHeight - 375}px` : '200px',
          overflowY: 'auto',
        }"
      >
        <item-card-h
          v-for="item in historyList"
          :key="item.order_id"
          :img="item.product_picture"
          :name="item.product_name"
          :dueDate="item.due_date"
          :status="item.receive_status"
        />
      </div>
    </div>
  </div>
  <!-- <nav-bar class="nav-bar" /> -->
</template>

<script setup>
  import { ref, onMounted } from "vue";
  import { useStore } from "vuex";
  import ItemCardH from "../components/ItemCardH.vue";
  // import NavBar from "@/components/NavBar.vue";

  const store = useStore();
  const selected = ref("all");
  const windowHeight = ref(0);

  const showUnshipped = ref(true);
  const showWaiting = ref(true);
  const showHistory = ref(true);

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

    document.querySelector(".form-select").style.transform = "scale(1.15)";
    setTimeout(() => {
      document.querySelector(".form-select").style.transform = "scale(1)";
    }, 100);
  };

  const unshippedList = store.getters.getOrders.filter(
    (item) => item.receive_status == "未到貨"
  );
  const waitingList = store.getters.getOrders.filter(
    (item) => item.receive_status === "待領取"
  );
  const historyList = store.getters.getOrders.filter(
    (item) => item.receive_status === "已領取"
  );

  const addFocus = (event) => {
    event.target.style.boxShadow = "0 0 0";
  };

  const removeFocus = (event) => {
    event.target.style.boxShadow = "none";
  };

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

  .form-select {
    width: 150px;
    margin-left: 5%;
    margin-top: 48px;
    margin-bottom: 24px;
    cursor: pointer;
  }

  .form-select,
  .form-select option {
    background-color: #efefef8e;
    color: #333;
    border: none;
    outline: none;
    padding: 12px 24px;
    border-radius: 4px;
    appearance: none;
    font-size: 16px;
  }

  .option {
    border-radius: 1px;
    font-size: 16px;
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
    border: 3px solid #888;
    padding: 10px;
  }

  .cards::-webkit-scrollbar {
    width: 0px;
  }
  .cards:hover {
    box-shadow: inset 0 0 10px #888;
    transform: scale(1.05);
  }

  select option {
    max-width: 7px;
  }
</style>
