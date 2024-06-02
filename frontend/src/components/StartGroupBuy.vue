<template>
    <div class="overlay">
      <div class="card">
        <h3>選擇團購商品</h3>
        <div class="products">
            <div v-for="item in props.items" :key="item.id"> 
                <span>{{ item.itemName }}</span> 
                <el-checkbox v-model="item.status" size="large" class="checkbox"/>
            </div>
        </div>

        <div class="buttons">
          <store-button :action="'確認'" class="button" @click="check" />
          <button class="buttonCancel" @click="closed">取消</button>
        </div>
      </div>
      <div class="subOverlay" v-show="checked">
        <div class="subCard" >
            <h3>團購確認</h3>
            <span>開啟團購</span>
            <div>{{ products }}</div>

            <div class="buttons">
                <store-button :action="'確認'" class="button" @click="confirm" />
                <button class="buttonCancel" @click="closeSub">取消</button>
            </div>
        </div>
      </div>   
      
    </div>
  </template>
  
  <script setup>
  import { ref, defineProps ,defineEmits } from "vue";
  import StoreButton from "./StoreButton.vue";
  const emit = defineEmits(["isCanceled", "isChecked", "check"]);
  const props = defineProps(["items"]);

  const products = ref("");
  const checked = ref(false);

  const getProducts = () => {
    const checked = props.items.filter(item => item.status === true);

    products.value = checked.map((check, index) => {
            return index === 0 ? `「${check.itemName}」` : `、「${check.itemName}」`;
        }).join('');
    }

  const closed = () => {
    emit("isClosed", false);
    closeSub();
  }

  const closeSub = () => {
    checked.value = false;
  }

  const check = () => {
    getProducts();
    checked.value = true;
  }

  const confirm = () => {
    closed();
  }

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

    .products{
        font-size:20px;
    }

    .products div{
        justify-content: center;
        align-items: baseline;
        display: flex;
        gap: 12px;
    }
    

    :deep(.el-checkbox__input.is-checked > .el-checkbox__inner)  {
        background-color: #4318ff;
        border-color: #4318ff;
    }

    :deep(.el-checkbox__inner)  {
        /* background-color: #4318ff; */
        width: 30px;
        border-color: #4318ff;
    }
    .subCard{
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
    .subOverlay{
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
  