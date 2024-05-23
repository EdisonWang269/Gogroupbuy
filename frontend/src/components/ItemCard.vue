<template>
  <div class="card">
    <img :src="product_picture" alt="image" class="card-img-top" />
    <div class="card-body">
      <p class="card-title">{{ product_name }}</p>
      <p class="card-text">
        $ {{ price }} <br />結單日期：{{ statement_date }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: ["product_name", "price", "product_picture", "statement_date"]
};
</script>

<style scoped>
.card {
  margin: 3px;
  width: 185px;
  /* height: 240px; */
  border-radius: 20px;
  border: none;
  box-shadow: 0px 3px 8px 2px rgba(180, 180, 180, 0.5);
}

.card-img-top {
  margin: 5% auto -3%;
  width: 90%;
  height: auto;
  border-radius: 10px;
}

.card-body {
  margin: 0 auto;
  padding: 0px;
}

.card-title {
  text-align: center;
  font-size: 20px;
  color: #ac503c;
}

.card-text {
  margin-top: -18px;
  padding: 10px 5px;
  text-align: center;
  font-size: 14px;
}
</style>
