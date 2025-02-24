<template>
  <div class="news-list-container">
    <NewsCard v-for="newsItem in news?.items" :news="newsItem" :key="newsItem.id" v-memo="newsItem.id" />
  </div>
</template>

<script setup lang="ts">
import { watch } from 'vue';
import { useNews } from '@/composables/useNews';
import NewsCard from './NewsCard.vue';

type Props = {
  page: number;
  size: number;
}

const $props = withDefaults(defineProps<Props>(), {
  page: 1,
  size: 10
})

const { news, pending, setQuery } = useNews($props.page, $props.size);

watch(() => $props.page, () => {
  setQuery($props.page, $props.size)
})
</script>

<style scoped>
.news-list-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  gap: 10px;

  max-width: 100%;
}
</style>