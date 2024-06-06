<template>
  <div class="overlay">
    <div class="card">
      <h3>選擇團購商品</h3>
      <div class="products">
        <el-col :span="8">
      <el-dropdown trigger="click">
        <span class="el-dropdown-link">
          選擇上架團購商品<el-icon class="el-icon--right"><arrow-down /></el-icon>
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item v-for="item in items" :key="item.id" @click="setItem(item.product_name, item.product_id)">{{ item.product_name }}</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </el-col>
        <el-date-picker
            v-model="date"
            type="date"
            placeholder="Select date and time"
            class="datePicker"
          />

      </div>

      <div class="buttons">
        <store-button :action="'確認'" class="button" @click="check" />
        <button class="buttonCancel" @click="closed">取消</button>
      </div>
    </div>
    <div class="subOverlay" v-show="checked">
      <div class="subCard">
        <h3>團購確認</h3>
        <span>已開啟團購</span>
        <!-- <div>{{ products }}</div> -->

        <div class="buttons">
          <store-button :action="'確認'" class="button" @click="confirm" />
          <button class="buttonCancel" @click="closeSub">取消</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, defineProps, defineEmits, computed } from "vue";
  import StoreButton from "./StoreButton.vue";
  import { useStore } from "vuex";

  const store = useStore();
  const emit = defineEmits(["isCanceled", "isChecked", "check"]);
  const items = computed(() => store.state.manager.unloadItems);

  const item = {
    itemName: "",
    id: "",
  }
  const date = ref("");
  
  const products = ref("");
  const checked = ref(false);

  // const getProducts = () => {
  //   const checked = props.items.filter((item) => item.status === true);

  //   products.value = checked
  //     .map((check, index) => {
  //       return index === 0
  //         ? `「${check.itemName}」`
  //         : `、「${check.itemName}」`;
  //     })
  //     .join("");
  // };

  const closed = () => {
    emit("isClosed", false);
    closeSub();
  };

  const closeSub = () => {
    checked.value = false;
  };

  const check = () => {
    // getProducts();
    checked.value = true;
  };

  const confirm = async () => {
    closed();
    // const response = await fetch(`/api/product/ontheshelves`, {
    //   method: "POST",
    //   headers: {
    //     Authorization: `Bearer ${store.state.manager.token}`,
    //   },
    //   body: JSON.stringify({
    //     launch_date: new Date(),
    //     product_id: item.id,
    //     statement_date: date.value,
    //   })  
    // });
    // const data = await response.json();
    // store.commit("manager/setUnloadItems", data);
    // console.log(store.state.manager.unloadItems);
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
