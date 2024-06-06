<template>
  <div class="card">
    <div class="wrapper">
      <div class="imgContainer">
        <img :src="product_picture" alt="image" class="card-img-top" />
      </div>
    </div>
    
    
    <div class="card-body">
      <p class="card-title">{{ product_name }}</p>
      <p class="card-text">
        價錢: <b>$ {{ price }} / {{ unit }}</b> <br />結單日期：<b>{{
          statement_date
        }}</b>
      </p>
    </div>
  </div>
</template>

<script>
  export default {
    props: [
      "product_name",
      "price",
      "product_picture",
      "statement_date",
      "unit",
    ],
  };
</script>

<style scoped>
  .card {
    margin: 3px;
    width: 90%;
    height: auto;
    border-radius: 20px;
    border: none;
    box-shadow: 0px 3px 8px 2px rgba(180, 180, 180, 0.5);
    /* text-align: center; */
  }
  .wrapper{
    width: 100%;
    display: flex;
    justify-content: center;
  }
  .imgContainer{
    width: 120px;
    height: 120px;
    
  }
  .card-img-top {
    margin: 5% auto -3%;
    width: 100%;
    height: 100%;
    border-radius: 10px;
    object-fit: cover;
  }

  .card-body {
    margin: 0 auto;
    padding: 0px;
  }

  .card-title {
    text-align: center;
    font-size: 20px;
    color: #ac503c;
    margin-top: 12px;
  }

  .card-text {
    margin-top: -18px;
    padding: 10px 5px;
    text-align: center;
    font-size: 14px;
  }
</style>
