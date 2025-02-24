export type ApiResponseNews = {
  items: News[]
}

export type News = {
  id: number;
  date: string;
  emotional_tone: string;
  main_facts: string[];
  main_idea: string;
  relevant_keywords: string[];
}