<template>
  <manager-pop
    :usage="topic"
    :original="endDate"
    :type="type"
    :customerName="customerName"
    @isCanceled="cancel"
    @check="setEndDate"
    @isChecked="check"
    v-show="popShow"
  />
  <div class="all">
    <div class="header">
      <div class="info">
        <h1>{{ itemName }}</h1>
        <!-- 從 vuex 抓商品資訊 -->
        <span>上架日期：{{ uploadDate }}</span>
        <span>結單日期：{{ endDate }} <i class="bi bi-pencil" @click="editDate"></i></span>
      </div>
      
      <div class="buttons">
        <store-button :action="'結單管理 '" :icon="'<i class=\'bi bi-pencil\'></i>'" @click="endOrder"/>
        <store-button :action="'到貨管理 '" :icon="'<i class=\'bi bi-pencil\'></i>'" @click="arriveManage"/>
      </div>
      
    </div>
    <div class="searchBar">
      <el-input v-model="searchInput" id="search" placeholder="搜尋用戶">
        <template #prefix>
          <i class="bi bi-search"></i>
        </template>
      </el-input>
    </div>
    <div class="buttonList">
      <div class="function">
        <store-button
          :action="'增加現場購買顧客  '"
          :icon="'<i class=\'bi bi-plus-lg\'></i>'"
          @click="addCustomer"
        />
        <!-- <date-filter :opstions = "orderDates"/> -->
      </div>
      <div class="notify" @click="notify($event)">
        <i class="bi bi-bell"></i>
        <button class="noti">一鍵通知</button>
      </div>
    </div>
    <item-table @singleNotify="notify($event)" />
    <div class="num">
      <span>已領取： {{ checkedNum }}</span>
      <span>未領取： {{ uncheckedNum }}</span>
    </div>
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
  import { ref } from "vue";
  // import { TableColumnCtx, TableInstance } from 'element-plus';
  // import { computed } from 'vue';
  import StoreButton from "../components/StoreButton.vue";
  import ItemTable from "@/components/ItemTable.vue";
  import ManagerPop from "../components/ManagerPop.vue";

  export default {
    components: {
      StoreButton,
      ItemTable, // 可以也可以在這裡綁資料庫的訂單資料
      ManagerPop,
      // DateFilter,
    },

    setup() {
      const itemName = ref("香帥芋泥蛋糕");
      const uploadDate = ref("2024/05/09");
      const endDate = ref("2024/05/15");
      const searchInput = ref("");
      const topic = ref("");
      const popShow = ref(false);
      const type = ref("");
      const customerName = ref("Tom,Alex,Sammy"); //要通知的顧客名字
      const checkedNum = ref(0);
      const uncheckedNum = ref(0);
      const editDate = () => {
        topic.value = "更改結單日期";
        popShow.value = true;
        type.value = "editDate";
      };
      const notify = (value) => {
        if (typeof value === "string") {
          topic.value = "通知";
          popShow.value = true;
          type.value = "notify";
          customerName.value = value;
        } else {
          topic.value = "通知所有未領取顧客";
          popShow.value = true;
          type.value = "notify";
        }
      };
      // const notifyCustomerName = () =>{

      // }
      const cancel = (value) => {
        popShow.value = value;
      };
      const check = (value) => {
        popShow.value = value;
      };
      const setEndDate = (date) => {
        console.log(date);
        if (date != "") {
          endDate.value = date;
        }
      };
      const addCustomer = () => {
        topic.value = "增加現場購買顧客";
        type.value = "addCus";
        showPop();
      };

      const endOrder = () =>{
        topic.value = "結單管理";
        type.value = "endOrder";
        showPop();
      }

      const arriveManage = () =>{
        topic.value = "到貨管理";
        type.value = "arriveManage";
        showPop();
      }

      const showPop = () =>{
        popShow.value = true;
      }

      return {
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
        notify,
        customerName,
        searchInput,
        addCustomer,
        checkedNum,
        uncheckedNum,
        endOrder,
        arriveManage,
      };
    },
  };
</script>

<style scoped>
  .all {
    background-color: #fafafa;
    width: 100%;
    height: 100%;
  }
  .header {
    margin: 0 5%;
    display: flex;
    /* gap: 30px; */
    align-items: baseline;
    justify-content: space-between;
  }
  .info{
    display: flex;
    width:60%;
    align-items: baseline;
    gap:30px;
  }
  .buttons{
    display: flex;
    padding-bottom: 10px;
    gap: 10px;
  }
  .bi.bi-pencil {
    color: #5c73db;
    cursor: pointer;
  }
  h1 {
    font-weight: 700;
    font-size: 32px;
    /* margin-left: 5%; */
    padding-top: 20px;
  }
  .searchBar {
    border-radius: 10px;
    width: 90%;
    text-align: center;
    margin: 0 auto;
  }
  #search {
    margin: 0 auto;
    padding: 16px 0;
  }

  i {
    color: black;
  }
  ::v-deep .el-input__wrapper {
    padding: 8px 16px;
    border-radius: 10px;
    border: 1px solid #4763e4;
  }
  .noti {
    padding: 8px 11px;
    border: none;
    background-color: #dc2626;
    border-radius: 10px;
    font-size: 12px;
    color: white;
  }
  .bi.bi-bell {
    cursor: pointer;
    font-size: 20px;
  }
  .buttonList {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    width: 85%;
    margin-left: 5%;
    margin-top: 16px;
  }
  .function {
    display: flex;
    gap: 40px;
  }
  .notify {
    display: flex;
    height: fit-content;
    gap: 10px;
  }

  .pages {
    display: flex;
    width: 100%;
    /* position: absolute; */
    justify-content: center;
    /* margin: 0 auto; */
    position: absolute;
    bottom: 0;
  }
  .num {
    color: #a1a1aa;
    margin-top: 20px;
    display: flex;
    gap: 50px;
    width: 100%;
    justify-content: center;
  }
</style>
