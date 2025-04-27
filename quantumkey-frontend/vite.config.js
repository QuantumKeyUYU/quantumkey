// quantumkey-frontend/vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [
    react(),  // React плагин для Vite
  ],
  server: {
    port: 3000,
    proxy: {
      '/threshold': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/vdf': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/pq': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
    },
  },
})
