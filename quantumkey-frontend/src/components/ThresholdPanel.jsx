import React, { useState } from 'react'
import axios from 'axios'

export default function ThresholdPanel() {
  const [secret, setSecret] = useState('')
  const [n, setN] = useState(3)
  const [k, setK] = useState(2)
  const [shares, setShares] = useState([])
  const [recoverInput, setRecoverInput] = useState('')
  const [recovered, setRecovered] = useState('')
  const [error, setError] = useState(null)

  const handleSplit = async e => {
    e.preventDefault()
    setError(null)
    setShares([])
    try {
      const resp = await axios.post('/threshold/split', {
        secret,
        n: Number(n),
        k: Number(k)
      })
      setShares(resp.data.shares)
    } catch (e) {
      setError(e.response?.data?.detail || e.message)
    }
  }

  const handleRecover = async e => {
    e.preventDefault()
    setError(null)
    setRecovered('')
    try {
      const arr = JSON.parse(recoverInput)
      const resp = await axios.post('/threshold/recover', { shares: arr })
      setRecovered(resp.data.secret)
    } catch (e) {
      setError(e.response?.data?.detail || e.message)
    }
  }

  return (
    <div style={{ padding: 16, background: '#fafafa', borderRadius: 8 }}>
      <h2>Threshold Vaults</h2>

      <form onSubmit={handleSplit} style={{ marginBottom: 16 }}>
        <h3>Split Secret</h3>
        <input
          type="text"
          value={secret}
          onChange={e => setSecret(e.target.value)}
          placeholder="Secret"
          style={{ width: '100%', padding: 8 }}
          required
        />
        <div style={{ marginTop: 8 }}>
          <label>
            Parts (n):{' '}
            <input
              type="number"
              value={n}
              onChange={e => setN(e.target.value)}
              min={2}
              style={{ width: 60 }}
            />
          </label>
          <label style={{ marginLeft: 16 }}>
            Threshold (k):{' '}
            <input
              type="number"
              value={k}
              onChange={e => setK(e.target.value)}
              min={2}
              max={n}
              style={{ width: 60 }}
            />
          </label>
        </div>
        <button type="submit" style={{ marginTop: 8 }}>Split</button>
      </form>

      {shares.length > 0 && (
        <div style={{ marginBottom: 16 }}>
          <strong>Shares:</strong>
          <pre style={{ background: '#fff', padding: 8, maxHeight: 150, overflow: 'auto' }}>
            {JSON.stringify(shares, null, 2)}
          </pre>
        </div>
      )}

      <form onSubmit={handleRecover} style={{ marginBottom: 8 }}>
        <h3>Recover Secret</h3>
        <textarea
          value={recoverInput}
          onChange={e => setRecoverInput(e.target.value)}
          placeholder='Enter shares JSON, e.g. ["share1","share2",...]'
          rows={3}
          style={{ width: '100%', padding: 8 }}
          required
        />
        <button type="submit" style={{ marginTop: 8 }}>Recover</button>
      </form>

      {recovered && (
        <div style={{ marginBottom: 8 }}>
          <strong>Recovered Secret:</strong> {recovered}
        </div>
      )}

      {error && <div style={{ color: 'red', marginTop: 8 }}>{error}</div>}
    </div>
  )
}
