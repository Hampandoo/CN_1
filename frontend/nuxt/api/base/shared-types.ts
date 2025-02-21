import { errorEnum } from "@/utils/enums/errorEnum";

export class ApiError extends Error {
  constructor(
    public override message: string,
    public type: errorEnum = errorEnum.ServerError,
    public code?: number,
    public details?: any,
  ) {
    super(message);
    this.name = `Error Type: ${type}. Code: ${code}. Message`;
  }
}

export interface ApiSuccessResponse<T> {
  status: number;
  message?: string;
  data: T;
}
export type ApiErrorResponse = ApiError;
export type ApiResponse<T> = ApiSuccessResponse<T>;

export interface PaginatedList<T> {
  "items": T[],
  "total": number,
  "page": number,
  "size": number,
  "pages": number
}