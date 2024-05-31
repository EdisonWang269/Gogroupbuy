<template>
  <div class="center">
    <div class="login">
      <div class="header">
        <span id="title">團購系統</span>
        <br /><span id="caption">管理者頁面</span>
      </div>

      <div class="info">
        <span>Email</span>
        <input
          type="email"
          :class="status"
          :placeholder="placeholder"
          aria-label="Username"
          aria-describedby="basic-addon1"
          v-model="email"
        />
        <span>Password</span>
        <div class="input-group mb-3">
          <input
            :type="type"
            :class="status"
            id="password"
            placeholder="請輸入密碼"
            aria-label="Recipient's username"
            aria-describedby="basic-addon2"
            v-model="password"
          />
          <span class="input-group-text" id="basic-addon2"
            ><i :class="icon" id="suffix" @click="isShowed"></i
          ></span>
        </div>
      </div>
      <store-button
        :action="action"
        :icon="'<i class=\'bi bi-arrow-right\'></i>'"
        class="button"
        @click="logIn"
      />
    </div>
  </div>
</template>

<script>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  import StoreButton from "@/components/StoreButton.vue";
  export default {
    components: {
      StoreButton,
    },
    setup() {
      const router = useRouter();
      const action = "LogIn ";
      const icon = ref("bi bi-eye-slash");
      const show = ref(false);
      const type = ref("password");
      const validEmail = ref(true);
      const placeholder = ref("請輸入電子郵件");
      const status = ref("form-control");
      const email = ref("");
      const emailInput = ref(null); //要連資料庫判斷是否有帳號
      const password = ref(""); // 這也是連資料庫判斷
      const isShowed = () => {
        show.value = !show.value;
        if (show.value) {
          icon.value = "bi bi-eye";
          type.value = "text";
        } else {
          icon.value = "bi bi-eye-slash";
          type.value = "password";
        }
      };
      const logIn = () => {
        validEmail.value =
          emailInput.value &&
          emailInput.value.checkValidity() &&
          password.value;

        if (validEmail.value) {
          router.push("/manage");
          console.log("Logged In");
        } else {
          console.log("fail");
          status.value = "warning";
          placeholder.value = "請輸入正確的電子郵件或密碼";
        }
      };
      return {
        action,
        // showPassword,
        // unShowPassword,
        isShowed,
        show,
        icon,
        type,
        logIn,
        status,
        placeholder,
        email,
        password,
      };
    },
  };
</script>

<style scoped>
  .warning #password {
    /* height:50px; */
    width: 90%;
    border-radius: 0.375rem;
    padding: 0.375rem 0.75rem;
    color: #f87171;
    border: #f87171 1px solid;
  }
  .warning {
    /* height:50px; */
    width: 100%;
    border-radius: 0.375rem;
    padding: 0.375rem 0.75rem;
    color: #f87171;
    border: #f87171 1px solid;
  }

  .normal {
    height: 50px;
    border-radius: 12px;
    width: 100%;
  }
  input:focus,
  .warning:focus {
    border: 1px solid #4763e4;
  }
  :root {
    --input-border-color: white; /* 设置输入框边框颜色为红色 */
  }
  .center {
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .login {
    width: 30%;
    min-width: 520px;
    display: flex;
    flex-direction: column;
    gap: 40px;
  }
  .button {
    width: 100%;
  }
  .header {
    margin: 0 auto;
    text-align: center;
  }
  #title {
    font-size: 40px;
  }
  #caption {
    font-size: 20px;
  }
  .info {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  #suffix {
    cursor: pointer;
    position: relative;
  }
  #suffix:hover {
    color: rgba(71, 99, 228, 1);
    /* border-radius: 3px; */
    /* padding: 0 2px; */
  }
  .input-group-text {
    background-color: white;
  }
  #password {
    border-right: none;
  }
</style>
