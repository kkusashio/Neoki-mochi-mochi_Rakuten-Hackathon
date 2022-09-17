<script setup lang="ts">
import router from "@/router";
import store from "../store/index";
const logout = () => {
  store.commit("setUser", null);
  router.push("/");
};
</script>

<template>
  <div class="header">
    <div class="header__logo">
      <router-link class="header__logo-button" to="/">
        <img class="header__logo-img" :src="require('@/assets/img/logo.png')" alt="" />
      </router-link>
    </div>
    <div v-if="store.getters.isLogin" class="header__nav">
      <!-- eslint-disable-next-line -->
      <router-link class="header__nav-button" to="main">メインページへ</router-link>
      <div class="header__nav-button" to="/" @click="logout">ログアウト</div>
    </div>
    <div v-else class="header__nav">
      <!-- eslint-disable-next-line -->
      <router-link class="header__nav-button" to="register">新規登録</router-link>
      <router-link class="header__nav-button" to="login">ログイン</router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.header {
  background-color: #ffc2b4;
  padding: 0px 10px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;

  &__logo {
    height: 90%;
  }

  &__logo-img {
    height: 100%;
  }

  &__nav-button {
    display: inline-block;
    background-color: #ffc2b4;
    padding: 10px 15px;
    border-radius: 5px;
    text-decoration: none;
    color: white;
    font-size: 20px;
    font-weight: bold;
    transition: all 0.2s ease-in-out;
    cursor: pointer;

    &:hover {
      background-color: #fed7ce;
    }

    &:not(:last-child) {
      margin-right: 10px;
    }
  }
}
</style>
