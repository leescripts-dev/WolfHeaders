<div align="center">

<pre>
██╗    ██╗ ██████╗ ██╗     ███████╗██╗  ██╗███████╗ █████╗ ██████╗ ███████╗██████╗ ███████╗
██║    ██║██╔═══██╗██║     ██╔════╝██║  ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝
██║ █╗ ██║██║   ██║██║     █████╗  ███████║█████╗  ███████║██║  ██║█████╗  ██████╔╝███████╗
██║███╗██║██║   ██║██║     ██╔══╝  ██╔══██║██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗╚════██║
╚███╔███╔╝╚██████╔╝███████╗██║     ██║  ██║███████╗██║  ██║██████╔╝███████╗██║  ██║███████║
 ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝
</pre>

# 🛡️ WolfHeaders

### HTTP Security Header Analyzer

Analyze • Score • Secure

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Version](https://img.shields.io/badge/Version-v1.0.0-success)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

## Overview

WolfHeaders is a lightweight Python CLI tool that analyzes a website's HTTP security headers and provides a simple security score along with recommendations.

It helps developers and security enthusiasts quickly identify missing HTTP security headers that improve browser-side security.

---

## Features

- Analyze HTTP response headers
- Detect missing security headers
- Security score calculation
- Rich terminal interface
- Simple recommendations
- Lightweight CLI
- Modular Python architecture

---

## How It Works

```text
User
 │
 ▼
wolfheaders example.com
 │
 ▼
Validate URL
 │
 ▼
HTTP Request
 │
 ▼
Receive Headers
 │
 ▼
Analyze Security Headers
 │
 ▼
Calculate Score
 │
 ▼
Generate Recommendations
 │
 ▼
Display Results
```

---

## Security Headers Checked

- Content-Security-Policy
- Strict-Transport-Security
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy
- Cross-Origin-Embedder-Policy
- Cross-Origin-Opener-Policy
- Cross-Origin-Resource-Policy

---

## Installation

Clone the repository

```bash
git clone https://github.com/leescripts-dev/WolfHeaders.git

cd WolfHeaders
```

Create a virtual environment

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install WolfHeaders

```bash
pip install -e .
```

---

## Usage

Basic Scan

```bash
wolfheaders example.com
```

With HTTPS

```bash
wolfheaders https://example.com
```

Help

```bash
wolfheaders -h
```

Version

```bash
wolfheaders --version
```

---

## Example Output

```text
Security Score: 7/9

✓ Content-Security-Policy
✓ Strict-Transport-Security
✓ X-Frame-Options
✗ Permissions-Policy
✗ Referrer-Policy

Recommendations

• Add Permissions-Policy
• Add Referrer-Policy
```

---

## Project Structure

```text
WolfHeaders/
│
├── wolfheaders.py
├── analyzer.py
├── scorer.py
├── banner.py
│
├── requirements.txt
├── setup.py
├── README.md
├── LICENSE
└── screenshots/
```

---

## Screenshots

### Banner

<p align="center">
<img src="screenshots/banner.png" width="900">
</p>

---

### Security Header Analysis

<p align="center">
<img src="screenshots/results.png" width="900">
</p>

---

## Technologies Used

- Python
- Requests
- Rich

---

## Roadmap

- JSON Export
- HTML Reports
- HTTP/2 Detection
- TLS Information
- Cookie Security Checks
- CSP Evaluation
- Header Severity Ratings

---

## Disclaimer

This project is intended for educational purposes and authorized security testing only.

---

## License

MIT License

---

<div align="center">

Built with Python 🐍

**Lee**

</div>