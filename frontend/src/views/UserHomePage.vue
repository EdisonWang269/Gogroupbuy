<template class="all">
  <router-view />
  <div class="header">
    <h1><i class="bi bi-house" id="homeIcon"></i>恩恩的團購商品</h1>
    <p>歡迎大家加入我的團購</p>
  </div>
  <search-bar />
  <!-- <img :src="testImg"> -->
  <div class="items">
    <item-card
      class="card"
      @click="checkDetail(item.group_buying_id)"
      v-for="item in items"
      :key="item.group_buying_id"
      v-bind="item"
    />
  </div>
</template>

<script setup>
  import { computed, watch } from "vue";
  import { useStore } from "vuex";
  import { useRouter } from "vue-router";

  import SearchBar from "../components/SearchBar.vue";
  import ItemCard from "../components/ItemCard.vue";

  const store = useStore();
  const router = useRouter();
  const items = computed(() => store.getters["user/filteredItems"]);

  const checkDetail = (itemID) => {
    store.commit("user/setCurrItemID", itemID);
    router.push(`/home/item/${itemID}`);
  };

</script>

<style scoped>
  .all {
    position: relative;
    height: 100vh;
    display: flex;
    flex-direction: column;
  }

  .header {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin: 5vh 0 0 20px;
    text-align: left;
  }

  h1 {
    font-weight: 500;
  }

  #homeIcon {
    margin-right: 12px;
    color: #ef2a39;
  }

  p {
    margin-top: 10px;
    font-size: 18px;
    color: #6a6a6a;
  }

  .items {
    flex: 1;
    margin: 10% 10px;
    padding-bottom: 60px; /* 確保不會被nav-bar擋住 */
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-row-gap: 16px;
    overflow-y: auto;
    place-items: center;
    overflow: visible;
  }

  .items::-webkit-scrollbar {
    width: 0;
    height: 0;
  }

  .card {
    cursor: pointer;
    width: 80%;
    transition: all 0.3s ease;
  }

  @media (hover: hover) and (pointer: fine) {
    .card:hover {
      transform: scale(1.075);
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
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
  }

  .nav-bar {
    position: fixed;
    bottom: 0;
    width: 100%;
    z-index: 999;
  }
</style>
