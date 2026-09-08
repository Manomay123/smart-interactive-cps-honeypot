# Smart Interactive Honeypot for Cyber-Physical Systems (CPS)

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Focus](https://img.shields.io/badge/Security-SCADA%20%2F%20ICS%20%2F%20IIoT-red.svg)]()

A non-disruptive, deceptive security framework engineered to emulate Supervisory Control and Data Acquisition (SCADA), Industrial Control Systems (ICS), and Industrial IoT (IIoT) protocols. This framework captures malicious interaction, generates detailed attack logs, and applies threat intelligence analysis without risking operational disruption to live critical infrastructure.

---

## 🏗️ System Architecture & Workflow

1. **Deceptive Emulation Layer**: Simulates industrial protocols (e.g., Modbus, DNP3, Ethernet/IP) to attract automated scanners, advanced persistent threats (APTs), and unauthorized reconnaissance.
2. **Interaction & Telemetry Ingestion**: Captures complete payload streams, session telemetry, and attacker commands in real time.
3. **AI Threat Analytics**: Processes raw logs to classify attack patterns, identify payload anomalies, and score threat severity.

---

## 📁 Repository Structure

- `01_Architecture_and_Design/`: System topology diagrams, threat model, and design specifications.
- `02_Honeypot_Code_and_Logs/`: Interaction scripts, protocol emulators, and captured operational logs.
- `03_AI_Model_and_Analytics/`: Analytics scripts, machine learning classification pipelines, and feature extraction.
- `04_Screenshots/`: Execution capture, terminal logs, and system monitoring outputs.
- `05_Final_Report_and_Presentation/`: Comprehensive project report and presentation deck.

---

## 🛡️ Target Environment Scope

- **SCADA / ICS Protocols**: Modbus TCP, DNP3, S7comm simulation targets.
- **Industrial IoT**: Embedded edge controllers and sensor gateway interfaces.
- **Threat Vector Coverage**: Reconnaissance, brute-force attempts, unauthorized register manipulation, and replay attacks.

---

## 👤 Author

Created by **Manomay Saxena** — *Cyber Security Essentials Certification (Capstone Project)*.
