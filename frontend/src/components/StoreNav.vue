<template>
  <div class="all">
    <nav style="--bs-breadcrumb-divider: '>'" aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item">{{ action }}</li>
        <!-- 從 vuex 抓sidebar value -->
        <li
          class="breadcrumb-item active"
          aria-current="page"
          v-if="action === '商品管理'"
        >
          {{ item }}
        </li>
        <!-- 從 vuex 抓商品名稱 -->
      </ol>
    </nav>
  </div>
</template>

<script>
  export default {
    props: ["action", "item"],
  };
</script>

<style scoped>
  .all {
    width: 100%;
    display: flex;
    vertical-align: center;
    align-items: center;
    justify-items: center;
    /* height: 80px; */
    padding-left: 40px;
    background-color: #fff;
  }
  .all nav {
    height: 100%;
    padding-top: 25px;
    margin: auto 0;
    display: block;
    text-align: center;
  }
  .breadcrumb-item.active {
    color: #4658ac;
  }
</style>
