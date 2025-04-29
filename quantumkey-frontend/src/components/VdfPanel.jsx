// quantumkey-frontend/src/components/VdfPanel.jsx
import React, { useState } from 'react'
import axios from 'axios'

export default function VdfPanel() {
  const [input, setInput] = useState('')
  const [proof, setProof] = useState('')
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleEval = async (e) => {
    e.preventDefault()
    setError(null)
    setProof('')
    setLoading(true)
    try {
      const resp = await axios.get('/vdf/eval', {
        params: { input_data: input }
      })
      setProof(resp.data.result)
    } catch (err) {
      setError(err.response?.data?.detail || err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <h2>VDF (Verifiable Delay Function)</h2>

      <form onSubmit={handleEval} style={{ display: 'flex', gap: 12, flexWrap: 'wrap' }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Input data"
          style={{ flex: '1 1 200px', padding: 8 }}
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Evaluating…' : 'Eval VDF'}
        </button>
      </form>

      {proof && (
        <div className="result">
          <strong>Proof:</strong> {proof}
        </div>
      )}
      {error && <div style={{ color: 'red', marginTop: 8 }}>{error}</div>}
    </div>
  )
}
