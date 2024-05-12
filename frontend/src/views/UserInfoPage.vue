<template>
  <h1>
    <i class="bi bi-person"></i>
    個人資訊
  </h1>
  <img src="../assets/logo.png">
  <div>
    <div class="infoBar">
        <span>姓名</span>
        <p>{{ user.name }}</p>
    </div>
    <div class="infoBar">
        <span>手機</span>
        <p>{{ user.phoneNum }}</p>
    </div>
    <div class="infoBar">
        <span>會員等級</span>
        <p>{{ user.status }}</p>
    </div>
  </div>
</template>

<script>
export default {
    setup(){
        const user = {
            name: "陳以恩",
            phoneNum: "0922-111-333",
            status: "一般會員",
        }
        
        return{
            user,
        };
    }

}
</script>

<style scoped>

</style>