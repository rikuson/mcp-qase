import { ProjectCreateAccessEnum } from 'qaseio';
import { z } from 'zod';
import { client, toResult } from '../utils.js';
import { pipe } from 'ramda';

export const ListProjectsSchema = z.object({
  limit: z.number().optional(),
  offset: z.number().optional(),
});

export const GetProjectSchema = z.object({
  code: z.string(),
});

export const CreateProjectSchema = z.object({
  code: z.string(),
  title: z.string(),
  description: z.string().optional(),
  access: z.nativeEnum(ProjectCreateAccessEnum).optional(),
  group: z.string().optional(),
});

export const listProjects = pipe(
  client.projects.getProjects.bind(client.projects),
  toResult,
);

export const getProject = pipe(
  client.projects.getProject.bind(client.projects),
  toResult,
);

export const createProject = pipe(
  client.projects.createProject.bind(client.projects),
  toResult,
);
