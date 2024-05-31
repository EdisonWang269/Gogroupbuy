<template>
  <div class="table">
    <el-table :data="tableData" height="250" style="width: 100%">
      <el-table-column prop="name" label="顧客姓名" />
      <el-table-column prop="orderNum" label="數量" />
      <el-table-column
        prop="dueDate"
        label="領取期限"
        :filter-method="filterHandler"
        :filters="dateFilters"
      />
      <el-table-column prop="phoneNum" label="手機號碼" />
      <el-table-column prop="status" label="訂單狀況">
        <template #default="scope">
          <el-tag :type="setType(scope.row.status)" effect="light" round>
            {{ setLabel(scope.row.status) }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="checked" label="完成度">
        <template #default="scope">
          <div class="checkBox">
            <el-checkbox
              v-model="scope.row.checked"
              size="large"
              @change="handleChange(scope.row)"
            />
            <!-- <el-button
              type="danger"
              round
              size="small"
              v-if="!scope.row.checked"
              @click="singleNotify(scope.row.name)"
              >通知</el-button
            > -->
          </div>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  import { ref } from "vue";
  // import { TableColumnCtx, TableInstance } from 'element-plus';
  import { computed } from "vue";

  export default {
    components: {},

    setup(props, { emit }) {
      const filterDates = ref([]);
      const singleNotify = (name) => {
        emit("singleNotify", name);
      };
      const tableData = ref([
        {
          name: "Tom",
          orderNum: 1,
          dueDate: "2019/05/20",
          phoneNum: "0912330330",
          status: true,
          checked: true,
        },
        {
          name: "Alex",
          orderNum: 1,
          dueDate: "2019/05/20",
          phoneNum: "0912330330",
          status: false,
          checked: false,
        },
        {
          name: "Tom",
          orderNum: 1,
          dueDate: "2019/07/20",
          phoneNum: "0912330330",
          status: true,
          checked: true,
        },
      ]);

      const setType = (value) => {
        if (value) {
          return "success";
        } else {
          return "danger";
        }
      };
      const setLabel = (value) => {
        if (value) {
          return "已領取";
        } else {
          return "未領取";
        }
      };
      const handleChange = (row) => {
        row.status = row.checked;
      };
      const filterHandler = (value, row, column) => {
        const property = column.property;
        return row[property] === value;
      };
      const dates = computed(() => {
        const uniqueDates = [
          ...new Set(tableData.value.map((item) => item.dueDate)),
        ];
        return uniqueDates;
      });
      const dateFilters = computed(() => {
        return dates.value.map((date) => ({
          text: date,
          value: date,
        }));
      });
      const addItem = () => {};

      return {
        // Search
        tableData,
        setType,
        setLabel,
        handleChange,
        filterHandler,
        dates,
        filterDates,
        dateFilters,
        singleNotify,
        addItem,
      };
    },
  };
</script>

<style scoped>
  .table {
    width: 90%;
    margin: 0 auto;
    margin-top: 3%;
  }
  .checkBox {
    display: flex;
    align-items: center;
    gap: 20px;
  }
  /* ::v-deep .el-table__header-wrapper, .el-table__body-wrapper, .el-table__row, .cell{
    background-color: #FAFAFA;
} */
  ::v-deep .el-tag.el-tag--danger.el-tag--light.is-round {
    background-color: #fee2e2;
  }
  ::v-deep .el-tag.el-tag--danger.el-tag--light.is-round > .el-tag__content {
    color: #991b1b;
    font-size: 12px;
  }
  ::v-deep .el-tag.el-tag--success.el-tag--light.is-round {
    background-color: #dcfce7;
  }
  ::v-deep .el-tag.el-tag--success.el-tag--light.is-round > .el-tag__content {
    color: #03543f;
    font-size: 12px;
  }
  ::v-deep .el-button.el-button--danger.el-button--small.is-round {
    background-color: #dc2626;
  }
  ::v-deep .el-checkbox__input.is-checked > .el-checkbox__inner {
    background-color: #4318ff;
    border-color: #4318ff;
  }
</style>
