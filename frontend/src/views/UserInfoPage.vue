<template>
  <h1 class="title">
    <i class="bi bi-person"></i>
    個人資訊
  </h1>
  <img :src="userImg" class="userImg" />
  <div class="wrap">
    <div class="infoBar">
      <span>姓名</span>
      <input
        type="text"
        :value="name"
        @input="store.commit('user/setUserName', $event.target.value)"
      />
    </div>
    <div class="infoBar">
      <span>手機</span>
      <input
        type="text"
        v-model="phoneNum"
        @input="store.commit('user/setUserPhone', $event.target.value)"
        placeholder="請輸入手機號碼"
      />
    </div>
    <div class="infoBar">
      <span>會員等級</span>
      <p>{{ status }}</p>
    </div>
  </div>
</template>

<script setup>
  import { computed, ref } from "vue";
  import { useStore } from "vuex";

  const store = useStore();
  const name = computed(() => store.state.user.userName);
  const phoneNum = ref(store.state.user.userPhone);
  const status = ref("一般會員");
  const userImg = computed(() => store.state.user.userImg);
</script>

<style scoped>
  .navBar {
    position: fixed;
    bottom: 0;
  }
  i {
    color: #ef2a39;
  }
  h1.title {
    margin-left: 5%;
    margin-top: 48px;
    text-align: left;
  }
  img.userImg {
    display: block;
    height: 115px;
    width: 115px;
    border-radius: 50%;
    margin: 60px auto;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s;
    transform: scale(1.3);
  }
  img.userImg:hover {
    box-shadow: 0 0 30px #ff4545;
    animation: rotateImage 2s infinite;
  }
  @keyframes rotateImage {
    0% {
      transform: scale(1.4) rotate(0deg);
    }
    50% {
      transform: scale(1.4) rotate(360deg);
    }
    100% {
      transform: scale(1.4) rotate(0deg);
    }
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
    transition: transform 0.3s;
  }
  .infoBar p:hover {
    transform: translateY(-5px);
  }

  .infoBar input {
    border: 1px solid #eeeeee;
    border-radius: 10px;
    padding: 22px 16px;
    font-size: 16px;
    text-align: left;
    transition: border-color 0.3s;
  }
  .infoBar input:focus {
    border-color: #ef2a39;
  }

  .wrap {
    display: flex;
    flex-direction: column;
    gap: 30px;
    width: 80%;
    margin: 0 auto;
    transition: transform 0.3s;
    margin-bottom: 20%;
  }
  .wrap:hover {
    transform: translateY(-10px);
  }
</style>
