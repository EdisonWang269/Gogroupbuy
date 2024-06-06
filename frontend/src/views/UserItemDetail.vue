<template>
  <div class="header">
    <router-link to="/"><i class="bi bi-arrow-left-short"></i></router-link>
    <h1>恩恩的團購</h1>
  </div>
  <img
    :src="item.product_picture"
    class="item-img"
    @mouseenter="hoverImg"
    @mouseleave="leaveImg"
  />
  <div class="main">
    <div class="namePart">
      <p class="name">
        {{ item.product_name }} <br />
        <span class="price">價格：$ {{ item.price }} / {{ item.unit }}</span>
      </p>
    </div>
    <div class="num">
      <p>數量</p>
      <div class="orderPlace">
        <i class="bi bi-dash-square-fill" @click="minOrder"></i>
        <span>{{ orderNum }}</span>
        <i class="bi bi-plus-square-fill" @click="addOrder"></i>
      </div>
    </div>
  </div>
  <big-button :action="buttonAct" class="hover-button" @click="checkOrder" />
  <div class="content">
    <span>結單日期：{{ item.statement_date }}</span>
    <span>商品說明：</span>
    <span id="content">{{ item.product_describe }}</span>
  </div>
  <confirm-pop
    v-if="orderCheck"
    class="pop"
    :name="item.product_name"
    :orderNum="orderNum"
    @cancelled="cancel"
    @confirmed="checkAndNoPhone"
  ></confirm-pop>
  <phone-pop v-if="noPhoneNum" class="pop" @cancelled="cancel" />
  <nav-bar />
</template>

<script setup>
  import { ref } from "vue";
  import { useStore } from "vuex";
  import { useRouter } from "vue-router";

  import BigButton from "../components/BigButton.vue";
  import ConfirmPop from "@/components/ConfirmPop.vue";
  import PhonePop from "../components/PhonePop.vue";
  import NavBar from "../components/NavBar.vue";

  const store = useStore();
  const router = useRouter();

  const item = store.getters["user/currItem"];
  const buttonAct = "立即下單";
  const orderNum = ref(1);

  const addOrder = () => {
    orderNum.value++;
  };

  const minOrder = () => {
    orderNum.value--;
    if (orderNum.value < 1) {
      orderNum.value = 1;
    }
  };

  const orderCheck = ref(false);
  const checkOrder = () => {
    if (orderNum.value > 0) {
      store.commit("user/setCurrItemNum", orderNum.value);
      orderCheck.value = true;
    }
  };

  const noPhoneNum = ref(false);
  const checkAndNoPhone = () => {
    noPhoneNum.value = store.state.user.userPhone === "";

    if (orderCheck.value && !noPhoneNum.value) {
      router.push("/home/item/confirm");
    }
  };

  const cancel = () => {
    orderCheck.value = false;
  };
</script>

<style scoped>
  .content {
    margin-bottom: 20%;
  }
  .navBar {
    position: fixed;
    bottom: 0;
  }
  i {
    font-size: 28px;
    font-weight: 700;
  }

  h1 {
    font-weight: 500;
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

  .item-img {
    width: 360px;
    height: 360px;
    /* border: 1px solid gray; */
    display: block;
    margin: 0 auto;
    margin-bottom: 5px;
    border-radius: 10px;
    position: relative;
    z-index: 10;
    object-fit: cover;
  }

  .item-img:hover {
    animation: scale-up-down 2s forwards;
  }

  @keyframes scale-up-down {
    0% {
      transform: scale(1.1);
    }
    20% {
      transform: scale(1.28);
    }
    100% {
      transform: scale(1);
    }
  }

  .main {
    display: flex;
    color: #3c2f2f;
    /* gap:5%; */
    /* padding: 0 5px; */
    /* margin: 0 auto; */
    justify-content: space-evenly;
  }

  .namePart {
    display: block;
    margin-bottom: 0;
  }

  .name {
    font-size: 32px;
    font-weight: bold;
  }
  .price {
    font-weight: lighter;
    font-size: 24px;
    vertical-align: baseline;
  }

  .orderPlace {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20%;
    padding-left: 10px;
    /* padding-bottom: 40px; */
    justify-content: center;
    align-items: center;
    font-size: 24px;
  }

  i {
    color: #ef2a39;
    font-size: 45px;
    cursor: pointer;
    transition: color 0.3s;
  }
  i:hover {
    color: #d41e1e;
  }

  .num {
    position: relative;
    display: flex;
    gap: 0;
    flex-direction: column;
    justify-content: flex-start;
    align-items: baseline;
  }
  .num > p {
    font-size: 24px;
    padding: 0;
    margin-bottom: 0;
  }

  .hover-button {
    transition: background-color 0.3s, transform 0.3s;
    background-color: #3c2f2f;
    border-radius: 10px;
    padding: 5px 10px;
    cursor: pointer;
    color: white;
  }
  .hover-button:hover {
    background-color: #ef2a39;
    transform: scale(1.05);
  }

  .content {
    margin-top: 5px;
    display: flex;
    flex-direction: column;
    gap: 7px;
    font-size: 24px;
    padding: 5px 5%;
    color: #3c2f2f;
    text-align: left;
  }

  #content {
    font-size: 16px;
    color: #6a6a6a;
  }

  .pop {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 999;
  }

  .bi.bi-dash-square-fill,
  .bi.bi-plus-square-fill {
    transition: transform 0.3s, color 0.3s;
    color: #333333;
  }

  .bi.bi-dash-square-fill:hover {
    transform: scale(1.05);
    color: #333333;
  }

  .bi.bi-plus-square-fill:hover {
    transform: scale(1.15);
    color: hsl(0, 100%, 50%);
  }

  .bi.bi-dash-square-fill,
  .bi.bi-plus-square-fill :not(:hover) {
    transform: scale(1);
    color: #333333;
  }
</style>
