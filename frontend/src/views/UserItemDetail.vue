<template>
  <div class="header">
    <router-link to="/"><i class="bi bi-arrow-left-short"></i></router-link>
    <h1>恩恩的團購</h1>
  </div>
  <img :src="item.product_picture" />
  <div class="main">
    <div class="namePart">
      <p class="name">
        {{ item.product_name }} <br />
        <span class="price">價格：$ {{ item.price }} / {{ item.measure }}</span>
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
  <big-button :action="buttonAct" @click="order" />
  <div class="content">
    <span>結單日期：{{ item.statement_date }}</span>
    <span>商品說明：</span>
    <span id="content">{{ item.product_describe }}</span>
  </div>
  <confirm-pop
    v-if="ordercheck"
    class="pop"
    :name="item.product_name"
    :orderNum="orderNum"
    @isCancelled="cancel"
    @confirmed="checkAndNoPhone"
  ></confirm-pop>
  <phone-pop v-if="noPhoneNum" class="pop" @isCancelled="cancel" />
  <nav-bar />
</template>

<script setup>
import { ref } from "vue";
import { useStore } from "vuex";

import BigButton from "../components/BigButton.vue";
import ConfirmPop from "@/components/ConfirmPop.vue";
import PhonePop from "../components/PhonePop.vue";
import NavBar from "@/components/NavBar.vue";

const store = useStore();

const item = store.getters.currItem;
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

const ordercheck = ref(false);
const order = () => {
  if (orderNum.value > 0) {
    store.commit("setCurrItemNum", orderNum.value);
    ordercheck.value = true;
  }
};

const noPhoneNum = ref(false);
const checkAndNoPhone = (value) => {
  if (value == true) {
    noPhoneNum.value = true;
    ordercheck.value = false;
  }
};

const cancel = (value) => {
  if (value == true) {
    ordercheck.value = false;
  }
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

img {
  width: auto;
  height: 40vh;
  /* border: 1px solid gray; */
  display: block;
  margin: 0 auto;
  margin-bottom: 5px;
  border-radius: 10px;
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

/* button{
    background-color:#3C2F2F;
    border: none;
    border-radius: 20px;
    box-shadow: 3px 3px 8px 3px rgba(0, 0, 0, 0.2);
    display: block;
    width: 90%;
    font-size: 32px;
    font-weight: 700;
    color: white;
    margin: 0 auto;
    padding: 10px 0;
} */
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
}
</style>
