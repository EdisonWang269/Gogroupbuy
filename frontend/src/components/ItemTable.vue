<template>
  <div class="table">
    <el-table
      :data="filteredTableData"
      height="550"
      style="width: 100%"
      ref="dataTable"
    >
      <el-table-column prop="user_name" label="顧客姓名" />

      <el-table-column prop="quantity" label="數量" />

      <el-table-column prop="due_date" label="領取期限" />

      <el-table-column prop="phone" label="手機號碼" />

      <el-table-column prop="receive_status" label="訂單狀況">
        <template #default="scope">
          <el-tag
            :type="setType(scope.row.receive_status)"
            effect="light"
            round
          >
            {{ scope.row.receive_status }}
          </el-tag>
        </template>
      </el-table-column>

      //FIXME: 切換商品時checkbox狀態不會被更新
      <el-table-column prop="receive_status" label="完成度">
        <template #default="scope">
          <div class="checkBox">
            <el-checkbox
              :checked="scope.row.receive_status === '已領取' ? true : false"
              size="large"
              @change="handleCheckboxChange(scope.row, scope.row.order_id)"
            />
          </div>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
  import { computed, defineProps } from "vue";
  import { useStore } from "vuex";

  const store = useStore();
  const props = defineProps({
    searchInput: String,
  });

  const tableData = computed(() => store.state.manager.orders);

  const filteredTableData = computed(() => {
    const keyword = props.searchInput.toLowerCase();
    if (!keyword) {
      return tableData.value.filter((order) => {
        return order.product_name === store.state.manager.currItem.product_name;
      });
    } else {
      return tableData.value.filter((item) => {
        return (
          item.user_name.toLowerCase().includes(keyword) &&
          item.product_name === store.state.manager.currItem.product_name
        );
      });
    }
  });

  const setType = (receive_status) => {
    if (receive_status === "已領取") {
      return "success";
    } else {
      return "danger";
    }
  };

  const handleCheckboxChange = (row, order_id) => {
    const newStatus = row.receive_status === "已領取" ? "待領取" : "已領取";
    store.commit("manager/setOrderStatus", { order_id, status: newStatus });
    store.commit("manager/setCheckedNum");
    store.commit("manager/setUncheckedNum");
  };
</script>

<style scoped>
  .table {
    width: 90%;
    margin: 0 auto;
    margin-top: 3%;
    overflow-x: hidden;
  }
  :deep(.el-scrollbar__bar.is-horizontal) {
    height: 0 !important;
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
  :deep(.el-button.el-button--danger.el-button--small.is-round) {
    background-color: #dc2626;
  }
  :deep(.el-checkbox__input.is-checked > .el-checkbox__inner) {
    background-color: #4318ff;
    border-color: #4318ff;
  }
</style>
