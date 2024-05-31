<template class="all">
  <router-view />
  <div class="header">
    <h1><i class="bi bi-house" id="homeIcon"></i>恩恩的團購商品</h1>
    <p>歡迎大家加入我的團購</p>
  </div>
  <search-bar />
  <div class="items">
    <item-card
      class="card"
      @click="checkDetail(item.group_buying_id)"
      v-for="item in items"
      :key="item.group_buying_id"
      v-bind="item"
    />
  </div>
  <!-- <nav-bar class="nav-bar" /> -->
</template>

<script setup>
  import { computed } from "vue";
  import { useStore } from "vuex";
  import { useRouter } from "vue-router";

  import SearchBar from "../components/SearchBar.vue";
  import ItemCard from "../components/ItemCard.vue";
  // import NavBar from "@/components/NavBar.vue";

  const store = useStore();
  const router = useRouter();
  const items = computed(() => store.getters.filteredItems);

  const checkDetail = (itemID) => {
    store.commit("setCurrItemID", itemID);
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
  }

  .items::-webkit-scrollbar {
    width: 0;
    height: 0;
  }

  .card {
    cursor: pointer;
    width: 90%;
    transition: all 0.3s ease;
  }

  .card:hover {
    transform: scale(1.05);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  }

  .card:hover::after,
  .card:hover::before {
    content: "";
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    transform: rotate(180deg);
    transform-origin: bottom;
    z-index: -1;
  }

  .card:hover .item-card-name {
    color: #ef2a39;
    text-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    text-transform: uppercase;
  }

  .card:hover .item-card-price {
    color: #ef2a39;
    text-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  }

  .card:hover .item-card-img {
    filter: blur(10px);
    opacity: 0.5;
  }

  .nav-bar {
    position: fixed;
    bottom: 0;
    width: 100%;
    z-index: 999;
  }
</style>
