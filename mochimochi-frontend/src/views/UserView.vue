<script setup lang="ts">
import store from "@/store";
</script>

<template>
  <div class="user-page">
    <p class="user-page__name">{{ store.getters.name }}さん</p>
    <img class="user-page__img" :src="require('@/assets/img/rank.jpg')" alt="" />
  </div>
</template>

<style lang="scss" scoped>
.user-page {
  height: 100%;
  padding-top: 20px;

  &__name {
    font-size: 40px;
    font-weight: bold;
    color: rgb(92, 92, 92);
  }

  &__img {
    height: calc(100vh - 300px);
  }
}
</style>
