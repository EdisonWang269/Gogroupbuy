<template>
  <div class="card">
    <div class="card-body">
      <p class="card-title">{{ name }}</p>
      <p class="card-text">
        取貨期限：
        <br /><b>{{ dueDate }} </b> <br />訂單狀態：<br /><b>{{ status }}</b>
      </p>
    </div>

    <!-- TODO: add real image -->
    <!-- <img :src="img" class="card-img-top" alt="..." /> -->
    <img src="../assets/user.jpg" class="card-img-top" alt="..." />
  </div>
</template>

<script>
  export default {
    props: ["name", "dueDate", "status", "img"],
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
    max-height: 200px;
  }
  .card-body {
    flex: 1;
    padding: 0;
  }
  .card-title {
    font-size: 24px;
    color: #ac503c;
  }

  img {
    width: 50%;
    height: auto;
  }
</style>
