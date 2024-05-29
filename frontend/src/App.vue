<template>
  <router-view />
</template>

<script>
  import { mapState, mapActions } from "vuex";

  export default {
    name: "App",
    methods: {
      ...mapState(["items"]),
      ...mapActions(["fetchItems", "fetchOrders"]),
    },
    mounted() {
      this.fetchItems();
      this.fetchOrders();
    },
  };
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
</style>
