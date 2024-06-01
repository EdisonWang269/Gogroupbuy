<template>
  <div class="header">
    <h1>恩恩的團購</h1>
  </div>
  <h2>訂單完成<i class="bi bi-check-lg"></i></h2>
  <div class="info">
    你已成功訂購 <br />
    商品：「{{ currItem.product_name }}」 <br />
    數量：「{{ currItemNum }} {{ currItem.unit }}」
    <br />
    <span id="sml">*領取時間與資訊請待團購主通知</span>
  </div>
  <big-button :action="action" @click="backToHome" class="back" />
  <div class="otherItem">
    <!-- <div
      style="transform: scale(1.1)" 
    > -->
      <item-card 
        v-bind="item" 
        
        class="card"
        v-for="item in items"
        :key="item.group_buying_id"
        @click="checkDetail(item.group_buying_id)"
        :class="{ 'card-hover': hoveredItem === item.group_buying_id }"
        @mouseenter="hoveredItem = item.group_buying_id"
        @mouseleave="hoveredItem = null"
      />
    <!-- </div> -->
  </div>
  <nav-bar class="navBar" />
</template>

<script setup>
  import { computed, ref } from "vue";
  import { useRouter } from "vue-router";
  import { useStore } from "vuex";

  import ItemCard from "@/components/ItemCard.vue";
  import BigButton from "@/components/BigButton.vue";
  import NavBar from "../components/NavBar.vue";

  const action = "回到賣場";
  const router = useRouter();
  const store = useStore();

  const currItem = computed(() => store.getters["user/currItem"]);
  const currItemNum = computed(() => store.state.user.currItemNum);
  const items = computed(() => {
    return store.getters["user/filteredItems"].filter((item) => {
      return item.product_name !== store.getters["user/currItem"].product_name;
    });
  });

  const backToHome = () => {
    router.push({ name: "home" });
  };

  const checkDetail = (itemID) => {
    store.commit("user/setCurrItemID", itemID);
    router.push(`/home/item/${itemID}`);
  };

  const hoveredItem = ref(null);
</script>

<style scoped>
  .navBar {
    position: fixed;
    bottom: 0;
  }
  i {
    font-size: 28px;
    font-weight: 700;
  }

  h1 {
    font-weight: 700;
    display: inline-block;
    text-align: center;
    position: relative;
    margin: 0 auto;
    overflow-x: hidden;
  }

  .header {
    display: flex;
    padding: 20px 12px 0 12px;
    justify-content: flex-start;
    align-items: center;
  }
  h2 {
    color: #ef2a39;
    font-weight: 700;
    text-align: center;
  }

  .info {
    font-size: 24px;
    color: #6a6a6a;
    margin-left: 8%;
    line-height: 1.7;
    margin-top: 10px;
    text-align: left;
    transition: all 0.3s ease;
  }
  #sml {
    font-size: 20px;
  }

  .back {
    margin-top: 12px;
    transition: all 0.3s ease;
  }
  .back:hover {
    transform: scale(1.05);
  }
  .otherItem {
    position: relative;
    margin: 10% 0;
    padding: 0 0 5% 0;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-row-gap: 16px;
    border-radius: 20px;
    height: 55%;
    margin-top: 25px;
    transition: all 0.3s ease;
    overflow-x: hidden;
    place-items: center;
    overflow: visible;
  }

  .card {
    /* margin-top: 12px; */
    /* background-color: transparent; */
    /* border: none; */
    /* position: relative; */
    /* display: flex; */
    /* justify-content: center; */
    align-items: center;
    transition: all 0.3s ease;
    width: 90%;
  }

  .card-hover {
    transform: scale(1.05);
    animation: shakeAndScale 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
    animation-iteration-count: infinite;
  }

  @keyframes shakeAndScale {
    10%,
    90% {
      transform: translate3d(-1px, 0, 0) scale(1.075);
    }
    20%,
    80% {
      transform: translate3d(2px, 0, 0) scale(1.075);
    }
    30%,
    50%,
    70% {
      transform: translate3d(-4px, 0, 0) scale(1.075);
    }
    40%,
    60% {
      transform: translate3d(4px, 0, 0) scale(1.075);
    }
    0%,
    100% {
      transform: translate3d(0, 0, 0) scale(1.05);
    }
  }
</style>
