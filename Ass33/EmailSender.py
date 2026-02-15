import os
import sys
import time
import psutil
import smtplib
from email.message import EmailMessage
from datetime import datetime

# ---------------- EMAIL CONFIG ----------------
SENDER_EMAIL = "aalegaonkar712@gmail.com"
APP_PASSWORD = "usqf hulf ncfd zicl"   # Gmail app password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
# ----------------------------------------------


def get_process_summary():
    procs = []

    for p in psutil.process_iter(['pid','name','cpu_percent','memory_percent','num_threads']):
        try:
            info = p.info
            info["open_files"] = len(p.open_files())
            procs.append(info)
        except:
            continue

    total = len(procs)

    top_cpu = sorted(procs, key=lambda x: x['cpu_percent'], reverse=True)[:5]
    top_mem = sorted(procs, key=lambda x: x['memory_percent'], reverse=True)[:5]
    top_threads = sorted(procs, key=lambda x: x['num_threads'], reverse=True)[:5]
    top_files = sorted(procs, key=lambda x: x['open_files'], reverse=True)[:5]

    return total, top_cpu, top_mem, top_threads, top_files

def format_table(title, plist):
    text = f"\n--- {title} ---\n"
    for p in plist:
        text += (
            f"PID:{p['pid']} | "
            f"{p['name']} | "
            f"CPU:{p.get('cpu_percent',0):.2f}% | "
            f"MEM:{p.get('memory_percent',0):.2f}% | "
            f"Threads:{p.get('num_threads',0)} | "
            f"OpenFiles:{p.get('open_files',0)}\n"
        )
    return text

def build_report():
    total, cpu, mem, threads, files = get_process_summary()

    body = f"""
System Report — {datetime.now()}

Total Processes: {total}
"""

    body += format_table("Top CPU Usage Processes", cpu)
    body += format_table("Top Memory Usage Processes", mem)
    body += format_table("Top Thread Count Processes", threads)
    body += format_table("Top Open File Processes", files)

    return body


def latest_log_file(log_folder):
    files = [os.path.join(log_folder, f) for f in os.listdir(log_folder)]
    files = [f for f in files if os.path.isfile(f)]
    if not files:
        return None
    return max(files, key=os.path.getmtime)


def send_mail(receiver, subject, body, attachment_path=None):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    if attachment_path:
        with open(attachment_path, "rb") as f:
            data = f.read()
        fname = os.path.basename(attachment_path)

        msg.add_attachment(
            data,
            maintype="application",
            subtype="octet-stream",
            filename=fname
        )

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

    print("Mail sent successfully")


def main():
    if len(sys.argv) != 4:
        print("Usage: PlatformSurveillance.py <log_folder> <receiver_email> <interval_minutes>")
        return

    log_folder = sys.argv[1]
    receiver = sys.argv[2]
    interval = int(sys.argv[3])

    while True:
        print("Generating report...")
        report = build_report()
        logfile = latest_log_file(log_folder)

        send_mail(
            receiver,
            subject="Periodic System Report",
            body=report,
            attachment_path=logfile
        )

        print(f"Sleeping {interval} minutes...")
        time.sleep(interval * 60)


if __name__ == "__main__":
    main()
