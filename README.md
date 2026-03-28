# 🛡️ Privacy Sentinel

**AI-Powered Local Anomaly Detection & Privacy Monitoring System**

---

## 🚀 Overview

Privacy Sentinel is a **real-time host-based anomaly detection system** that monitors system behavior to detect suspicious or privacy-invasive activities.

It combines:

* 🔍 **System monitoring** (process, network, devices, screen)
* 🧠 **Rule-based behavioral intelligence**
* 🤖 **Machine learning (Isolation Forest)**
* 💡 *(Planned)* **LLM + RAG for explainable AI**

---

## 🎯 Problem Statement

Modern systems run multiple background processes with **no visibility** into:

* Microphone / camera usage
* Screen recording / sharing
* Hidden data transmission
* Fake or spoofed applications

Traditional antivirus:

* ❌ relies on signatures
* ❌ fails on unknown threats

👉 Privacy Sentinel solves this using **behavior + anomaly detection**

---

## 🧠 System Architecture

```
System (OS Events)
        ↓
Monitoring Layer (Sensors)
        ↓
Context Builder
        ↓
Identity Verification
        ↓
Behavior Analysis
        ↓
Brain Engine (Rule-based)
        ↓
SQLite Database
        ↓
Feature Engine
        ↓
ML Model (Isolation Forest)
        ↓
LLM (RAG - planned)
```

---

## 🔍 Features

### ✅ Real-Time Monitoring

* Process creation & termination
* CPU usage tracking
* Network connections (IP + port mapping)
* Microphone & camera access detection
* Screen recording / sharing detection

---

### 🧠 Intelligent Risk Detection

* Identity verification (path + signature)
* Behavior correlation (mic + network, screen + network, etc.)
* Risk classification:

  * 🟢 LOW
  * 🟡 MEDIUM
  * 🟠 HIGH
  * 🔴 CRITICAL

---

### 🤖 Machine Learning

* Uses **Isolation Forest**
* Learns *normal system behavior*
* Detects **anomalies without labeled data**

---

### 🗄 Data Logging

* Stores structured logs in SQLite
* Enables:

  * training ML model
  * historical analysis
  * debugging

---

### 🔮 Future (LLM + RAG)

* Explain detected anomalies
* Answer:

  * “Is this dangerous?”
  * “Why is this flagged?”
* Local lightweight models (Mistral / Phi)

---

## 🏗 Project Structure

```
privacy_sentinel/
│
├── core/
│   ├── process_monitor.py
│   ├── network_monitor.py
│   ├── device_monitor.py
│   ├── screen_monitor.py
│   ├── context_builder.py
│   ├── identity.py
│   ├── behavior.py
│   ├── brain.py
│   ├── feature_engine.py
│   ├── train_model.py
│   └── predict.py
│
├── database/
│   └── db.py
│
├── model.pkl
├── main.py
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/privacy-sentinel.git
cd privacy-sentinel
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Required libraries:

```text
psutil
pandas
scikit-learn
joblib
```

---

## ▶️ Usage

---

### 🟢 Step 1: Start Monitoring

```bash
python main.py
```

This will:

* start all monitors (process, network, device, screen)
* log events into SQLite DB
* evaluate risk using brain engine

👉 Let it run for **10–20 minutes**

---

### 🟡 Step 2: Train AI Model

Stop monitoring (Ctrl + C), then run:

```bash
python core/train_model.py
```

Output:

```
Training on X samples
Model trained and saved!
```

---

### 🔵 Step 3: Run with AI (optional integration)

After training, the system can:

* classify risk (rule-based)
* detect anomaly (ML)

Example output:

```
[START] STREAMING detected
Process: chrome.exe
[RISK] LOW
[AI] NORMAL
```

---

## 🧪 Generating Test Data (Safe Methods)

To simulate anomalies:

* Run apps from `Downloads` or `Temp`
* Use microphone + network (Meet/Discord)
* Screen share (Zoom/Meet)
* Run high CPU scripts
* Rename executables (e.g., fake `chrome.exe`)

---

## 🤖 Machine Learning Details

### Model: Isolation Forest

* Unsupervised learning
* Detects deviations from normal behavior

### Features Used:

* CPU usage
* Time (hour of execution)
* Path risk

---

## 🔐 Detection Logic

The system uses **correlation-based reasoning**:

Example:

```
mic + network + suspicious path → CRITICAL
screen + network → HIGH
mic only → MEDIUM
```

---

## 🚀 Future Enhancements

* 🔥 LLM + RAG integration
* 📊 Dashboard UI
* 🚨 Real-time alerts
* 🛑 Process blocking
* 🌐 Cross-platform support

---

## 💡 Key Highlights

* Behavior-based detection (not signature-based)
* Identity + behavior correlation
* Works with **no labeled data**
* Fully local (privacy-friendly)

---

## 📌 Resume Line

> Built an AI-powered host-based anomaly detection system that monitors system behavior and detects suspicious activities using rule-based intelligence and unsupervised machine learning.

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**.
It does not replace professional security tools.

---

## 👨‍💻 Author

Vedant Patil
Computer Engineering | AI & Systems Enthusiast

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
