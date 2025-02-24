import { ref, computed, watch } from "vue";
import { apiClient } from "../service/apiClient";
import { ENDPOINTS } from "../service/endpoints"
import { type ApiResponseNews } from "../types/news"

export const useNews = (initialPage?: number, initialSize?: number) => {
  const page = ref(initialPage);
  const page_size = ref(initialSize);

  function setQuery(newPage: number, newSize?: number) {
    page.value = newPage;
    page_size.value = newSize  || page_size.value;
  }

  const queryParams = computed(() => {
    return {
      page: page.value,
      page_size: page_size.value
    };
  });
  
  const { data: news, pending, refresh } = useAsyncData(
    `news-${JSON.stringify(queryParams.value)}`,
    () => apiClient<ApiResponseNews[]>(ENDPOINTS.GENERATORS.GENERATED_NEWS, { query: queryParams.value, server: true })
  );

  watch(queryParams, () => {
    refresh();
  }, { deep: true })

  return { news, pending, setQuery }
}