<template>
  <div class="news-card">
    <div class="news-card-content">
      <div><p v-for="(line, key) in news.content" :key="line">{{key}}: {{line}}</p></div>
    </div>
  </div>
</template>

<script setup lang='ts'>
  import * as newsType from "~/api/base/modules/news/types";
  import { type ParsedNews } from "~/types/ParsedNews";

interface Props {
  news: ParsedNews
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