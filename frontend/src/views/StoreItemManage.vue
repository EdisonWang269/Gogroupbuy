<template>
  <manager-pop
    class="pop"
    :usage="topic"
    :original="endDate"
    :type="type"
    :customerName="customerName"
    @isCanceled="cancel"
    @check="checkAction"
    @isChecked="check"
    v-show="popShow"
  />

  <div class="all">
    <div class="header">
      <div class="info">
        <h1>{{ currItemName }}</h1>
        <span
          >結單日期：{{ endDate }}
          <i class="bi bi-pencil" @click="editDate"></i>
        </span>
      </div>

      <div class="buttons">
        <store-button
          :action="'結單管理 '"
          :icon="'<i class=\'bi bi-pencil\'></i>'"
          @click="endOrder"
        />
        <store-button
          :action="'到貨管理 '"
          :icon="'<i class=\'bi bi-pencil\'></i>'"
          @click="arriveManage"
        />
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
          :action="'增加現場購買顧客'"
          :icon="'<i class=\'bi bi-plus-lg\'></i>'"
          @click="addCustomer"
        />
      </div>

      <div class="notify" @click="notify($event)">
        <i class="bi bi-bell"></i>
        <button class="noti">一鍵通知</button>
      </div>
    </div>

    <item-table @singleNotify="notify($event)" :searchInput="searchInput" />

  </div>
</template>

<script setup>
  import { ref, computed } from "vue";
  import { useStore } from "vuex";
  import StoreButton from "../components/StoreButton.vue";
  import ItemTable from "@/components/ItemTable.vue";
  import ManagerPop from "../components/ManagerPop.vue";
  import { ElMessage } from 'element-plus';

  const store = useStore();

  const searchInput = ref("");

  const topic = ref("");
  const popShow = ref(false);
  const type = ref("");

  const currItemName = computed(
    () => store.state.manager.currItem.product_name
  );
  
  const receive = computed(() => store.state.manager.currItem.statement_date);
  const formatDate = (date) =>{
    const unformattedDate = new Date(date);
    const year = unformattedDate.getFullYear();
    const month = String(unformattedDate.getMonth() + 1).padStart(2, '0'); // 月份从0开始，因此需要+1
    const day = String(unformattedDate.getDate()).padStart(2, '0');

    const formatted = `${year}/${month}/${day}`;
    return formatted;
  }
  const endDate = computed(() => {
      return formatDate(receive.value);
  });
  
  const customerName = computed(() => {
    const names = new Set();
    store.state.manager.orders
      .filter((order) => order.receive_status === "待領取")
      .forEach((order) => names.add(order.user_name));
    return Array.from(names);
  });

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

  const cancel = (value) => {
    popShow.value = value;
  };
  const check = (value) => {
    popShow.value = value;
  };
  const checkAction = async (updated) => {
    if(type.value === "addCus"){
      const response = await fetch(`/api/product/instore_shopping/${store.state.manager.currItem.product_id}`, {
      method: "PUT",
      headers: {
        "Authorization": `Bearer ${store.state.manager.token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        instore_purchase_quantity: parseInt(updated),
      }),
    });
    console.log(response);
    if(!response.success) {
      ElMessage({
        message: '現場存貨數量不足',
        type: 'warning',
    })
    }
    await store.dispatch("manager/fetchOrders");
    } else if(type.value === "endOrder"){
      const response = await fetch(`/api/product/${store.state.manager.currItem.product_id}`, {
      method: "PUT",
      headers: {
        "Authorization": `Bearer ${store.state.manager.token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        cost: updated[0],
        purchase_quantity: updated[1],
      }),
    });
    console.log(updated[0]+ " "+ updated[1]);
    console.log(response);
    } else if (type.value === "arriveManage"){
      const response = await fetch(`/api/product/arrival/${store.state.manager.currItem.product_id}`, {
      method: "PUT",
      headers: {
        "Authorization": `Bearer ${store.state.manager.token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        arrival_date: updated[0],
        due_days: updated[1],
      }),
    });
    console.log(updated[0]+ " "+ updated[1]);
    console.log(response);
    }else if (type.value === "editDate"){
      endDate.value = formatDate(updated);

      const response = await fetch(`/api/product/changedate/${store.state.manager.currItem.product_id}`, {
      method: "PUT",
      headers: {
        "Authorization": `Bearer ${store.state.manager.token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        new_statement_date: updated
      }),
    });
    store.commit("manager/setUpdatedDate", updated);
    console.log(response);
    }
    
  };
  const addCustomer = () => {
    topic.value = "增加現場購買顧客";
    type.value = "addCus";
    showPop();
  };

  const endOrder = () => {
    topic.value = "結單管理";
    type.value = "endOrder";
    showPop();
  };

  const arriveManage = () => {
    topic.value = "到貨管理";
    type.value = "arriveManage";
    showPop();
  };

  const showPop = () => {
    popShow.value = true;
  };
</script>

<style scoped>
  item-table {
    height: 1000px;
  }

  .pop {
    transition: transform;
  }
  .all {
    background-color: #fff;
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
  .info {
    display: flex;
    width: 70%;
    align-items: baseline;
    gap: 30px;
    background: #fff;
  }
  .buttons {
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
  :deep(.el-input__wrapper) {
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

  .table {
    max-height: 55%;
  }

  .table::-webkit-scrollbar {
    width: 0;
    height: 0;
  }
</style>
