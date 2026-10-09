import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const modelsCollection = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/models" }),
  schema: z.object({
    title: z.string(),
    lab: z.string(),
    releaseDate: z.date(),
    contextWindow: z.string(),
    license: z.string(),
    description: z.string(),
    officialUrl: z.string().url().optional(),
    paperUrl: z.string().url().optional(),
    modalities: z.array(z.string()).optional(),
    image: z.string().url().optional(),
    sourceUrl: z.string().url().optional(),
    sourceTitle: z.string().optional(),
  })
});

const labsCollection = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/labs" }),
  schema: z.object({
    name: z.string(),
    location: z.string(),
    description: z.string(),
    website: z.string().url().optional(),
    image: z.string().url().optional(),
    sourceUrl: z.string().url().optional(),
    sourceTitle: z.string().optional(),
  })
});

const researchersCollection = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/researchers" }),
  schema: z.object({
    name: z.string(),
    lab: z.string(),
    role: z.string(),
    famousFor: z.string(),
    image: z.string().url().optional(),
    sourceUrl: z.string().url().optional(),
    sourceTitle: z.string().optional(),
    links: z.object({
      x: z.string().url().optional(),
      github: z.string().url().optional(),
      scholar: z.string().url().optional(),
    }).optional()
  })
});

export const collections = {
  'models': modelsCollection,
  'labs': labsCollection,
  'researchers': researchersCollection,
};
