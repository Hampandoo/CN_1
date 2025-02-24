<template>
  <div class="news-card">
    <h3>{{ news.main_idea }}</h3>
    <ul>
      <li v-for="(fact, idx) in news.main_facts" :key="idx" v-memo="idx">
        {{ fact }}
      </li>
    </ul>
    <p>Emotional tone: {{ news.emotional_tone }}</p>
    <p>
      <span v-for="keyword in news.relevant_keywords" :key="keyword" v-memo="keyword" class="keyword">{{ keyword }}</span>
    </p>
    <span>Date: {{ news.date }}</span>
  </div>
</template>

<script lang="ts" setup>
import { type News } from '@/types/news';
type Props = {
  news: News
}
const $props = defineProps<Props>();
</script>

<style scoped>
.news-card {
  background: var(--color-background);
  border-radius: 8px;
  border: 1px solid var(--color-green);
  padding: 10px;

  width: 100%;
}
.keyword {
  margin: 0 6px;
}
</style>