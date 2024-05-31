<template>
  <button class="button">{{ action }}<span v-html="icon"></span></button>
</template>

<script>
  export default {
    props: ["action", "icon"],
  };
</script>

<style scoped>
  .button {
    background-color: #4763e4;
    text-align: center;
    border-radius: 12px;
    color: #fff;
    padding: 13px;
    border: none;
  }
</style>
