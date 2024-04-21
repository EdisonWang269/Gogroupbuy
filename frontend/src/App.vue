<template>
  <router-view/>
  <nav-bar />
</template>

<script>
// import HelloWorld from './views/HelloWorld.vue'
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',
  components: {
    NavBar,
  }
}
</script>

<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50; */
  /* margin-top: 60px; */
  margin: 0 auto;
  border: solid 1px rgb(211, 209, 209,0.5);
  box-shadow: 0 0 10px rgb(211, 209, 209,0.5);
  border-radius: 35px;

  height: 932px;
  width: 430px;
  position: relative;
}
</style>
