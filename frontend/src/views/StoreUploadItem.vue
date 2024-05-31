<template>
  <div class="all">
    <div class="header">
      <h1>上架商品</h1>
    </div>
    <div class="uploadArea">
      <div>
        <span>商品名稱</span>
        <el-input class="input"></el-input>
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
        <span>商品價格（寫法： 250/個）</span>
        <el-input class="input"></el-input>
      </div>
      <div>
        <span>結單日期</span>
        <el-input class="input">
          <template #prefix>
            <i class="bi bi-calendar3"></i>
          </template>
        </el-input>
      </div>
      <div>
        <span>商品說明</span>
        <textarea></textarea>
      </div>
    </div>
  </div>
</template>

<script>
  export default {};
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
  /* .uploadArea div{
    display: block;
} */
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
</style>
