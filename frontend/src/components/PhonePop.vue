<template>
  <div class="all">
    <div class="card">
      <h1>請輸入手機號碼</h1>
      <h3>僅需輸入一次即可通知領貨</h3>
      <div class="content">
        <input type="text" v-model="userPhone" />
      </div>
      <div class="buttonArea">
        <button id="confirm" @click="submit">確認</button>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  import { useStore } from "vuex";

  const store = useStore();
  const router = useRouter();
  const userPhone = ref("");
  const regex = /^09\d{8}$/;

  const submit = () => {
    if (!regex.test(userPhone.value)) {
      alert("請輸入正確的手機號碼，例如：0912-345-678");
    } else {
      store.commit("user/setUserPhone", userPhone.value);
      router.push("/home/item/confirm");
    }
  };
</script>

<style scoped>
  .all {
    background-color: rgba(0, 0, 0, 0.5);
    width: 100%;
    height: 100%;
    /* border-radius: 35px; */
  }

  .card {
    display: flex;
    flex-direction: column;
    text-align: center;
    justify-content: space-around;
    padding: auto, 0;
    margin: auto auto;
    top: 35%;
    border-radius: 20px;
    width: 70%;
    height: 32%;
  }
  h1 {
    margin: 0 auto;
    margin-top: 10%;
    margin-bottom: 10px;
    color: #3c2f2f;
    font-weight: 700;
    font-size: 30px;
  }
  h3 {
    font-size: 15px;
  }
  .content {
    font-size: 16px;
    /* display: flexbox; */
    text-align: center;
  }
  input {
    width: 85%;
    border: solid 1px black;
    border-radius: 10px;
    height: 65px;
    font-size: 28px;
    text-align: center;
    transition: all 0.3s;
    margin-bottom: 20px;
  }
  .buttonArea {
    text-align: center;
    margin-bottom: 10%;
  }
  button {
    border: none;
    border-radius: 12px;
    font-size: 16px;
    color: white;
    width: 38%;
    height: 48px;
    transition: all 0.3s;
    margin-top: 1%;
  }
  button:hover {
    cursor: pointer;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    transform: scale(1.05);
  }

  #cancel {
    background-color: #3c2f2f;
  }

  #confirm {
    background-color: #ef2a39;
    margin-left: 14px;
  }
</style>
