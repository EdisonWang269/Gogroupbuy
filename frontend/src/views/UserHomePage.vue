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
      :img="item.product_picture"
      :name="item.product_name"
      :price="item.price"
      :measure="item.measure"
      :endDate="item.statement_date"
    />
  </div>
  <nav-bar />
</template>

<script setup>
import { computed } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import SearchBar from "../components/SearchBar.vue";
import ItemCard from "../components/ItemCard.vue";
import NavBar from "@/components/NavBar.vue";

const store = useStore();
const router = useRouter();
const items = computed(() => store.getters.filteredItems);

const checkDetail = (itemID) => {
  router.push(`/home/item/${itemID}`);
};
</script>

<style scoped>
.all {
  position: relative;
}
.header {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin: 5vh 0 0 20px;
  text-align: left;
}

h1 {
  font-weight: 800;
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
  position: relative;
  left: 6px;
  margin: 10% 10px;
  padding: 0 0 5% 0;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-row-gap: 16px;
  max-height: 63%;
  overflow: scroll;
}

.items::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.card {
  cursor: pointer;
}
</style>
