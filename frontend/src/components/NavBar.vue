<template>
  <div class="navBar">
    <div class="container">
      <router-link to="/history" class="link">
        <div class="menu" @click="$emit('click-history')">
          <i class="bi bi-list"></i>
          <span class="text">歷史訂單</span>
        </div>
      </router-link>
      <router-link to="/" class="link">
        <div class="menu" @click="$emit('click-home')">
          <i class="bi bi-house"></i>
          <span class="text">團購商品列表</span>
        </div>
      </router-link>
      <router-link to="/userInfo" class="link">
        <div class="menu" @click="$emit('click-userInfo')">
          <i class="bi bi-person"></i>
          <span class="text">個人資訊</span>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
  export default {};
</script>

<style scoped>
  .navBar {
    width: 100vw;
    border-radius: 20px 20px 0 0;
    background-color: #ef2a39;
    position: absolute;
    bottom: 0;
  }

  .container {
    display: flex;
    justify-content: space-between;
  }

  .menu {
    transition: background-color 0.3s;
    /* height: 58px; */
    width: 88px;
    text-align: center;
    display: flex;
    flex-direction: column;
    cursor: pointer;
  }
  .menu:hover {
    background-color: #f0687d;
    border-radius: 20px 20px 0 0;
  }

  i {
    font-size: 35px;
    color: white;
    padding: 0;
  }

  .text {
    color: white;
    font-size: 14px;
    letter-spacing: 3%;
  }

  .link {
    text-decoration: none;
  }
</style>
