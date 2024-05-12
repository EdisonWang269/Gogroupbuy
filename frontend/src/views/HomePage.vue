<template class="all">
    <router-view />   
    <div class="header">
        <h1><i class="bi bi-house" id="homeIcon"></i>恩恩的團購商品</h1>
        <p>歡迎大家加入我的團購</p>
    </div>
    <search-bar @search-query="getValue($event)" v-model="searchQuery"/>
    <div class="items">
        <!-- 已寫好資料和模板綁定，到時將資料庫資料傳到 item 加入 items array 即可顯示 -->
        <item-card v-for="item in items" :key="item.ID" :img="item.img" :name="item.name" :price="item.price" :measure="item.measure" :endDate="item.endDate" class="card"/>
    </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import SearchBar from '../components/SearchBar.vue';
import ItemCard from '../components/ItemCard.vue';
export default {
    components:{
        ItemCard,
        SearchBar,
    },
    setup(){
        const router = useRouter();
        const currentID = ref(0);
        
        // 一個商品的物件
        const item = {
            img: require("../assets/cakeItem.png"),
            ID: currentID.value++,
            name: "",
            price: 240,
            measure: "",
            endDate: "",
        };

        // 儲存所有商品的 array 
        const items = ref([]);

        // 使用者輸入的搜尋字串
        const searchQuery = ref("");

        const getValue = (value) => {
            searchQuery.value = value;
        };
        // 測試 v-model 綁定正確
        const check = () => {
            console.log(searchQuery.value);
        };

        const checkDetail = (itemID) => {
            router.push(`/home/item/${itemID}`);
        };

        return{
            item,
            items,
            searchQuery,
            check,
            getValue,
            checkDetail,

        };
    }
}
</script>

<style>
.all{
    position: relative;
}
.header{
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin: 48px 0 0 20px;
}

h1{
    font-weight: 800;
}

#homeIcon{
 margin-right: 12px;   
 color:#EF2A39;
}

p{
    margin-top: 10px;
    font-size: 18px;
    color: #6A6A6A;
}

.items{
    position: relative;
    left: 6px;
    margin: 10% 10px;
    padding: 0 0 5% 0;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-row-gap: 16px;
    max-height: 63%;
    overflow: scroll;

}

.items::-webkit-scrollbar{
    
    width: 0;
    height: 0;
}

.card{
    cursor: pointer;
}




</style>