import React, { useState } from "react"
import axios from "axios"

export default function PqSignaturePanel() {
  const [message, setMessage] = useState("")
  const [falconSig, setFalconSig] = useState("")
  const [phaseProof, setPhaseProof] = useState("")
  const [verifyResult, setVerifyResult] = useState(null)

  const handleSign = async () => {
    const res = await axios.post("/pq/sign", { message })
    setFalconSig(res.data.falcon_signature)
    setPhaseProof(res.data.phase_proof)
    setVerifyResult(null)
  }

  const handleVerify = async () => {
    const res = await axios.post("/pq/verify", { message, falcon_signature: falconSig, phase_proof: phaseProof })
    setVerifyResult(res.data.valid)
  }

  return (
    <div className="p-4 border rounded space-y-4">
      <h2 className="text-xl font-semibold">PQ-signature</h2>
      <textarea
        rows={3}
        value={message}
        onChange={e => setMessage(e.target.value)}
        placeholder="Message"
        className="w-full p-2 border rounded"
      />
      <div className="flex gap-2">
        <button onClick={handleSign} className="px-4 py-2 bg-green-600 text-white rounded">Sign</button>
        <button
          onClick={handleVerify}
          disabled={!falconSig || !phaseProof}
          className="px-4 py-2 bg-blue-600 text-white rounded disabled:opacity-50"
        >
          Verify
        </button>
      </div>
      {falconSig && (
        <div>
          <h3 className="font-medium">Falcon Signature:</h3>
          <pre className="bg-gray-100 p-2 rounded break-all">{falconSig}</pre>
        </div>
      )}
      {phaseProof && (
        <div>
          <h3 className="font-medium">Phase Proof:</h3>
          <pre className="bg-gray-100 p-2 rounded break-all">{phaseProof}</pre>
        </div>
      )}
      {verifyResult !== null && (
        <div className={`${verifyResult ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'} p-2 rounded`}>
          {verifyResult ? 'Valid ✔️' : 'Invalid ❌'}
        </div>
      )}
    </div>
  )
}
