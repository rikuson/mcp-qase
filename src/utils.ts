import { AxiosResponse } from 'axios';
import { ResultAsync } from 'neverthrow';
import { QaseApi } from 'qaseio';

export type ApiError = {
  response?: { data?: { message?: string } };
  message: string;
};

export type ApiResponse<T> = {
  data: {
    result?: T;
    status: boolean;
    errorMessage?: string;
  };
};

export const formatApiError = (error: unknown) => {
  const apiError = error as ApiError;
  return apiError.response?.data?.message || apiError.message;
};

export const toResult = (promise: Promise<AxiosResponse>) =>
  ResultAsync.fromPromise(promise, formatApiError);

export const client = (({ QASE_API_TOKEN }) => {
  if (!QASE_API_TOKEN) {
    throw new Error(
      'QASE_API_TOKEN environment variable is required. Please set it before running the server.',
    );
  }
  return new QaseApi({
    token: QASE_API_TOKEN,
  });
})(process.env);
