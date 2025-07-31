# SafeLinker
A Python tool that extracts **links from any text** and checks if they're safe using Google's Safe Browsing API.


This beginner-friendly Python tool takes **any text input** (like emails, social media posts, or notes), extracts **all URLs**, and checks whether they are **safe or malicious** using the [Google Safe Browsing API](https://developers.google.com/safe-browsing).

---

## 🚀 Features

- 🔍 Extracts all links (http, https, www) from plain text
- 🛡️ Verifies link safety (detects malware, phishing, etc.)
- ✅ Shows whether links are safe or unsafe
- 📦 Uses official Google Safe Browsing API
- 🧠 Designed for beginners learning APIs & automation

---

## 📷 Demo

Paste your text (it can have multiple links):
Check this: http://testsafebrowsing.appspot.com/s/malware.html and this one: https://www.google.com

Links found and their safety status:

⚠️  http://testsafebrowsing.appspot.com/s/malware.html → UNSAFE (Malware or Phishing detected)
✅ https://www.google.com → Safe

---

## 🧑‍💻 Setup Instructions

1. **Clone this repo**
   ```bash
   git clone https://github.com/yourusername/link-safety-checker.git
   cd link-safety-checker

2. **Install dependencies**
    pip install requests

3. **Get a free Google Safe Browsing API key**
    Go to: Google API Console
    Create a project → Enable "Safe Browsing API" → Create API Key

4. **Add your API key to the code**
     Replace this line : 

