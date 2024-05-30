<template>
  <h1>
    <i class="bi bi-person"></i>
    個人資訊
  </h1>
  <!-- <img :src="userImg" /> -->
  <img src="../assets/user.jpg" />
  <div class="wrap">
    <div class="infoBar">
      <span>姓名</span>
      <input type="text" v-model="name" />
    </div>
    <div class="infoBar">
      <span>手機</span>
      <input
        type="text"
        v-model="phoneNum"
        @input="store.commit('setUserPhone', $event.target.value)"
        placeholder="請輸入手機號碼"
      />
    </div>
    <div class="infoBar">
      <span>會員等級</span>
      <p>{{ status }}</p>
    </div>
  </div>
  <nav-bar />
</template>

<script setup>
  import { ref } from "vue";
  import { useStore } from "vuex";
  import NavBar from "@/components/NavBar.vue";

  const store = useStore();
  const name = ref("陳以恩");
  const phoneNum = ref(store.state.userPhone);
  const status = ref("一般會員");
</script>

<style scoped>
  i {
    color: #ef2a39;
  }
  h1 {
    /* position: relative; */
    margin-left: 5%;
    margin-top: 48px;
    text-align: left;
  }
  img {
    /* position: relative; */
    display: block;
    height: 115px;
    width: auto;
    border-radius: 35px;
    margin: 60px auto;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
  }
  .infoBar {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }
  .infoBar span {
    font-size: 15px;
    color: #a9a9a9;
    text-align: left;
  }

  .infoBar p {
    border: 1px solid #eeeeee;
    border-radius: 10px;
    padding: 22px 16px;
    font-size: 16px;
    text-align: left;
  }

  .infoBar input {
    border: 1px solid #eeeeee;
    border-radius: 10px;
    padding: 22px 16px;
    font-size: 16px;
    text-align: left;
  }

  .wrap {
    display: flex;
    flex-direction: column;
    gap: 30px;
    width: 80%;
    margin: 0 auto;
  }
</style>
