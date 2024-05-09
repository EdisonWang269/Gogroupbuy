<template>
    <div class="header">
        <router-link to="/home"><i class="bi bi-arrow-left-short"></i></router-link>
        <h1>恩恩的團購</h1>
    </div>
    <img src="../assets/cakeItem.png"> 
    <div class="main">
        <div class="namePart">
            <p class="name">{{ item.name }}
                <br><span class="price">價格：$ {{ item.price }} / {{ item.measure }}</span>
            </p>
        </div>
        <div class="num">
            <p>數量</p>
            <div class="orderPlace">
                <i class="bi bi-dash-square-fill" @click="minOrder"></i>
                <span>{{ orderNum }}</span>
                <i class="bi bi-plus-square-fill" @click="addOrder"></i>
            </div>
        </div>
    </div>
    <big-button :action="buttonAct" @click="order"/>
    <div class="content">
        <span>結單日期：{{ item.endDate }}</span>
        <span>商品說明：</span>
        <span id="content">{{ item.content }}</span>
    </div>
    <confirm-pop v-if="ordercheck" class="pop" :name="item.name" :orderNum="orderNum" @isCancelled="cancel"></confirm-pop>
</template>

<script>
import { ref } from 'vue';
import BigButton from '../components/BigButton.vue';
import ConfirmPop from '@/components/ConfirmPop.vue';
export default {
    components:{
        BigButton,
        ConfirmPop,
    },  
    setup(){
        const buttonAct = "立即下單";
        const orderNum = ref(1);
        const item = { //這裡要插值
            name: "香帥芋頭蛋糕",
            img: "../assets/cakeItem.png",
            price: 240,
            endDate: "2024/05/20",
            measure: "條",
            content: "★香純原味 嚴選台灣在地食材香氣較濃的品種~檳榔心芋頭 ★口感紮實 軟綿Q彈蛋糕體，純淨天然的芋頭香氣一口接著一口永難忘懷 ★堅持品質 堅持不添加任何防腐劑與人工色素",
        };
        const addOrder = () => {
            orderNum.value ++;
        };
        const minOrder = () => {
            orderNum.value --;
            if(orderNum.value < 0){
                orderNum.value = 0;
            }
        };

        const ordercheck = ref(false);
        const order = () => {
            if(orderNum.value > 0){
                ordercheck.value = true;
            }
        };

        const cancel = (value) => {
            if(value == true){
                ordercheck.value = false;
            }
        };

        return{
            orderNum,
            item,
            addOrder,
            minOrder,
            buttonAct,
            ordercheck,
            order,
            cancel,
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
    width:88%;
    height: auto;
    /* border: 1px solid gray; */
    display: block;
    margin: 0 auto;
    border-radius: 10px;
}

.main{
    display: flex;
    color: #3C2F2F;
    gap:5%;
    padding: 5px 5% 0 5%;
    margin: 0 auto;

}

.namePart{
    display: block;
    margin-bottom: 0;
    
}
.name{
    font-size: 32px;
    font-weight: bold;
}
.price{
    font-size: 24px;
    vertical-align: baseline;
}

.orderPlace{
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 20%;
    padding-left: 10px;
    /* padding-bottom: 40px; */
    justify-content: center;
    align-items: center;
    font-size: 24px;
}

i{
    color: #EF2A39;
    font-size: 45px;
    cursor: pointer;
}

.num{
    position: relative;
    display: flex;
    gap: 0;
    flex-direction: column;
    justify-content: flex-start;
    align-items: baseline;
}
.num >p {
    font-size: 24px;
    padding: 0;
    margin-bottom: 0;
}

/* button{
    background-color:#3C2F2F;
    border: none;
    border-radius: 20px;
    box-shadow: 3px 3px 8px 3px rgba(0, 0, 0, 0.2);
    display: block;
    width: 90%;
    font-size: 32px;
    font-weight: 700;
    color: white;
    margin: 0 auto;
    padding: 10px 0;
} */
.content{
    margin-top: 5px;
    display: flex;
    flex-direction: column;
    gap: 7px;
    font-size:24px;
    padding: 5px 5%;
    color: #3C2F2F;
}

#content{
    font-size: 16px;
    color: #6A6A6A;
}

.pop{
    position:absolute;
    top: 0;
    left: 0;
}

</style>