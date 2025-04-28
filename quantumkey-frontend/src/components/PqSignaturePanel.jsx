import React, { useState } from 'react'
import axios from 'axios'

export default function PqSignaturePanel() {
  const [msg, setMsg] = useState('')
  const [sig, setSig] = useState('')
  const [errS, setErrS] = useState(null)
  const [vMsg, setVMsg] = useState('')
  const [vSig, setVSig] = useState('')
  const [resV, setResV] = useState(null)
  const [errV, setErrV] = useState(null)

  const handleSign = async e => {
    e.preventDefault()
    setErrS(null); setSig('')
    try {
      const { falcon_sig, phase_proof } = (await axios.post('/pq/sign', { message: msg })).data
      setSig(`${falcon_sig}:${phase_proof}`)
    } catch (e) {
      setErrS(e.response?.data?.detail || e.message)
    }
  }

  const handleVerify = async e => {
    e.preventDefault()
    setErrV(null); setResV(null)
    try {
      const { valid } = (await axios.post('/pq/verify', {
        message: vMsg,
        signature: vSig
      })).data
      setResV(valid)
    } catch (e) {
      setErrV(e.response?.data?.detail || e.message)
    }
  }

  return (
    <div style={{ padding: 16, background: '#eef6ff', borderRadius: 8 }}>
      <h2>PQ-Signature</h2>

      <form onSubmit={handleSign} style={{ marginBottom: 24 }}>
        <textarea
          value={msg}
          onChange={e => setMsg(e.target.value)}
          placeholder="Сообщение для подписи"
          rows={3}
          style={{ width: '100%', padding: 8 }}
        />
        <button type="submit" style={{ marginTop: 8 }}>Sign</button>
        {sig  && <pre style={{ background: '#fff', padding: 8, marginTop: 8 }}>{sig}</pre>}
        {errS && <div style={{ color: 'red', marginTop: 8 }}>{errS}</div>}
      </form>

      <form onSubmit={handleVerify}>
        <textarea
          value={vMsg}
          onChange={e => setVMsg(e.target.value)}
          placeholder="Сообщение для проверки"
          rows={2}
          style={{ width: '100%', padding: 8 }}
        />
        <textarea
          value={vSig}
          onChange={e => setVSig(e.target.value)}
          placeholder="Подпись"
          rows={2}
          style={{ width: '100%', padding: 8, marginTop: 8 }}
        />
        <button type="submit" style={{ marginTop: 8 }}>Verify</button>
        {resV !== null && (
          <div style={{ marginTop: 8 }}>
            Результат: {resV ? '✅ Valid' : '❌ Invalid'}
          </div>
        )}
        {errV && <div style={{ color: 'red', marginTop: 8 }}>{errV}</div>}
      </form>
    </div>
  )
}
