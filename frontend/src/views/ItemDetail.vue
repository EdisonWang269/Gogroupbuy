<template>
    <div class="header">
        <i class="bi bi-arrow-left-short"></i>
        <h1>恩恩的團購</h1>
    </div>
    <img src="../assets/cakeItem.png">
    <div class="main">
        <div class="namePart">
            <p class="name">{{ name }}
                <br><span class="price">價格：$ {{ price }} / {{ measure }}</span>
            </p>
        </div>
        <div class="num">
            <p>數量</p>
            <div class="orderPlace">
                <i class="bi bi-dash-square-fill"></i>
                <span>{{ orderNum }}</span>
                <i class="bi bi-plus-square-fill"></i>
            </div>
        </div>
    </div>
    
</template>

<script>
import { ref } from 'vue';
export default {
    setup(){
        const image = "../assets/cakeItem.png";
        const name = ref("香帥芋頭蛋糕");
        const orderNum = ref(1);

        return{
            image,
            name,
            orderNum,
        };
    }

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

img{
    width:95%;
    height: auto;
    /* border: 1px solid gray; */
    display: block;
    margin: 0 auto;
    border-radius: 10px;
}

.main{
    display: flex;
    color: #3C2F2F;

}

.namePart{
    display: block;
    
}
.name{
    font-size: 32px;
    font-weight: bold;
}
.price{
    font-size: 24px;
}

.orderPlace{
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 20%;
    justify-content: center;
    align-content: center;
    font-size: 24px;
}

i{
    color: #EF2A39;
    font-size: 45px;
}

.num{
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}
.num >p {
    font-size: 24px;
}

</style>