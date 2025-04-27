import React from "react"
import VaultsPanel from "./components/VaultsPanel"
import VdfPanel from "./components/VdfPanel"
import PqSignaturePanel from "./components/PqSignaturePanel"
import "./index.css"

export default function App() {
  return (
    <div className="container">
      <header className="header">
        <h1>QuantumKey Vault Dashboard</h1>
        <p>
          Secure and verifiable key management with threshold vaults, VDF, and
          PQ-signatures
        </p>
      </header>

      <div className="cards">
        <div className="card">
          <VaultsPanel />
        </div>
        <div className="card">
          <VdfPanel />
        </div>
        <div className="card">
          <PqSignaturePanel />
        </div>
      </div>

      <footer className="footer">
        © {new Date().getFullYear()} QuantumKey. All rights reserved.
      </footer>
    </div>
  )
}
