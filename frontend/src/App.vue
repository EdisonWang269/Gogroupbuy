<template>
  <router-view />
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "App",
  methods: {
    ...mapActions(["fetchItems"])
  },
  mounted() {
    this.fetchItems();
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
