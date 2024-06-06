<template>
  <div class="card">
    <div class="card-body">
      <p class="card-title">
        <span>{{ name }}</span>
      </p>
      <p class="card-text">
        取貨期限：
        <br /><b>{{ dueDate }} </b> <br />訂單狀態：<br /><b>{{ status }}</b>
      </p>
    </div>
    <div class="imgContainer">
      <img :src="product_picture" class="card-img-top" alt="image" />
    </div>
    
  </div>
</template>

<script>
  export default {
    props: ["name", "dueDate", "status", "product_picture"],
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
    /* max-height: 200px; */
  }
  .imgContainer{
    display: flex;
    height: 100%;
    align-items: center;
  }
  
  .card-body {
    flex: 1;
    padding: 0;
  }
  .card-title {
    font-size: 24px;
    color: #ac503c;
    width: 80%;
    overflow: hidden;
    position: relative;
    white-space: nowrap;
  }

  img {
    width: 50%;
    height: 80%;
    object-fit: cover;
  }

  .card-title span {
    display: inline-block;
    animation: scroll 5s linear infinite;
    animation-delay: 0.5s;
  }

  .scrollAnimation {
  }

  @keyframes scroll {
    0% {
      transform: translateX(0);
    }
    100% {
      transform: translateX(-100%);
    }
  }
</style>
