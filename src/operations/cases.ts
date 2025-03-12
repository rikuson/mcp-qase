import { TestCaseCreate } from 'qaseio';
import { z } from 'zod';
import { client, toResult } from '../utils.js';
import { apply, pipe } from 'ramda';

export const GetCasesSchema = z.object({
  code: z.string(),
  search: z.string().optional(),
  milestoneId: z.number().optional(),
  suiteId: z.number().optional(),
  severity: z.string().optional(),
  priority: z.string().optional(),
  type: z.string().optional(),
  behavior: z.string().optional(),
  automation: z.string().optional(),
  status: z.string().optional(),
  externalIssuesType: z
    .enum([
      'asana',
      'azure-devops',
      'clickup-app',
      'github-app',
      'gitlab-app',
      'jira-cloud',
      'jira-server',
      'linear',
      'monday',
      'redmine-app',
      'trello-app',
      'youtrack-app',
    ])
    .optional(),
  externalIssuesIds: z.array(z.string()).optional(),
  include: z.string().optional(),
  limit: z.number().optional(),
  offset: z.number().optional(),
});

export const GetCaseSchema = z.object({
  code: z.string(),
  id: z.number(),
});

export const CreateCaseSchema = z.object({
  code: z.string(),
  testCase: z.record(z.any()).transform((v) => v as TestCaseCreate),
});

export const UpdateCaseSchema = z.object({
  code: z.string(),
  id: z.number(),
  title: z.string().optional(),
  description: z.string().optional(),
  preconditions: z.string().optional(),
  postconditions: z.string().optional(),
  severity: z.number().optional(),
  priority: z.number().optional(),
  type: z.number().optional(),
  behavior: z.number().optional(),
  automation: z.number().optional(),
  status: z.number().optional(),
  suite_id: z.number().optional(),
  milestone_id: z.number().optional(),
  layer: z.number().optional(),
  is_flaky: z.boolean().optional(),
  params: z
    .array(
      z.object({
        title: z.string(),
        value: z.string(),
      }),
    )
    .optional(),
  tags: z.array(z.string()).optional(),
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
  custom_fields: z
    .array(
      z.object({
        id: z.number(),
        value: z.string(),
      }),
    )
    .optional(),
});

export const CreateCaseBulkSchema = z.object({
  code: z.string(),
  cases: z.array(
    z.object({
      title: z.string(),
      description: z.string().optional(),
      preconditions: z.string().optional(),
      postconditions: z.string().optional(),
      severity: z.number().optional(),
      priority: z.number().optional(),
      type: z.number().optional(),
      behavior: z.number().optional(),
      automation: z.number().optional(),
      status: z.number().optional(),
      suite_id: z.number().optional(),
      milestone_id: z.number().optional(),
      layer: z.number().optional(),
      is_flaky: z.boolean().optional(),
      params: z
        .array(
          z.object({
            title: z.string(),
            value: z.string(),
          }),
        )
        .optional(),
      tags: z.array(z.string()).optional(),
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
      custom_fields: z
        .array(
          z.object({
            id: z.number(),
            value: z.string(),
          }),
        )
        .optional(),
    }),
  ),
});

export const getCases = pipe(
  apply(client.cases.getCases.bind(client.cases)),
  toResult,
);

export const getCase = pipe(client.cases.getCase.bind(client.cases), toResult);

export const createCase = pipe(
  client.cases.createCase.bind(client.cases),
  toResult,
);

const convertCaseData = (
  data: Omit<z.infer<typeof UpdateCaseSchema>, 'code' | 'id'>,
) => ({
  ...data,
  is_flaky: data.is_flaky === undefined ? undefined : data.is_flaky ? 1 : 0,
  params: data.params
    ? data.params.reduce(
        (acc, param) => ({
          ...acc,
          [param.title]: [param.value],
        }),
        {},
      )
    : undefined,
});

export const updateCase = pipe(
  (
    code: string,
    id: number,
    data: Omit<z.infer<typeof UpdateCaseSchema>, 'code' | 'id'>,
  ) => client.cases.updateCase(code, id, convertCaseData(data)),
  toResult,
);
