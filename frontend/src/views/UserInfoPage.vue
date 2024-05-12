<template>
  <h1>
    <i class="bi bi-person"></i>
    個人資訊
  </h1>
  <img :src="user.userImg">
  <div class="wrap">
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
import { ref } from 'vue';
export default {
    setup(){
        const user = ref({
            userImg: require("../assets/user.jpg"),
            name: "陳以恩",
            phoneNum: "0922-111-333",
            status: "一般會員",
        });
        
        return{
            user,
        };
    }

}
</script>

<style scoped>
i{
    color: #EF2A39;
}
h1{
    /* position: relative; */
    margin-left: 5%;
    margin-top: 48px;
}
img{
    /* position: relative; */
    display: block;
    height: 115px;
    width: auto;
    border-radius: 35px;
    margin: 60px auto;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
}
.infoBar{
    display: flex;
    flex-direction: column;
    gap: 6px;
}
.infoBar span{
    font-size: 15px;
    color:#A9A9A9;
}

.infoBar p{
    border: 1px solid #EEEEEE;
    border-radius: 10px;
    padding: 22px 16px;
    font-size: 16px;
}
.wrap{
    display: flex;
    flex-direction: column;
    gap: 30px;
    width: 80%;
    margin: 0 auto;
}

</style>