# 📧 Human Email Sender Simulator - Red Team Tool

![Red Team](https://img.shields.io/badge/Red%20Team-Tool-critical?style=flat-square&logo=apache)

A tool designed to simulate human-like email behavior for use in advanced social engineering campaigns, such as **QR phishing**, **APT simulations**, and **targeted Red Team engagements**.

This tool aims to improve deliverability and avoid detection by spam filters through **evasion techniques**, such as:
- Injection of invisible characters in subject and body.
- Randomized and configurable sending delays (mimicking human timing).
- HTML email support with optional embedded images.

> 🔒 Passwords are never stored or logged — inputs are used only during the current session.

---

## 🚀 Features

- ✅ Sends emails with configurable subject, body, and embedded image (optional).
- ✅ Reads target recipients from `.txt` files (one email per line).
- ✅ Includes invisible Unicode characters randomly for evasion.
- ✅ Simulates human behavior via randomized time delays.
- ✅ Logs each sent or failed email with timestamp.
- ✅ Works with any SMTP provider supporting TLS login (e.g. Gmail, Hostinger, Outlook, etc.).

---

## 📁 Input Requirements

### 1. Recipients List

Create a text file in the working directory, for example:

```txt
recipients.txt
```

Contents:

```
alice@example.com
bob@example.org
charlie@example.net
```

### 2. Optional Embedded Image

You can embed an image (e.g., a QR code or branding asset) into the HTML body of the email. Only `.png` images in the current folder will be detected.

---

## ⚙️ Installation

1. **Run the tool**:
   ```bash
   python email_sender.py
   ```

---

## 📦 Dependencies

Install via `pip install -r requirements.txt`. The tool uses:

- `colorama`
- `pytz`

These are lightweight libraries used for colored output and timezone handling.

---

## 🧪 Use Case Examples

### QR Phishing Campaign

Simulate a fake promotion with an embedded QR code and custom HTML body, delayed sending, and evasion via invisible characters.

### APT Red Team Simulation

Send realistic, delayed, human-like phishing emails during a long-running campaign.

---

## 📝 Logs

Each execution generates a log file like:

```
logs_campaign_20250718_180429.log
```

It contains the timestamp, status (SENT/FAIL), and recipient address.

---

## ⚠️ Disclaimer

This tool is intended for educational and authorized Red Team use only. Use it only in environments where you have explicit permission to conduct phishing simulations or social engineering exercises.

Unauthorized use of this tool may violate laws or ethical boundaries.

---

## 👨‍💻 Author

Developed by **C0mm4nd1** - Red Teamer & Offensive Security Consultant

