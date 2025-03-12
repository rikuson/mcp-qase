import { z } from 'zod';
import { client, toResult } from '../utils.js';
import { pipe } from 'ramda';

export const GetSuitesSchema = z.object({
  code: z.string(),
  search: z.string().optional(),
  limit: z.number().optional(),
  offset: z.number().optional(),
});

export const GetSuiteSchema = z.object({
  code: z.string(),
  id: z.number(),
});

export const CreateSuiteSchema = z.object({
  code: z.string(),
  title: z.string(),
  description: z.string().optional(),
  preconditions: z.string().optional(),
  parent_id: z.number().optional(),
});

export const UpdateSuiteSchema = z.object({
  code: z.string(),
  id: z.number(),
  title: z.string().optional(),
  description: z.string().optional(),
  preconditions: z.string().optional(),
  parent_id: z.number().optional(),
});

export const DeleteSuiteSchema = z.object({
  code: z.string(),
  id: z.number(),
});

export const getSuites = pipe(
  client.suites.getSuites.bind(client.suites),
  toResult,
);

export const getSuite = pipe(
  client.suites.getSuite.bind(client.suites),
  toResult,
);

export const createSuite = pipe(
  client.suites.createSuite.bind(client.suites),
  toResult,
);

export const updateSuite = pipe(
  client.suites.updateSuite.bind(client.suites),
  toResult,
);

export const deleteSuite = pipe(
  client.suites.deleteSuite.bind(client.suites),
  toResult,
);
