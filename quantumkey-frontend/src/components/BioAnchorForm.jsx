import React, { useState } from "react";

export default function BioAnchorForm() {
  const [userId, setUserId] = useState("");
  const [hash, setHash] = useState("");
  const [status, setStatus] = useState("");

  const register = async () => {
    const resp = await fetch("/bio/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, bio_hash: hash }),
    });
    const json = await resp.json();
    setStatus(json.detail || JSON.stringify(json));
  };

  const verify = async () => {
    const resp = await fetch("/bio/verify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, bio_hash: hash }),
    });
    const json = await resp.json();
    setStatus(json.valid ? "✔ Verified" : "✖ Not verified");
  };

  return (
    <div className="card">
      <h2 className="section-title">Biometric Anchor</h2>
      <div className="form-row">
        <input
          className="input"
          placeholder="User ID"
          value={userId}
          onChange={e => setUserId(e.target.value)}
        />
        <input
          className="input"
          placeholder="Biometric hash"
          value={hash}
          onChange={e => setHash(e.target.value)}
        />
      </div>
      <div className="form-row">
        <button className="btn" onClick={register}>Register</button>
        <button className="btn" onClick={verify}>Verify</button>
      </div>
      {status && <div className="result">{status}</div>}
    </div>
  );
}
