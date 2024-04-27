<template>
    <div class="header">
        <router-link to="/home"><i class="bi bi-arrow-left-short"></i></router-link>
        <h1>恩恩的團購</h1>
    </div>
    <h2>訂單完成<i class="bi bi-check-lg"></i></h2>
    <div class="info">
        你已成功訂購
        <br>商品：「{{ name }}」
        <br>數量：「{{ num }}」
        <br><span id="sml">*領取時間與資訊請待團購主通知</span>
    </div>
</template>

<script>
export default {
    props:[ 'name', 'num' ],

}
</script>

<style scoped>
i {
    font-size: 28px;
    font-weight: 700;
}

h1{
    font-weight: 700;
    display: inline-block;
    text-align: center;
    position: relative;
    margin: 0 auto;
}

.header{
    display: flex;
    padding: 20px 12px 0 12px;
    justify-content: flex-start;
    align-items: center;
}
h2{
    color: #EF2A39;
    font-weight: 700;
    text-align: center;
}

.info{
    font-size: 24px;
    color: #6A6A6A;
}
#sml{
    font-size: 20px;
}

</style>