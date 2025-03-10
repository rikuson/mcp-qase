import { SharedStepUpdate } from "qaseio";
import { z } from "zod";
import { client, toResult } from "../utils.js";
import { pipe } from "ramda";

export const GetSharedStepsSchema = z.object({
  code: z.string(),
  search: z.string().optional(),
  limit: z.number().optional(),
  offset: z.number().optional(),
});

export const GetSharedStepSchema = z.object({
  code: z.string(),
  hash: z.string(),
});

export const CreateSharedStepSchema = z.object({
  code: z.string(),
  title: z.string(),
  action: z.string(),
  expected_result: z.string().optional(),
  data: z.string().optional(),
  steps: z
    .array(
      z.object({
        action: z.string(),
        expected_result: z.string().optional(),
        data: z.string().optional(),
        position: z.number().optional(),
      }),
    )
    .optional(),
});

export const UpdateSharedStepSchema = z
  .object({
    code: z.string(),
    hash: z.string(),
    title: z.string(),
    action: z.string(),
    expected_result: z.string().optional(),
    data: z.string().optional(),
    steps: z
      .array(
        z.object({
          action: z.string(),
          expected_result: z.string().optional(),
          data: z.string().optional(),
          position: z.number().optional(),
        }),
      )
      .optional(),
  })
  .transform((data) => ({
    code: data.code,
    hash: data.hash,
    stepData: {
      title: data.title,
      action: data.action,
      expected_result: data.expected_result,
      data: data.data,
      steps: data.steps,
    } as SharedStepUpdate,
  }));

export const DeleteSharedStepSchema = z.object({
  code: z.string(),
  hash: z.string(),
});

export const getSharedSteps = pipe(
  client.sharedSteps.getSharedSteps.bind(client.sharedSteps),
  toResult,
);

export const getSharedStep = pipe(
  client.sharedSteps.getSharedStep.bind(client.sharedSteps),
  toResult,
);

export const createSharedStep = pipe(
  client.sharedSteps.createSharedStep.bind(client.sharedSteps),
  toResult,
);

export const updateSharedStep = pipe(
  client.sharedSteps.updateSharedStep.bind(client.sharedSteps),
  toResult,
);

export const deleteSharedStep = pipe(
  client.sharedSteps.deleteSharedStep.bind(client.sharedSteps),
  toResult,
);

