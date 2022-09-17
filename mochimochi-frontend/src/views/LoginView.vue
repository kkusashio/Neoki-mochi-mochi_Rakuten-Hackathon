<script setup lang="ts">
import router from "@/router";
import axios from "axios";
import { reactive } from "vue";
import store from "../store/index";

type FormValue = {
  username: string;
  password: string;
};
const formValue = reactive<FormValue>({
  username: "",
  password: "",
});

const login = async () => {
  await axios
    .post("/auth/login/", formValue)
    .then((e) => {
      store.commit("setUser", { token: e.data.token, name: formValue.username });
      router.push("/main");
    })
    .catch((e) => console.error(e));
};
</script>

<template>
  <div class="login">
    <form class="login__form" @submit.prevent="login">
      <label>
        <input required type="text" placeholder="ユーザー名" v-model="formValue.username" />
      </label>
      <label>
        <input required type="password" placeholder="パスワード" v-model="formValue.password" />
      </label>
      <button>ログイン</button>
    </form>
  </div>
</template>

<style lang="scss" scoped>
.login {
  height: 100%;
  background-color: #ebecf0;
  display: flex;
  align-items: center;
  justify-content: center;
}
button,
input {
  border: 0;
  outline: 0;
  font-size: 16px;
  border-radius: 320px;
  padding: 16px;
  background-color: #ebecf0;
  text-shadow: 1px 1px 0 #fff;
}
label {
  display: block;
  margin-bottom: 24px;
  width: 500px;
}
input {
  margin-right: 8px;
  box-shadow: inset 2px 2px 5px #babecc, inset -5px -5px 10px #fff;
  width: 100%;
  box-sizing: border-box;
  transition: all 0.2s ease-in-out;
  appearance: none;
  -webkit-appearance: none;
}
input:focus {
  box-shadow: inset 1px 1px 2px #babecc, inset -1px -1px 2px #fff;
}
button {
  color: #61677c;
  font-weight: bold;
  box-shadow: -5px -5px 20px #fff, 5px 5px 20px #babecc;
  transition: all 0.2s ease-in-out;
  cursor: pointer;
  width: 300px;
}
button:hover {
  box-shadow: -2px -2px 5px #fff, 2px 2px 5px #babecc;
}
button:active {
  box-shadow: inset 1px 1px 2px #babecc, inset -1px -1px 2px #fff;
}
</style>
