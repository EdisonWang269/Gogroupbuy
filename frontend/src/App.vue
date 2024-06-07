<template>
  <router-view/>
</template>

<script>
  import { mapActions } from "vuex";

  export default {
    name: "App",
    methods: {
      ...mapActions("user", ["fetchUserInit"]),
      ...mapActions("manager", ["fetchManagerInit"]),
    },
    mounted() {
      this.fetchUserInit();
      this.fetchManagerInit();
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
