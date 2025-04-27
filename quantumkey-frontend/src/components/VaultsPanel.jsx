import React, { useState } from "react"
import axios from "axios"

export default function VaultsPanel() {
  const [secret, setSecret] = useState("")
  const [n, setN] = useState(5)
  const [t, setT] = useState(3)
  const [shares, setShares] = useState([])

  const split = async () => {
    const res = await axios.post("/threshold/split", { secret, shares: n, threshold: t })
    setShares(res.data.shares)
  }

  const recover = async () => {
    const res = await axios.post("/threshold/recover", { parts: shares.slice(0, t), prime: res.data.prime })
    alert(`Recovered: ${res.data.secret}`)
  }

  return (
    <div className="p-4 border rounded space-y-4">
      <h2 className="text-xl font-semibold">Threshold Vaults</h2>
      <input
        type="text"
        placeholder="Secret"
        value={secret}
        onChange={e => setSecret(e.target.value)}
        className="w-full p-2 border rounded"
      />
      <div className="flex gap-2">
        <input
          type="number"
          value={n}
          onChange={e => setN(+e.target.value)}
          className="w-20 p-2 border rounded"
        />
        <input
          type="number"
          value={t}
          onChange={e => setT(+e.target.value)}
          className="w-20 p-2 border rounded"
        />
        <button onClick={split} className="px-4 py-2 bg-green-600 text-white rounded">Split</button>
      </div>
      {shares.length > 0 && (
        <ul className="list-disc pl-5">
          {shares.map((s, i) => (
            <li key={i} className="break-all">{s}</li>
          ))}
        </ul>
      )}
    </div>
  )
}