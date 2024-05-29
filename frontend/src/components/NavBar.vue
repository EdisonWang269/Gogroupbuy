<template>
  <div class="navBar">
    <div class="container">
      <router-link to="/history" class="link">
        <div class="menu">
          <i class="bi bi-list"></i>
          <span class="text">歷史訂單</span>
        </div>
      </router-link>
      <router-link to="/" class="link">
        <div class="menu">
          <i class="bi bi-house"></i>
          <span class="text">團購商品列表</span>
        </div>
      </router-link>
      <router-link to="/userInfo" class="link">
        <div class="menu">
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
    /* padding: 9px, 46px; */
    position: absolute;
    bottom: 0;
  }

  .container {
    display: flex;
    /* gap: 13%; */
    justify-content: space-between;
  }

  .menu {
    /* height: 58px; */
    width: 88px;
    text-align: center;
    display: flex;
    flex-direction: column;
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
