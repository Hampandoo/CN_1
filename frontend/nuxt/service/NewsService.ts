import { loadLatestNews } from "@/api/base/modules/news/";
import * as newsTypes from "@/api/base/modules/news/types";

class NewsService {
  async loadLatestNews() {
    return await loadLatestNews();
  }
}

export const newsService = new NewsService();