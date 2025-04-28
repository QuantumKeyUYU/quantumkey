import React, { useState } from 'react'
import axios from 'axios'

export default function VdfPanel() {
  const [msg, setMsg] = useState('')
  const [digest, setDigest] = useState('')
  const [error, setError] = useState(null)

  const handleEval = async e => {
    e.preventDefault()
    setError(null)
    setDigest('')
    try {
      const resp = await axios.get('/vdf/eval', { params: { message: msg } })
      setDigest(resp.data.phase_proof || resp.data.digest || resp.data) 
    } catch (e) {
      setError(e.response?.data?.detail || e.message)
    }
  }

  return (
    <div style={{ padding: 16, background: '#fafafa', borderRadius: 8 }}>
      <h2>VDF (Verifiable Delay Function)</h2>

      <form onSubmit={handleEval}>
        <textarea
          value={msg}
          onChange={e => setMsg(e.target.value)}
          placeholder="Message to eval"
          rows={3}
          style={{ width: '100%', padding: 8 }}
          required
        />
        <button type="submit" style={{ marginTop: 8 }}>Eval VDF</button>
      </form>

      {digest && (
        <div style={{ marginTop: 16 }}>
          <strong>Phase Proof / Digest:</strong>
          <pre style={{ background: '#fff', padding: 8 }}>{digest}</pre>
        </div>
      )}

      {error && <div style={{ color: 'red', marginTop: 8 }}>{error}</div>}
    </div>
  )
}
