<template>
  <button>{{ action }}</button>
</template>

<script>
  // import { ref } from 'vue';
  export default {
    props: ["action"],
    setup() {
      // const action = ref("");

      return {
        // action,
      };
    },
  };
</script>

<style scoped>
  button {
    background-color: #3c2f2f;
    border: none;
    border-radius: 20px;
    box-shadow: 3px 3px 8px 3px rgba(0, 0, 0, 0.2);
    display: block;
    width: 90%;
    font-size: 32px;
    font-weight: 700;
    color: white;
    margin: 0 auto;
    padding: 10px 0;
  }
</style>
