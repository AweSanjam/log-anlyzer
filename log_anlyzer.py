import re
import openai
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# === CONFIG ===
openai.api_key = os.getenv("OPENAI_API_KEY")  # Or replace with your API key string
LOG_FILE = "sample.log"
GPT_MODEL = "gpt-4"  # or "gpt-3.5-turbo"
REPORT_FILE = "report.txt"

# Email config (replace or use env vars)
SENDER_EMAIL = os.getenv("SENDER_EMAIL") or "yourgmail@gmail.com"
APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD") or "your-app-password"
TO_EMAIL = os.getenv("TO_EMAIL") or "recipient@example.com"

# === PARSE LOG FILE ===
def extract_errors(log_path):
    error_lines = []
    with open(log_path, 'r') as f:
        for line in f:
            if re.search(r"\b(ERROR|WARNING|CRITICAL)\b", line, re.IGNORECASE):
                error_lines.append(line.strip())
    return error_lines

# === GPT EXPLANATION ===
def gpt_explain_issues(errors):
    if not errors:
        return "✅ No critical issues found in the log."

    prompt = f"""You are an expert IT support engineer. Analyze the following system log entries and explain the issues in plain English. Suggest solutions if possible.

Logs:
{chr(10).join(errors)}

Response:"""

    try:
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT Error: {e}"

# === EMAIL REPORT ===
def send_email_report(to_email, subject, body, sender_email, app_password):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
        print("📬 Email sent successfully!")
    except Exception as e:
        print(f"❌ Email failed: {e}")

# === MAIN ===
def main():
    print("📄 Reading log file...")
    errors = extract_errors(LOG_FILE)
    print(f"⚠️ Found {len(errors)} issue(s).")

    print("\n🤖 Generating GPT summary...")
    summary = gpt_explain_issues(errors)

    print("\n📋 Summary:\n")
    print(summary)

    with open(REPORT_FILE, "w") as f:
        f.write(summary)
        print(f"\n✅ Summary saved to {REPORT_FILE}")

    # Send email
    send_email_report(
        to_email=TO_EMAIL,
        subject="🛠️ Log Analyzer Report",
        body=summary,
        sender_email=SENDER_EMAIL,
        app_password=APP_PASSWORD
    )

if __name__ == "__main__":
    main()
