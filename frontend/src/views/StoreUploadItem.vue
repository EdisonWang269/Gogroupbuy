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
          <store-button :action="'確認上架'" class="button" @click="submit" />
          <button class="button" id="delete" @click="deleteAll">
            全部刪除
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
  import { useStore } from "vuex";
  import { ref } from "vue";
  import StoreButton from "../components/StoreButton.vue";

  const name = ref("");
  const price = ref("");
  const supplier = ref("");
  const file = ref();
  const encodeFile = ref("");
  const content = ref("");
  const endDate = ref("");
  const formVisible = ref(true);

  //FIXME: 改成陳宣瑜的版本，還要加上fetch
  const onfile = (event) => {
    const file = event.target.files[0];
    const fileReader = new FileReader();

    fileReader.readAsDataURL(file);
    fileReader.addEventListener("load", () => {
      const mimeType = file.type;
      const base64Data = fileReader.result.split(",")[1];
      const encodedFile = `data:${mimeType};base64,${base64Data}`; // 添加 MIME 類型前綴

      encodeFile.value = encodedFile;
    });
  };

  const deleteAll = () => {
    formVisible.value = false;

    setTimeout(() => {
      name.value = "";
      price.value = "";
      supplier.value = "";
      file.value = "";
      content.value = "";
      endDate.value = "";

      formVisible.value = true;
    }, 500);
  };

  const handleBeforeLeave = (el) => {
    el.style.opacity = 1;
  };

  const submit = () => {
    console.log(encodeFile);
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
