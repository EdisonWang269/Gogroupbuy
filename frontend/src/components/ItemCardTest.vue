<template>
    <div class="card">
    <img src="../assets/cakeItem.png" class="card-img-top" alt="...">
    <div class="card-body">
      <p class="card-title">{{ name }}</p>
      <p class="card-text">$ {{ price }} / {{ measure }}
          <br>結單日期：{{ endDate }}
      </p>
    </div>
  </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  export default {
      
      setup(){
          
          const price = ref(240);
          const measure = ref("條");
          const name = ref("香帥芋頭蛋糕");
          const endDate = ref("2024/05/20");
  
  
          return{
              price,
              measure,
              name,
              endDate,
          };
      }
  }
  </script>
  
  <style scoped>
  .card{
      margin: 3px;
      width: 185px;
      /* height: 240px; */
      border-radius: 20px;
      border: none;
      box-shadow: 3px 2px 8px 0px rgba(180, 180, 180, 0.5)
  }
  
  .card-img-top{
      margin: 5% auto -3%;
      width: 90%;
      height: auto;
      border-radius: 10px;
  }
  
  .card-body{
      margin: 0 auto;
      padding: 0px;
  }
  
  .card-title{
      text-align: center;
      font-size: 20px;
      color: #AC503C;
  }
  
  .card-text{
      margin-top: -18px;
      padding: 10px 5px;
      text-align: center;
      font-size: 14px;
  }
  
  </style>