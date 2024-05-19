<template>
  <div class="overlay">
    <div class="card">
        <h4>{{ usage }}</h4>
        <div class="editDate" v-if="type==='editDate'">
            <div>
                <span>原來結單日期</span>
                <el-input :value="original" style="width: 500px" disabled/>
            </div>
            <div>
                <span>更新結單日期</span>
                <el-input v-model="updated" style="width: 500px" placeholder="Please input" />
                <span id="alert" v-show="alertShow">請輸入新的結單日期</span>
            </div>
            
        </div>
        <div class="buttons">
            <store-button :action="'確認'" class="button" @click="check"/>
            <button class="buttonCancel" @click="cancel">取消</button>
        </div>
    </div>
  </div>
</template>

<script>
import {ref} from 'vue';
import StoreButton from './StoreButton.vue';
export default {
    props:['usage','original','type'],
    components:{
        StoreButton,
    },
    setup(props,{emit}){
        const updated = ref("");
        const alertShow = ref(false);
        const alert = () =>{
            if(updated.value == ""){
                alertShow.value = true;
            }
            else{
                alertShow.value = false;
            }
        }
        const cancel = () =>{
            emit('isCanceled', false);
        }
        const check = () =>{
            alert();
            if(!alertShow.value){
                emit('isChecked', false);
                if(props.type === "editDate"){
                    console.log(props.type);
                    emit('check', updated.value);
                    updated.value = "";
                }
            }
            else{
                emit('check', false);
            }
        }
        return{
            updated,
            cancel,
            check,
            alertShow,
        }
    }
}
</script>

<style scoped>
.overlay {
    position: absolute;
    left:0;
    top:0;
    display:flex;
    justify-content:center;
    align-items:center;
    width: 100vw;
    height: 100vh;
    position: fixed;
    background-color: rgba(0, 0, 0, 0.6);
    z-index: 5;
}
.card{
    display:flex;
    flex-direction: column;
    gap:40px;
    /* margin: 0 auto; */
    padding:32px;
    width: 70%;
    height: fit-content;
    background-color: white;
    border-radius: 12px;
}
h4{
    font-weight: bold;
}
.buttons{
    display: flex;
    gap:8px;
}
.button{
    width:200px;
    height: 100%;
}
.buttonCancel{
    width:200px;
    height: 100%;
    padding: 13px;
    border: 1px #D4D4D8 solid;
    border-radius: 10px;
    background-color: white;
}
#cancel{
    height: 100%;
    border-radius: 10px;
}
.editDate{
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.editDate >div{
    display: flex;
    flex-direction: column;
    gap:8px;
}
#alert{
    /* font-size: 10px; */
    color: #DC2626;
}
/* ::v-deep .el-button.button{
    
    height: 50px;
    padding: 13px;
} */

</style>