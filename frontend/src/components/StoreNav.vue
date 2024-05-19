<template>
    <div class="all">
        <nav style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><router-link to="/manager">{{ action }}</router-link></li>  <!-- 從 vuex 抓sidebar value -->
                <li class="breadcrumb-item active" aria-current="page">{{ item }}</li>  <!-- 從 vuex 抓商品名稱 -->
            </ol>
        </nav>
    </div>
  
</template>

<script>
export default {
    props:['action','item'],
}
</script>

<style scoped>
.all{
    width: 100%;
    vertical-align: center;
    align-items: center;
    justify-items: center;
    /* height: 80px; */
    padding-left: 40px;
    background-color: #fff;
}

</style>