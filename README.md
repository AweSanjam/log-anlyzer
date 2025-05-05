# 🛠️ GPT-Powered Log Analyzer + Email Alerts

This is a **smart log analysis tool** built in Python that scans system/server logs, extracts warnings and errors, and uses **OpenAI's GPT API** to summarize and explain them in plain English.  
It also emails the report automatically — and is designed to be cloud-automated or expanded with a web interface.

---

## 🔧 Features

- 📜 Reads and parses log files (e.g., system, app, or simulated logs)
- 🧠 Uses GPT-4 or GPT-3.5 to summarize and suggest fixes
- 📬 Sends the results via email using Gmail SMTP
- 💾 Saves the summary as a `report.txt` file
- ☁️ Built to be scheduled using Task Scheduler, cron, or cloud services (e.g., AWS Lambda)
- 🌐 Can be adapted to serve as a backend for a web-based log monitoring tool

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/AweSanjam/log-analyzer.git
cd log-analyzer
```

### 2. Install dependencies

```bash
pip install openai
```

> Optional: If you're using `.env` for secrets, install dotenv:

```bash
pip install python-dotenv
```

### 3. Prepare your environment

#### Option A: Use environment variables (recommended)

```bash
$env:OPENAI_API_KEY="your-openai-key"
$env:SENDER_EMAIL="yourgmail@gmail.com"
$env:EMAIL_APP_PASSWORD="your-app-password"
$env:TO_EMAIL="recipient@example.com"
```

#### Option B: Use a `.env` file

```env
OPENAI_API_KEY=your-openai-key
SENDER_EMAIL=yourgmail@gmail.com
EMAIL_APP_PASSWORD=your-app-password
TO_EMAIL=recipient@example.com
```

And load it in the script using:

```python
from dotenv import load_dotenv
load_dotenv()
```

### 4. Run the analyzer

```bash
python log_analyzer.py
```

You’ll get a printed summary, an email (if configured), and a saved `report.txt`.

---

## 📁 Project Structure

```
├── log_analyzer.py     # Main script
├── sample.log          # Example log file
├── .env                # API keys & credentials (not pushed)
```

---

## 🧠 Example Output

From this log:

```
[ERROR] Failed to bind to port 80
[WARNING] Disk usage at 95%
[CRITICAL] Memory leak detected in process
```

GPT Summary:
> "The server failed to start due to a port conflict. Disk space is critically low, and a memory leak was detected. You should check running services, clear disk space, and investigate the memory usage of process IDs."

---

## ☁️ Cloud & Web Potential

- **Cloud Automation**: Easily deploy on AWS Lambda, Azure Functions, or PythonAnywhere to run on a schedule
- **Web Support**: The output can be integrated into a Flask or React dashboard for real-time log monitoring
- **DevOps Support**: Integrate with monitoring tools or Slack/email notifications

---

## 📜 License

MIT — Free to use, modify, and deploy. Just don't let it take your job... yet 😏

---

Want help building the web interface next? Or converting this into a Lambda function?
