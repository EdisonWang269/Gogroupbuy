<template>
  <div class="all">
    <div class="card">
      <h1>訂單確認</h1>
      <div class="content">
        <span>您將訂購</span><br />
        <span>「{{ item.product_name }}」</span><br />
        <span>數量：「{{ orderNum }} {{ item.unit }}」</span>
      </div>
      <div class="buttonArea">
        <button id="cancel" @click="cancel">取消</button>
        <button id="confirm" @click="confirm">確認</button>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { defineEmits, computed } from "vue";
  import { useStore } from "vuex";

  const store = useStore();
  const emit = defineEmits(["cancelled", "confirmed"]);

  const item = computed(() => store.getters["user/currItem"]);
  const orderNum = computed(() => store.state.user.currItemNum);

  const cancel = () => {
    emit("cancelled");
  };

  const confirm = () => {
    emit("confirmed");

    const newOrder = {
      group_buying_id: item.value.group_buying_id,
      product_name: item.value.product_name,
      due_date: "未到貨",
      quantity: orderNum.value,
      receive_status: "未到貨",
    };
    store.commit("user/addWaitingOrder", newOrder);

    fetch("/api/order", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${store.state.user.token}`,
      },
      body: JSON.stringify({
        group_buying_id: item.value.group_buying_id,
        quantity: orderNum.value,
        product_picture: item.value.product_picture,
      }),
    });
    store.dispatch("manager/fetchOrder");
  };
</script>

<style scoped>
  .all {
    background-color: rgba(0, 0, 0, 0.5);
    width: 100vw;
    height: 100vh;
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
    position: inherit;
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
    color: #6a6a6a;
  }
  .buttonArea {
    text-align: center;
    margin-bottom: 10%;
  }
  button {
    margin-top: 10px;
    border: none;
    border-radius: 12px;
    font-size: 16px;
    color: white;
    width: 38%;
    height: 48px;
    transition: 0.3s;
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
