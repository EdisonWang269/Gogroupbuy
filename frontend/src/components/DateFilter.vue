<template>
  <div>
    <el-select v-model="value" clearable placeholder="所有日期">
      <el-option
        v-for="item in formattedOptions"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      />
    </el-select>
  </div>
</template>

<script>
  import { ref } from "vue";
  import { computed } from "vue";
  export default {
    props: {
      options: {
        type: Array,
        required: true,
        default: () => [],
      },
    },
    setup(props, { emit }) {
      const value = ref("");
      const chosen = () => {
        emit("filt", value.value);
      };
      const formattedOptions = computed(() => {
        return props.options.map((option) => ({
          label: option,
          value: option,
        }));
      });

      return {
        chosen,
        formattedOptions,
      };
    },
  };
</script>

<style></style>
