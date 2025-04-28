import React, { useState } from 'react'
import axios from 'axios'

export default function TimelockPanel() {
  const [toCreate, setToCreate] = useState('')
  const [unlockIn, setUnlockIn] = useState(30)
  const [createResp, setCreateResp] = useState(null)
  const [openId, setOpenId] = useState('')
  const [openedMsg, setOpenedMsg] = useState('')
  const [error, setError] = useState(null)

  const handleCreate = async e => {
    e.preventDefault()
    setError(null)
    setCreateResp(null)
    try {
      const resp = await axios.post('/timelock/create', {
        message: toCreate,
        unlock_in: Number(unlockIn)
      })
      setCreateResp(resp.data)
    } catch (e) {
      setError(e.response?.data?.detail || e.message)
    }
  }

  const handleOpen = async e => {
    e.preventDefault()
    setError(null)
    setOpenedMsg('')
    try {
      const resp = await axios.get(`/timelock/open/${openId}`)
      setOpenedMsg(resp.data.message)
    } catch (e) {
      setError(e.response?.data?.detail || e.message)
    }
  }

  return (
    <div style={{ padding: 16, background: '#fafafa', borderRadius: 8 }}>
      <h2>TimeLock</h2>

      <form onSubmit={handleCreate} style={{ marginBottom: 16 }}>
        <h3>Create Timelock</h3>
        <textarea
          value={toCreate}
          onChange={e => setToCreate(e.target.value)}
          placeholder="Secret message"
          rows={2}
          style={{ width: '100%', padding: 8 }}
          required
        />
        <div style={{ marginTop: 8 }}>
          <label>
            Unlock in (seconds):{' '}
            <input
              type="number"
              value={unlockIn}
              onChange={e => setUnlockIn(e.target.value)}
              min={1}
              style={{ width: 80 }}
            />
          </label>
        </div>
        <button type="submit" style={{ marginTop: 8 }}>Create</button>
      </form>

      {createResp && (
        <div style={{ marginBottom: 16 }}>
          <strong>ID:</strong> {createResp.id}<br/>
          <strong>Opens at:</strong> {createResp.ready_at}
        </div>
      )}

      <form onSubmit={handleOpen} style={{ marginBottom: 8 }}>
        <h3>Open Timelock</h3>
        <input
          type="text"
          value={openId}
          onChange={e => setOpenId(e.target.value)}
          placeholder="Enter ID"
          style={{ width: '100%', padding: 8 }}
          required
        />
        <button type="submit" style={{ marginTop: 8 }}>Open</button>
      </form>

      {openedMsg && (
        <div style={{ marginBottom: 8 }}>
          <strong>Message:</strong> {openedMsg}
        </div>
      )}

      {error && <div style={{ color: 'red', marginTop: 8 }}>{error}</div>}
    </div>
  )
}
