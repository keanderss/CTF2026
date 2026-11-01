// @ts-check

import mdx from '@astrojs/mdx';
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';

import react from '@astrojs/react';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://example.com',
  output: 'server',
  adapter: vercel(),
  integrations: [mdx(), react()],
  vite: {
    plugins: [tailwindcss()],
  },
});