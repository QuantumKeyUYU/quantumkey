// src/__tests__/PqSignaturePanel.test.jsx
import React from 'react'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import axios from 'axios'
import PqSignaturePanel from '../components/PqSignaturePanel'

// Мокаем axios
jest.mock('axios')

describe('PqSignaturePanel', () => {
  beforeEach(() => {
    axios.post.mockReset()
  })

  test('рендерит формы и успешно подписывает', async () => {
    // Настраиваем mock-ответ для POST /pq/sign
    axios.post.mockResolvedValueOnce({
      data: { falcon_sig: 'FALCON', phase_proof: 'VDF123' }
    })

    render(<PqSignaturePanel />)

    // Вводим сообщение и кликаем Sign
    const textarea = screen.getByPlaceholderText(/сообщение для подписи/i)
    fireEvent.change(textarea, { target: { value: 'hello' } })
    fireEvent.click(screen.getByText(/^sign$/i))

    // Ждём, пока появится подпись
    await waitFor(() => {
      expect(screen.getByText(/FALCON:VDF123/)).toBeInTheDocument()
    })

    // Проверяем, что axios вызвался корректно
    expect(axios.post).toHaveBeenCalledWith('/pq/sign', { message: 'hello' })
  })

  test('обрабатывает ошибку при верификации', async () => {
    // Мокаем ответ invalid
    axios.post.mockResolvedValueOnce({ data: { valid: false } })

    render(<PqSignaturePanel />)

    // Вводим поля верификации
    fireEvent.change(screen.getByPlaceholderText(/сообщение для проверки/i), {
      target: { value: 'msg' }
    })
    fireEvent.change(screen.getByPlaceholderText(/^подпись$/i), {
      target: { value: 'bad' }
    })
    fireEvent.click(screen.getByText(/^verify$/i))

    // Ждём результат
    await waitFor(() => {
      expect(screen.getByText(/❌ Invalid/)).toBeInTheDocument()
    })
  })
})
