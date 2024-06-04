<template>
  <div class="table">
    <el-table :data="sortedTableData" height="650px" style="width: 100%">
      <el-table-column prop="user_name" label="顧客姓名" />
      <el-table-column prop="product_name" label="訂購商品" sortable />
      <el-table-column prop="quantity" label="數量" />
      <el-table-column prop="due_date" label="領取期限" sortable />
      <el-table-column prop="phone" label="手機號碼" />
      <el-table-column
        prop="receive_status"
        label="訂單狀況"
        sortable
        :sort-method="customSort"
      >
        <template #default="scope">
          <el-tag
            round
            effect="light"
            :type="setType(scope.row.receive_status)"
          >
            {{ scope.row.receive_status }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="receive_status" label="完成度">
        <template #default="scope">
          <div class="checkBox">
            <el-checkbox
              :checked="scope.row.receive_status === '已領取'"
              size="large"
              @change="handleCheckboxChange(scope.row, scope.$index)"
            />
          </div>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
  import { computed } from "vue";
  import { useStore } from "vuex";

  const store = useStore();
  const tableData = computed(() => store.state.manager.orders);

  const sortedTableData = computed(() => {
    return [...tableData.value].sort(customSort);
  });

  const setType = (receive_status) => {
    return receive_status === "已領取" ? "success" : "danger";
  };

  const handleCheckboxChange = (row, index) => {
    const newStatus = row.receive_status === "已領取" ? "待領取" : "已領取";
    store.commit("manager/setOrderStatus", { index, status: newStatus });
    store.commit("manager/setCheckedNum");
    store.commit("manager/setUncheckedNum");

    const sortedData = [...tableData.value].sort(customSort);
    store.commit("manager/setOrders", sortedData);
  };

  const customSort = (a, b) => {
    // 比較完成度
    if (a.receive_status === "待領取" && b.receive_status === "已領取") {
      return -1;
    } else if (a.receive_status === "已領取" && b.receive_status === "待領取") {
      return 1;
    }
    // 比較領取期限
    const dateA = new Date(a.due_date);
    const dateB = new Date(b.due_date);
    if (dateA < dateB) {
      return -1;
    } else if (dateA > dateB) {
      return 1;
    }
  };
</script>

<style scoped>
  .table {
    width: 90%;
    margin: 0 auto;
    margin-top: 48px;
  }
  .checkBox {
    display: flex;
    align-items: center;
    gap: 20px;
  }
  :deep(.el-tag.el-tag--danger.el-tag--light.is-round) {
    background-color: #fee2e2;
  }
  :deep(.el-tag.el-tag--danger.el-tag--light.is-round > .el-tag__content) {
    color: #991b1b;
    font-size: 12px;
  }
  :deep(.el-tag.el-tag--success.el-tag--light.is-round) {
    background-color: #dcfce7;
  }
  :deep(.el-tag.el-tag--success.el-tag--light.is-round > .el-tag__content) {
    color: #03543f;
    font-size: 12px;
  }
  :deep(.el-checkbox__input.is-checked > .el-checkbox__inner) {
    background-color: #4318ff;
    border-color: #4318ff;
  }
</style>
