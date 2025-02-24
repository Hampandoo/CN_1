<template>
  <article class="page">
    <NewsList :page="newsPage" :size="newsSize" />
  </article>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import NewsList from '@/components/feature/news/NewsList.vue';

definePageMeta({ layout: 'main' });

const newsPage = ref(1);
const newsSize = ref(10);
</script>

<style scoped>

</style>