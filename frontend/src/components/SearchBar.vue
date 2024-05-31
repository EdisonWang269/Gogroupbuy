<template>
  <div class="input-group input-group-lg" id="searchBar">
    <span class="input-group-text" id="addon-wrapping"
      ><i class="bi bi-search" id="search"></i
    ></span>
    <input
      type="text"
      class="form-control"
      placeholder="Search"
      aria-describedby="inputGroup-sizing-lg"
      v-model="keyword"
      @keydown.enter="search"
    />
  </div>
</template>

<script setup>
  import { computed } from "vue";
  import { useStore } from "vuex";
  const store = useStore();

  const keyword = computed({
    get() {
      return store.state.keyword;
    },
    set(value) {
      store.commit("setKeyword", value);
    },
  });

  const search = () => {
    store.dispatch("searchProduct");
  };
</script>

<style scoped>
  #search {
    font-size: 20px;
    transition: all 0.3s;
  }

  #searchBar {
    box-shadow: 5px 7px 8px 0px rgba(180, 180, 180, 0.5);
    border-radius: 20px;
    border: 1px solid rgba(180, 180, 180, 0.5);
    top: 20px;
    border: none;
    width: 90%;
    margin: 0 auto;
    height: 60px;
  }

  .input-group-text,
  .form-control {
    border: none;
    /* border-radius: 20px 0 0 20px; */
  }

  #searchBar:hover #search {
    transform: translateX(5px);
  }

  #searchBar:hover {
    box-shadow: 10px 10px 15px 0px rgba(180, 180, 180, 0.5);
  }
</style>
