<template>
  <div class="all">
    <div class="card">
      <h1>請輸入手機號碼</h1>
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

//TODO: 與資料庫的互動?
const submit = () => {
  if (userPhone.value == "") {
    alert("請輸入手機號碼");
  } else {
    store.commit("setUserPhone", userPhone.value);
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
  /* gap: 24px; */
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
  color: #3c2f2f;
  font-weight: 700;
  font-size: 32px;
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
}

#cancel {
  background-color: #3c2f2f;
}

#confirm {
  background-color: #ef2a39;
  margin-left: 14px;
}
</style>
