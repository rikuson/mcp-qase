import { z } from "zod";
import { client, toResult } from "../utils.js";
import { pipe } from "ramda";

export const GetPlansSchema = z.object({
  code: z.string(),
  limit: z.number().optional(),
  offset: z.number().optional(),
});

export const GetPlanSchema = z.object({
  code: z.string(),
  id: z.number(),
});

export const CreatePlanSchema = z.object({
  code: z.string(),
  title: z.string(),
  description: z.string().optional(),
  cases: z.array(z.number()),
});

export const UpdatePlanSchema = z.object({
  code: z.string(),
  id: z.number(),
  title: z.string().optional(),
  description: z.string().optional(),
  cases: z.array(z.number()).optional(),
});

export const DeletePlanSchema = z.object({
  code: z.string(),
  id: z.number(),
});

export const getPlans = pipe(
  client.plans.getPlans.bind(client.plans),
  toResult,
);

export const getPlan = pipe(client.plans.getPlan.bind(client.plans), toResult);

export const createPlan = pipe(
  client.plans.createPlan.bind(client.plans),
  toResult,
);

export const updatePlan = pipe(
  client.plans.updatePlan.bind(client.plans),
  toResult,
);

export const deletePlan = pipe(
  client.plans.deletePlan.bind(client.plans),
  toResult,
);
