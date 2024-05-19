<template>
  <div class="all">
    <div class="card">
      <h1>訂單確認</h1>
      <div class="content">
        <span>您將訂購</span>
        <br><span>「{{ name }}」</span>
        <br><span>數量：「{{ orderNum }}」</span>
      </div>
      <div class="buttonArea">
        <button id="cancel" @click="cancel">取消</button>
        <button id="confirm" @click="confirm">確認</button>
      </div>
    </div>
  </div>
  
</template>

<script>
// import { useRouter } from 'vue-router';
export default {
  props:[ 'name', 'orderNum' ],
  setup( props, { emit }){
    // const router = useRouter();
    const cancel = () => {
      emit('isCancelled', true);
    };

    const confirm = () =>{
      emit('confirmed', true);
      // router.push('/home/item/confirm');
    }

    return{
      cancel,
      confirm,
    };
  }

}
</script>

<style scoped>
.all{
  background-color: rgba(0, 0, 0, 0.5);
  width: 100%;
  height: 100%;
  /* border-radius: 35px; */
}

.card{
  
  display: flex;
  flex-direction: column;
  /* gap: 24px; */
  justify-content: space-around;;
  padding: auto, 0;
  margin: auto auto;
  top: 35%;
  border-radius: 20px;
  width: 70%;
  height: 32%;
}
h1{
  position: inherit;
  margin: 0 auto;
  margin-top: 10%;
  color: #3C2F2F;
  font-weight: 700;
  font-size: 32px;
}
.content{
  font-size: 16px;
  
  /* display: flexbox; */
  text-align: center;
  color: #6A6A6A;
}
.buttonArea{
  text-align: center;
  margin-bottom: 10%;
}
button{
  border: none;
  border-radius: 12px;
  font-size: 16px;
  color: white;
  width: 38%;
  height: 48px;
}



#cancel{
  background-color: #3C2F2F;
}

#confirm{
  background-color: #EF2A39;
  margin-left: 14px;
}

</style>