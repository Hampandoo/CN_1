import axios, { type AxiosInstance } from "axios";
import { setupInterceptors } from "./interceptors";

const baseApi: AxiosInstance = axios.create({
  baseURL: 'http://localhost:8080',
  headers: {
    'Content-Type': 'application/json',
  }
});

setupInterceptors(baseApi);

export default baseApi;