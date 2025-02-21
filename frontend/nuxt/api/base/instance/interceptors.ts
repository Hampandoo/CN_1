import { type AxiosInstance } from 'axios';
import { ApiError } from '../shared-types';
import { errorEnum } from '@/utils/enums/errorEnum';
import * as sharedTypes from "../shared-types";

export function setupInterceptors(axiosInstance: AxiosInstance) {
  setError(axiosInstance);
}

export const setError = (axiosInstance: AxiosInstance): void => {
  axiosInstance.interceptors.response.use(
    (response) => response,
    async (error): Promise<sharedTypes.ApiErrorResponse> => {
      if (error.response) {
        const { response } = error;
        let errorType: errorEnum = errorEnum.UnknownError;

        switch (response.status) {
          case 401:
            errorType = errorEnum.AuthenticationError;
            break;
          case 403:
            errorType = errorEnum.PermissionError;
            break;
          case 404:
            errorType = errorEnum.NotFoundError;
            break;
          case 422:
            errorType = errorEnum.ValidationError;
            break;
          case 500:
            errorType = errorEnum.ServerError;
            break;
          default: 
            errorType = errorEnum.UnknownError;
        }
        return Promise.reject(new ApiError(response.data.detail || 'Error', errorType, response.status, response.data));
      } else {
        return Promise.reject(new ApiError(error.data.detail, errorEnum.UnknownError));
      }
    });
}