import React, { useState } from "react"
import axios from "axios"

export default function VdfPanel() {
  const [input, setInput] = useState("")
  const [delay, setDelay] = useState(5)
  const [proof, setProof] = useState("")
  const [loading, setLoading] = useState(false)

  const evalVdf = async () => {
    setLoading(true)
    try {
      const res = await axios.get("/vdf/eval", { params: { input_data: input, delay } })
      setProof(res.data.result)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="p-4 border rounded space-y-3">
      <h2 className="text-xl font-semibold">Verifiable Delay Function</h2>
      <input
        type="text"
        placeholder="Input data"
        value={input}
        onChange={e => setInput(e.target.value)}
        className="w-full p-2 border rounded"
      />
      <div className="flex items-center gap-2">
        <label>Delay:</label>
        <input
          type="number"
          value={delay}
          min={1}
          onChange={e => setDelay(+e.target.value)}
          className="w-20 p-2 border rounded"
        />
        <button
          onClick={evalVdf}
          disabled={loading}
          className="px-4 py-2 bg-blue-600 text-white rounded"
        >
          {loading ? "Waiting..." : "Eval VDF"}
        </button>
      </div>
      {proof && (
        <div>
          <h3 className="font-medium">Proof:</h3>
          <pre className="bg-gray-100 p-2 rounded break-all">{proof}</pre>
        </div>
      )}
    </div>
  )
}
