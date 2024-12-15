<template>
  <div class="news-card">
    <div class="news-card-content">
      <div>{{ news.content }}</div>
    </div>
  </div>
</template>

<script setup lang='ts'>
import * as newsType from "~/api/base/modules/news/types";
interface Props {
  news: newsType.News
} 

defineProps<Props>();
</script>

<style scoped>
.news-card {
  border: 2px solid var(--color-green);
  border-radius: 4px;
  padding: 10px 12px;
  /* background:  linear-gradient(135deg, #f8f5f2, var(--color-green)); */
}
</style>