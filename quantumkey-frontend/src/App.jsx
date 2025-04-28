// src/App.jsx

import React from 'react'
import ThresholdPanel   from './components/ThresholdPanel'
import VdfPanel         from './components/VdfPanel'
import TimelockPanel    from './components/TimelockPanel'
import PqSignaturePanel from './components/PqSignaturePanel'
import './index.css'

export default function App() {
  return (
    <div className="container">
      <header className="header">
        <h1>QuantumKey Vault Dashboard</h1>
        <p>Secure key management: Threshold Vaults, VDF, Timelock & PQ-Signatures</p>
      </header>

      <main className="dashboard">
        <div className="card">
          <ThresholdPanel />
        </div>
        <div className="card">
          <VdfPanel />
        </div>
        <div className="card">
          <TimelockPanel />
        </div>
        <div className="card">
          <PqSignaturePanel />
        </div>
        <div className="card">
          <h2>QuantumTimeLock (Phase 2)</h2>
          <p>Здесь будет расширенный UI для TEE & Биометрии.</p>
        </div>
        <div className="card">
          <h2>Biometric Anchor</h2>
          <p>Регистрация и проверка биометрических хэшей.</p>
        </div>
      </main>

      <footer className="footer">
        <p>© 2025 QuantumKey. All rights reserved.</p>
      </footer>
    </div>
  )
}
