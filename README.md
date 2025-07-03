# PhishShield
PhishShield is a modern web-based tool designed to detect phishing URLs with high accuracy and speed. It leverages a multi-layered approach, combining machine learning, heuristic analysis, and real-time threat intelligence from multiple security APIs.

# 🛡️ PhishShield: Multi-Layered Phishing URL Detection

**PhishShield** is a full-stack web application for real-time phishing URL detection. It combines machine learning, heuristic analysis, and multiple threat intelligence APIs to provide layered protection against phishing attacks.

---

## 🚀 Features

- 🧠 **Machine Learning Detection**  
  Trained XGBoost model (99% test accuracy) using the PhiUSIIL dataset and 9+ engineered URL features.

- 🧪 **Heuristic Analysis**  
  Rule-based checks for suspicious top-level domains, IP-based domains, long or obfuscated URLs, and more.

- 🌐 **Threat Intelligence APIs**  
  Integrates with:
  - Google Safe Browsing
  - VirusTotal
  - CheckPhish

- 🖥️ **User-Friendly Web Interface**  
  Flask-based UI for scanning URLs, showing:
  - Risk scores
  - Heuristic flags
  - ML verdicts
  - Threat intelligence results

- ☁️ **Cloud-Ready Deployment**  
  Easily deployable to **Google Cloud Run** or any **Docker-compatible** platform.

---

## 🗂 Project Structure

phishshield/
├── app.py # Flask main application
├── utils/
│ ├── scanner.py # Core scanning logic
│ ├── phish_model.pkl # Trained XGBoost model
│ └── tld_encoder.pkl # Encoded TLD transformer
├── requirements.txt
├── templates/
│ └── index.html # Web UI template

Obtain API keys from the following services:

Google Safe Browsing → Google Developers Console

VirusTotal → virustotal.com

CheckPhish → CheckPhish.io

🛠️ How It Works
PhishShield uses a multi-layered detection pipeline:

User submits a URL via the web interface.

Heuristic Analysis runs first, flagging risks based on rules (e.g., suspicious TLDs, IP-based domains).

Threat Intelligence APIs are queried in parallel:

Google Safe Browsing checks known malicious URLs.

VirusTotal aggregates results from dozens of antivirus vendors.

CheckPhish detects phishing using AI and global threat feeds.

Feature Extraction is performed on the URL to create a numerical vector.

The XGBoost ML model predicts phishing probability using the feature vector.

Results are combined:

Risk score is calculated based on heuristics, API flags, and ML confidence.

User Interface displays all findings clearly:

Which APIs flagged it

Heuristic warnings

ML verdict with confidence
