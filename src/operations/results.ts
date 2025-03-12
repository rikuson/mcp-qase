import {
  TestStepResultCreateStatusEnum,
  ResultCreate,
  ResultCreateBulk,
  ResultUpdate,
} from 'qaseio';
import { z } from 'zod';
import { toResult } from '../utils.js';
import { apply, pipe } from 'ramda';
import { client } from '../utils.js';

export const GetResultsSchema = z.object({
  code: z.string(),
  limit: z.string().optional(),
  offset: z.string().optional(),
  status: z.nativeEnum(TestStepResultCreateStatusEnum).optional(),
  from: z.string().optional(),
  to: z.string().optional(),
});

export const GetResultSchema = z.object({
  code: z.string(),
  hash: z.string(),
});

export const CreateResultSchema = z.object({
  code: z.string(),
  id: z.number(),
  result: z.record(z.any()).transform((v) => v as ResultCreate),
});

export const CreateResultBulkSchema = z.object({
  code: z.string(),
  id: z.number(),
  results: z.record(z.any()).transform((v) => v as ResultCreateBulk),
});

export const UpdateResultSchema = z.object({
  code: z.string(),
  id: z.number(),
  hash: z.string(),
  result: z.record(z.any()).transform((v) => v as ResultUpdate),
});

export const getResults = pipe(
  apply(client.results.getResults.bind(client.results)),
  toResult,
);

export const getResult = pipe(
  client.results.getResult.bind(client.results),
  toResult,
);

export const createResult = pipe(
  client.results.createResult.bind(client.results),
  toResult,
);

export const createResultBulk = pipe(
  client.results.createResultBulk.bind(client.results),
  toResult,
);

export const updateResult = pipe(
  client.results.updateResult.bind(client.results),
  toResult,
);
