<template>
    <manager-pop :usage="topic" :original="endDate" :type="type" @isCanceled="cancel" @check="setEndDate" @isChecked="check" v-show="popShow"/>
    <div class="all">
        <div class="header">
            <h1>{{ itemName }}</h1> <!-- 從 vuex 抓商品資訊 -->
            <span>上架日期：{{ uploadDate }}</span>
            <span>結單日期：{{ endDate }}   <i class="bi bi-pencil" @click="editDate"></i></span>
        </div>
        <div class="searchBar">
            <el-input
                v-model="input4"
                id="search"
                placeholder="搜尋用戶"
            >
                <template #prefix>
                    <i class="bi bi-search"></i>
                </template>
            </el-input>
        </div>
        <div class="buttonList">
            <div class="function">
                <store-button :action="'增加現場購買顧客  '" :icon="'<i class=\'bi bi-plus-lg\'></i>'"/>
                <!-- <date-filter :opstions = "orderDates"/> -->
            </div>
            <div class="notify">
                <i class="bi bi-bell"></i>
                <button class="noti">一鍵通知</button>
            </div>
        </div>
        <manage-table />
        <div class="pages">
            <nav aria-label="Page navigation example">
                <ul class="pagination">
                    <li class="page-item">
                        <a class="page-link" href="#" aria-label="Previous">
                            <span aria-hidden="true">&laquo;</span>
                        </a>
                    </li>
                    <li class="page-item"><a class="page-link" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item">
                        <a class="page-link" href="#" aria-label="Next">
                            <span aria-hidden="true">&raquo;</span>
                        </a>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';
// import { TableColumnCtx, TableInstance } from 'element-plus';
// import { computed } from 'vue';
import StoreButton from '../components/StoreButton.vue';
import ManageTable from '@/components/ManageTable.vue';
import ManagerPop from '../components/ManagerPop.vue';

export default {
    components:{
        StoreButton,
        ManageTable,
        ManagerPop,
        // DateFilter,
    },

    setup(){
        const itemName = ref("香帥芋泥蛋糕");
        const uploadDate = ref("2024/05/09");
        const endDate = ref("2024/05/15");
        const topic = ref("");
        const popShow = ref(false);
        const type = ref("");
        const editDate = () =>{
            topic.value = "更改結單日期"
            popShow.value = true;
            type.value = "editDate";
        }
        const cancel = (value) =>{
            popShow.value = value;
        }
        const check = (value) =>{
            popShow.value = value;
        }
        const setEndDate = (date) =>{
            console.log(date);
            if(date != ""){
                endDate.value = date;
            }
            
        }
        
        return{
            itemName,
            uploadDate,
            endDate,
            editDate,
            topic,
            popShow,
            check,
            type,
            cancel,
            setEndDate,
        };
    }
}
</script>

<style scoped>
.all{
    background-color: #FAFAFA;
    width: 100%;
    height: 100%;
     
}
.header{
    display: flex;
    gap: 30px;
    align-items: baseline;
}
.bi.bi-pencil{
    color: #5C73DB;
    cursor: pointer;
}
h1{
    font-weight: 700;
    font-size:32px;
    margin-left: 5%;
    padding-top: 20px;
}
.searchBar{
    border-radius: 10px;
    width: 90%;
    text-align: center;
    margin: 0 auto;
}
#search{
    margin: 0 auto;
    padding: 16px 0;
}

i{
    color: black;
}
::v-deep .el-input__wrapper{
    padding: 8px 16px;
    border-radius: 10px;
    border: 1px solid #4763E4;
}
.noti{
    padding: 8px 11px;
    border: none;
    background-color: #DC2626;
    border-radius: 10px;
    font-size: 12px;
    color: white;
}
.bi.bi-bell{
    font-size: 20px;
}
.buttonList{
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    width: 85%;
    margin-left: 5%;
    margin-top: 16px;
}
.function{
    display: flex;
    gap: 40px;
}
.notify{
    display: flex;
    height: fit-content;
    gap:10px;
}

.pages{
    display: flex;
    width: 100%;
    /* position: absolute; */
    justify-content: center;
    /* margin: 0 auto; */
    position: absolute;
    bottom: 0;
}
</style>