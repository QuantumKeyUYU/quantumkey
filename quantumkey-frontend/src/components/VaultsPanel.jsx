import React, { useState } from "react";

export default function VaultsPanel() {
  const [secret, setSecret] = useState("");
  const [n, setN] = useState(5);
  const [k, setK] = useState(3);
  const [shares, setShares] = useState([]);

  const split = async () => {
    const resp = await fetch("/threshold/split", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ secret, shares: n, threshold: k }),
    });
    const data = await resp.json();
    setShares(data.shards || []);
  };

  return (
    <div className="card">
      <h2 className="section-title">Threshold Vaults</h2>
      <div className="form-row">
        <input
          className="input"
          placeholder="Secret"
          value={secret}
          onChange={e => setSecret(e.target.value)}
        />
      </div>
      <div className="form-row">
        <input
          className="input small"
          type="number"
          value={n}
          onChange={e => setN(Number(e.target.value))}
        />
        <input
          className="input small"
          type="number"
          value={k}
          onChange={e => setK(Number(e.target.value))}
        />
        <button className="btn" onClick={split}>Split</button>
      </div>
      {shares.length > 0 && (
        <pre className="result">{JSON.stringify(shares, null, 2)}</pre>
      )}
    </div>
  );
}
