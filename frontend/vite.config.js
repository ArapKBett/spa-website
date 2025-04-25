import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import path from 'path';

export default defineConfig({
  plugins: [svelte()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  css: {
    preprocessorOptions: {
      scss: {},
    },
  },
  build: {
    outDir: 'build', // Output to build/ instead of dist/
    emptyOutDir: true, // Clear build/ before building
  },
  base: '/', // Ensure correct base path for SPA
});
