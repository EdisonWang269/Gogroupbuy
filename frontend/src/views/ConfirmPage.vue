<template>
    <div class="header">
        <!-- <router-link to="/"><i class="bi bi-arrow-left-short"></i></router-link> -->
        <h1>恩恩的團購</h1>
    </div>
    <h2>訂單完成<i class="bi bi-check-lg"></i></h2>
    <div class="info">
        你已成功訂購  <!-- 這裡應該要用到 vuex 了因為他跟其他網頁沒有母子關係 -->
        <br>商品：「{{ name }}」
        <br>數量：「{{ num }}」
        <br><span id="sml">*領取時間與資訊請待團購主通知</span>
    </div>
    <big-button :action="action" @click="backToHome" class="back"/>
    <div class="otherItem">
        <item-card v-for="item in items" :key="item.ID" :name="item.name" :price="item.price" :measure="item.measure" :endDate="item.endDate" class="card"/>
    </div>
</template>

<script>
import ItemCard from '@/components/ItemCard.vue';
import { useRouter } from 'vue-router';
import BigButton from '@/components/BigButton.vue';
import { ref } from 'vue';
export default {
    components:{
        ItemCard,
        BigButton,
    },
    props:[ 'name', 'num' ],
    setup(){
        const action = "回到賣場";
        const router = useRouter();
        const backToHome = () => {
            router.push({name: 'homePage'});
        }

        const currentID = ref(0);
        
        // 一個商品的物件
        const item = {
            img: "",
            ID: currentID.value++,
            name: "",
            price: 240,
            measure: "",
            endDate: "",
        };

        // 儲存所有商品的 array 
        const items = ref([]);

        return{
            action,
            backToHome,
            item,
            items,
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
h2{
    color: #EF2A39;
    font-weight: 700;
    text-align: center;
}

.info{
    font-size: 24px;
    color: #6A6A6A;
    margin-left: 8%;
    line-height:1.7;
    margin-top: 10px;
}
#sml{
    font-size: 20px;
}

.back{
    margin-top: 12px;
}
.otherItem{
    position: relative;
    /* left: 6px; */
    margin: 10% 0;
    padding: 0 0 5% 0;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-row-gap: 16px;
    background-color: #F3F3F3;
    border-radius:20px;
    height: 55%;
    margin-top: 25px;
    overflow: scroll;

}

.items::-webkit-scrollbar{
    width: 0;
    height: 0;
}

</style>