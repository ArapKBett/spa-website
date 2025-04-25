import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  plugins: [svelte()],
  root: '.', // Explicitly set to frontend/ directory
  publicDir: 'public', // Explicitly set public directory
  server: {
    port: 5173
  },
  build: {
    outDir: 'build', // Output to build/
    emptyOutDir: true // Clear build/ before building
  }
});
