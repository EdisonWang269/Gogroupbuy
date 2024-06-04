<template>
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
          <el-upload
            v-model:file-list="fileList"
            class="upload-demo"
            action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
            multiple
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-remove="beforeRemove"
            :limit="3"
            :on-exceed="handleExceed"
          >
            <el-button>Click to upload</el-button>
            <template #tip>
              <div class="el-upload__tip">從電腦選擇檔案</div>
            </template>
          </el-upload>
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
          <store-button :action="'確認上架'" class="button" />
          <button class="button" id="delete" @click="deleteAll">全部刪除</button>
        </div>
      </div>
    </transition>
  </div>
</template>


<script setup>
import { ref } from 'vue';
import StoreButton from '../components/StoreButton.vue';

const name = ref("");
const price = ref("");
const supplier = ref("");
const fileList = ref([]);
const content = ref("");
const endDate = ref("");
const formVisible = ref(true);

const deleteAll = () => {
  formVisible.value = false; 

  setTimeout(() => {
    name.value = "";
    price.value = "";
    supplier.value = "";
    fileList.value = [];
    content.value = "";
    endDate.value = "";

    formVisible.value = true;
  }, 500); 
};

const handleBeforeLeave = (el) => {
  el.style.opacity = 1;
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
  border: 1px solid #D4D4D8;
  border-radius: 10px;
  background-color: #fff;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>

