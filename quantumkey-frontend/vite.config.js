import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  resolve: {
    extensions: ['.js', '.jsx']
  },
  server: {
    proxy: {
      '/threshold': 'http://localhost:8000',
      '/vdf':       'http://localhost:8000',
      '/timelock':  'http://localhost:8000',
      '/pq':        'http://localhost:8000'
    }
  }
})
