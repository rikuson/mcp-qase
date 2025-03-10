import { z } from "zod";
import { toResult } from "../utils.js";
import { apply, pipe } from "ramda";
import { client } from "../utils.js";

export const GetRunsSchema = z.object({
  code: z.string(),
  search: z.string().optional(),
  status: z.string().optional(),
  milestone: z.number().optional(),
  environment: z.number().optional(),
  fromStartTime: z.number().optional(),
  toStartTime: z.number().optional(),
  limit: z.number().optional(),
  offset: z.number().optional(),
  include: z.string().optional(),
});

export const GetRunSchema = z.object({
  code: z.string(),
  id: z.number(),
  include: z.enum(["cases"]).optional(),
});

export const getRuns = pipe(
  apply(client.runs.getRuns.bind(client.runs)),
  toResult,
);

export const getRun = pipe(client.runs.getRun.bind(client.runs), toResult);
