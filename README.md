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

⚠️  http://testsafebrowsing.appspot.com/s/malware.html → UNSAFE (Malware or Phishing detected)␣␣
✅ https://www.google.com → Safe  

---

## 🛠️Technologies Used

- Python 3
- re module for link extraction
- requests module for API communication
- Google Safe Browsing API

---

## 📚 What I Learned

- How to work with external APIs
- How to structure a request body in JSON
- How to extract URLs using regex
- How to handle errors with try/except
- How to parse JSON responses in Python

---

## 🌱 Why I Built This

As an 18-year-old self-learner, this is my first real-world project using an external API. I wanted to build something useful while learning about APIs, JSON, and automation with Python — and share it with others starting their journey.


---

## ✨ Future Ideas

- Save results to .txt or .csv
- GUI version using Tkinter
- Deploy as a browser extension

---

## 📫 Feedback & Support

Want to collaborate, give feedback, or just say hi?
- 📧 Email: neuralv.ai@gmail.com
- 📬 LinkedIn: https://www.linkedin.com/in/neural-vision-246281359/
- 🐦 Twitter(X): https://x.com/NeuralV_AI
