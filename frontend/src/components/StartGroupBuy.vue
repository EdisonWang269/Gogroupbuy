<template>
  <div class="overlay">
    <div class="subOverlay">
      <div class="subCard">
        <h3>團購確認</h3>
        <span>是否確認上架？</span>
        <!-- <div>{{ products }}</div> -->

        <div class="buttons">
          <store-button :action="'確認'" class="button" @click="confirm" />
          <button class="buttonCancel" @click="closed">取消</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, defineProps, defineEmits, computed, watch, onMounted } from "vue";
  import StoreButton from "./StoreButton.vue";
  import { useStore } from "vuex";
  import { ElMessage } from "element-plus";

  const store = useStore();
  const emit = defineEmits(["isClosed", "isChecked", "checked"]);
  const props = defineProps(['date']);
  
  const items = computed(() => store.getters["manager/getUnloadItem"]);
  const item = ref(null);

  const updateItem = () => {
  if (items.value && items.value.length > 0) {
    item.value = items.value[items.value.length - 1];
  } else {
    item.value = null;
  }
};

  const loadItems = async () => {
    await store.dispatch('manager/fetchUnloadItems');
    updateItem();
  };

  onMounted(() => {
    loadItems();
  });

  watch(items, (newItems) => {
    if (newItems.length > 0) {
      item.value = newItems[newItems.length - 1];
    } else {
      item.value = null;
    }
  }, { immediate: true });

  const closed = () => {
    emit("isClosed", false);
  };

  const confirm = async () => {
    ElMessage({
      message: '已成功新增商品',
      type: 'success',
    });
    closed();
    emit("checked", false);
    console.log(items.value);
    // 確保 item 不為 null
    if (item.value) {
      const response = await fetch(`/api/product/ontheshelves`, {
        method: "POST",
        headers: {
          'Authorization': `Bearer ${store.state.manager.token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          launch_date: new Date().toUTCString(),
          product_id: item.value.product_id,
          statement_date: props.date ,
        })  
      });
      console.log(response);
      await store.dispatch('manager/fetchItems');
      await store.dispatch('manager/fetchOrders');
      await store.dispatch('user/fetchItems');
    } else {
      console.error('No item available to post');
    }
  };
</script>

<style scoped>
  .overlay {
    position: absolute;
    left: 0;
    top: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100vh;
    position: fixed;
    background-color: rgba(0, 0, 0, 0.6);
    z-index: 5;
  }
  .card {
    display: flex;
    flex-direction: column;
    text-align: center;
    gap: 40px;
    /* margin: 0 auto; */
    padding: 32px;
    width: 40%;
    height: fit-content;
    background-color: white;
    border-radius: 12px;
  }
  h3 {
    font-weight: bold;
  }
  .buttons {
    display: flex;
    gap: 8px;
    justify-content: center;
  }
  .button {
    width: 200px;
    height: 100%;
  }
  .buttonCancel {
    width: 200px;
    height: 100%;
    padding: 13px;
    border: 1px #d4d4d8 solid;
    border-radius: 10px;
    background-color: white;
  }
  #cancel {
    height: 100%;
    border-radius: 10px;
  }

  .products {
    font-size: 20px;
  }

  .products div {
    justify-content: center;
    align-items: baseline;
    display: flex;
    gap: 12px;
  }

  :deep(.el-checkbox__input.is-checked > .el-checkbox__inner) {
    background-color: #4318ff;
    border-color: #4318ff;
  }

  :deep(.el-checkbox__inner) {
    /* background-color: #4318ff; */
    width: 30px;
    border-color: #4318ff;
  }
  .subCard {
    display: flex;
    flex-direction: column;
    text-align: center;
    gap: 40px;
    /* margin: 0 auto; */
    padding: 32px;
    width: 20%;
    height: fit-content;
    background-color: white;
    border-radius: 12px;
  }
  .subOverlay {
    position: absolute;
    left: 0;
    top: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100vh;
    position: fixed;
    background-color: rgba(0, 0, 0, 0.2);
    z-index: 6;
  }
</style>
