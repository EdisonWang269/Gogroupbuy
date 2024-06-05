<template>
  <div class="content">
    <router-view></router-view>
  </div>
  <nav-bar class="navBar" />
</template>

<script>
  import NavBar from "@/components/NavBar.vue";
  export default {
    components: {
      NavBar,
    },
  };
</script>

<style scoped>
  .content {
    margin-bottom: 5%;
  }
  .navBar {
    position: fixed;
    bottom: 0;
  }
</style>
