<template>
    <manager-pop :usage="topic" :original="endDate" :type="type" :customerName="customerName" @isCanceled="cancel" @check="setEndDate" @isChecked="check" v-show="popShow"/>
    <div class="all">
        <div class="header">
            <h1>顧客訂單管理與查詢</h1> 
        </div>
        <div class="searchBar">
            <el-input
                v-model="searchInput"
                id="search"
                placeholder="搜尋用戶、訂購商品"
            >
                <template #prefix>
                    <i class="bi bi-search"></i>
                </template>
            </el-input>
        </div>

        <manage-table @singleNotify="notify()"/>
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
import {ref} from 'vue';
import ManageTable from '@/components/ManageTable.vue';
import ManagerPop from '../components/ManagerPop.vue';
export default {
    components:{
        ManageTable,
        ManagerPop,

    },
    setup(){
        const topic = ref("");
        const popShow = ref(false);
        const type = ref("");
        const searchInput = ref("");
        const customerName = ref("");
        const notify = (value) =>{
            topic.value = "通知";
            popShow.value = true;
            type.value = "notify";
            customerName.value = value; 
        }
        const cancel = (value) =>{
            popShow.value = value;
        }
        return{
            searchInput,
            notify,
            topic,
            popShow,
            type,
            cancel,
            customerName,

        }

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
    cursor: pointer;
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