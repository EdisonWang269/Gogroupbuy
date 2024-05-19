<template>
  <div class="overlay">
    <div class="card">
        <p>{{ usage }}</p>
        <div class="buttons">
            <store-button :action="'確認'"/>
            <el-button>取消</el-button>
        </div>
    </div>
  </div>
</template>

<script>
import StoreButton from './StoreButton.vue';
export default {
    props:['usage'],
    components:{
        StoreButton,
    }
}
</script>

<style scoped>
.overlay {
    width: 100vw;
    height: 100vh;
    position: fixed;
    background-color: rgba(0, 0, 0, 0.6);
    z-index: 5;
}
.card{
    padding:32px;
    width: 90%;
    height: 435px;
    background-color: white;
    border-radius: 12px;
}
.buttons{
    display: flex;
    gap:8px;
}

</style>