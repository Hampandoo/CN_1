import baseApi from "../../instance";
import * as endpoints from "./endpoints";
import * as types from './types';
import * as sharedTypes from '../../shared-types';

export async function loadLatestNews(): Promise<sharedTypes.ApiResponse<types.News[]>> {
  return baseApi.get(endpoints.GET_LATEST_NEWS);
}