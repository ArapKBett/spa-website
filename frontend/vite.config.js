import { defineConfig } from 'vite';
import { sveltekit } from '@sveltejs/kit/vite';

export default defineConfig({
  plugins: [sveltekit()],
  server: {
    port: 5173
  },
  build: {
    outDir: 'build' // Ensure build output matches svelte.config.js
  }
});
