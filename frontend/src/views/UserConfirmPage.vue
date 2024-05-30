<template>
  <div class="header">
    <!-- <router-link to="/"><i class="bi bi-arrow-left-short"></i></router-link> -->
    <h1>恩恩的團購</h1>
  </div>
  <h2>訂單完成<i class="bi bi-check-lg"></i></h2>
  <div class="info">
    你已成功訂購 <br />
    商品：「{{ store.getters.currItem.product_name }}」 <br />
    數量：「{{ store.state.currItemNum }}」 <br />
    <span id="sml">*領取時間與資訊請待團購主通知</span>
  </div>
  <big-button :action="action" @click="backToHome" class="back" />
  <div class="otherItem">
    <item-card
      class="card"
      @click="checkDetail(item.group_buying_id)"
      v-for="item in items"
      :key="item.group_buying_id"
      v-bind="item"
    />
  </div>
  <nav-bar />
</template>

<script setup>
  import { computed } from "vue";
  import { useRouter } from "vue-router";
  import { useStore } from "vuex";

  import ItemCard from "@/components/ItemCard.vue";
  import BigButton from "@/components/BigButton.vue";
  import NavBar from "../components/NavBar.vue";

  const action = "回到賣場";
  const router = useRouter();
  const store = useStore();
  const items = computed(() => {
    return store.getters.filteredItems.filter((item) => {
      return item.product_name !== store.getters.currItem.product_name;
    });
  });

  const backToHome = () => {
    router.push({ name: "homePage" });
  };

  const checkDetail = (itemID) => {
    store.commit("setCurrItemID", itemID);
    router.push(`/home/item/${itemID}`);
  };
</script>

<style scoped>
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
  }
  #sml {
    font-size: 20px;
  }

  .back {
    margin-top: 12px;
  }
  .otherItem {
    position: relative;
    /* left: 6px; */
    margin: 10% 0;
    padding: 0 0 5% 0;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-row-gap: 16px;
    background-color: #f3f3f3;
    border-radius: 20px;
    height: 55%;
    margin-top: 25px;
    overflow: scroll;
  }

  .items::-webkit-scrollbar {
    width: 0;
    height: 0;
  }
</style>
