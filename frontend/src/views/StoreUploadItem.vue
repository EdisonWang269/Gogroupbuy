<template>
  <start-group-buy v-if="checked" :date="endDate" @isClosed="close"></start-group-buy>
  <div class="all">
    <div class="header">
      <h1>上架商品</h1>
    </div>
    <transition name="fade" @before-leave="handleBeforeLeave">
      <div v-if="formVisible" class="uploadArea">
        <div>
          <span>商品名稱</span>
          <el-input class="input" v-model="name"></el-input>
        </div>
        <div>
          <span>照片檔案</span>
          <div>
            <input type="file" class="upload" @change="onfile" />
          </div>
        </div>
        <div>
          <span>商品供應商</span>
          <el-input class="input" v-model="supplier"></el-input>
        </div>
        <div>
          <span>商品價格（寫法： 250/個）</span>
          <el-input class="input" v-model="price"></el-input>
        </div>
        <div>
          <span>結單日期</span>
          <div class="block">
            <el-date-picker
              v-model="endDate"
              type="date"
              placeholder="Select date and time"
            />
          </div>
        </div>
        <div>
          <span>商品說明</span>
          <textarea v-model="content"></textarea>
        </div>
        <div class="buttons">

          <store-button :action="'確認上架'" class="button" @click="uploadProduct()"/>
          <button class="button" id="delete" @click="deleteAll">全部刪除</button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { useStore } from 'vuex';
import { computed, ref } from 'vue';
import { ElMessage } from 'element-plus'
import StoreButton from '../components/StoreButton.vue';
import StartGroupBuy from '@/components/StartGroupBuy.vue';

const store = useStore();
const name = ref("");
const productPrice = ref("");
const price = ref("");
const supplier = ref("");
const file = ref([]);
const content = ref("");
const endDate = ref();
const formVisible = ref(true);
const unit = ref("");
const form= new FormData();

const onfile = (event) =>{
  file.value = event.target.files[0];
  form.append('photo', file.value);  // return form;
};

const checked = ref(false);
const check = () =>{
  checked.value = true;
}

const uploadProduct = async () => {
  if(isNull()){
    ElMessage({
      message: '尚未輸入完整上架訊息',
      type: 'warning',
    })
  }
  else{
    check();
    const part = price.value.split('/');
    productPrice.value = part[0];
    unit.value = part[1];

    form.append('price', productPrice.value);
    form.append('product_describe', content.value);
    form.append('product_name', name.value);
    form.append('supplier_name', supplier.value);
    form.append('unit', unit.value);
    //新增商品
    const response1 = await fetch(`/api/product`, {
      method: "POST",
      headers: {
        // 'Content-Type': 'multipart/form-data',
        Authorization: `Bearer ${store.state.manager.token}`,
      },
      body:form,
    });
    console.log(response1);
    await store.dispatch('manager/fetchUnloadItems');
    
  }
  };

  const clearAll = () =>{
    name.value = "";
    price.value = "";
    supplier.value = "";
    file.value = "";
    content.value = "";
    endDate.value = "";
  }
const deleteAll = () => {
  formVisible.value = false; 

  setTimeout(() => {
    name.value = "";
    price.value = "";
    supplier.value = "";
    file.value = [];
    content.value = "";
    endDate.value = "";

    formVisible.value = true;
  }, 500); 
};

const handleBeforeLeave = (el) => {
  el.style.opacity = 1;
};

const isNull = () => {
  if(name.value == "" || price.value == "" || supplier.value == "" || file.value == [] || content.value == "" || endDate.value == ""){
    return true;
  }
  else{
    return false;
  }
}

const close = (value) =>{
  checked.value = value;
  clearAll();
};

</script>

<style scoped>
  .all {
    background-color: #fafafa;
    width: 100%;
    height: 100%;
  }
  .header {
    display: flex;
    gap: 30px;
    align-items: baseline;
  }
  h1 {
    font-weight: 700;
    font-size: 32px;
    margin-left: 5%;
    padding-top: 20px;
  }
  .uploadArea {
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin: 0 auto;
    width: 90%;
  }
  .input {
    width: 100%;
  }
  textarea {
    resize: none;
    display: block;
    width: 100%;
    border: 1px solid #c8c8c8;
    border-radius: 12px;
    padding: 16px;
    height: 150px;
  }
  .buttons {
    display: flex;
    gap: 10px;
  }
  .button {
    width: 200px;
    height: 48px;
  }
  #delete {
    border: 1px solid #d4d4d8;
    border-radius: 10px;
    background-color: #fff;
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease;
  }

  .fade-enter,
  .fade-leave-to {
    opacity: 0;
  }

  ::-webkit-file-upload-button {
    border: 1px solid lightgrey;
    border-radius: 5px;
    padding: 5px 10px;
    background-color: white;
    cursor: pointer;
  }
</style>
