export const apiClient = async <T>(url: string, options: { query?: Record<string, any>, server?: boolean } = {}) => {
  return await $fetch<T>(url, {
    baseURL: useRuntimeConfig().public.API_BASE_URL,
    query: options.query,
    server: options.server ?? true,
  })
}