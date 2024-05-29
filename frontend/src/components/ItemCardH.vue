<template>
  <div class="card">
    <div class="card-body">
      <p class="card-title">{{ name }}</p>
      <p class="card-text">
        訂購日期：{{ orderDate }} //待刪除 <br />取貨期限：{{ dueDate }}
        <br />訂單狀態：{{ status }}
      </p>
    </div>
    <img :src="img" class="card-img-top" alt="..." />
  </div>
</template>

<script>
  export default {
    props: ["name", "orderDate", "dueDate", "status", "img"],
    // setup(){
    //     const name = ref("香帥芋頭蛋糕");
    //     const orderDate = ref("2024/ 5 / 10");
    //     const dueDate = ref("2024/ 5 / 30");
    //     const status = ref("已到貨待領取")
    //     return{
    //         name,
    //         orderDate,
    //         dueDate,
    //         status,
    //     };
    // }
  };
</script>

<style scoped>
  .card {
    border-radius: 20px;
    width: 90%;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    padding: 28px;
    gap: 14px;
    border: none;
    box-shadow: 0px 3px 8px 2px rgba(180, 180, 180, 0.5);
  }
  .card-body {
    padding: 0;
  }
  .card-title {
    font-size: 24px;
    color: #ac503c;
  }

  img {
    width: 120px;
    height: auto;
  }
</style>
