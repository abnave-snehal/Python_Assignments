import os
import time
import shutil
import sys
import zipfile
import hashlib
import schedule
import smtplib
from email.message import EmailMessage


# ---------------- EMAIL CONFIG ----------------
SENDER_EMAIL = "aalegaonkar712@gmail.com"
APP_PASSWORD = "usqf hulf ncfd zicl"   # Gmail app password
RECEIVER_EMAIL = "abnave712@gmail.com"
# ---------------------------------------------


# ---------------- LOGGING ----------------
def writeLog(message):
    os.makedirs("Logs", exist_ok=True)
    log_name = time.strftime("Logs/Backup_%Y-%m-%d.log")

    with open(log_name, "a") as f:
        f.write(message + "\n")


def getTodayLogFile():
    return time.strftime("Logs/Backup_%Y-%m-%d.log")


# ---------------- HASH ----------------
def calculateHash(path):
    hobj = hashlib.md5()

    with open(path, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            hobj.update(data)

    return hobj.hexdigest()


# ---------------- BACKUP COPY ----------------
def backupFiles(source, destination):
    copied = []

    os.makedirs(destination, exist_ok=True)

    for root, dirs, files in os.walk(source):
        for file in files:
            src = os.path.join(root, file)
            rel = os.path.relpath(src, source)
            dst = os.path.join(destination, rel)

            os.makedirs(os.path.dirname(dst), exist_ok=True)

            if (not os.path.exists(dst)) or (
                calculateHash(src) != calculateHash(dst)
            ):
                shutil.copy2(src, dst)
                copied.append(rel)
                writeLog("Copied: " + rel)

    return copied


# ---------------- ZIP ----------------
def makeZip(folder):
    ts = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + ts + ".zip"

    z = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            full = os.path.join(root, file)
            rel = os.path.relpath(full, folder)
            z.write(full, rel)

    z.close()
    return zip_name


# ---------------- EMAIL ----------------
def sendBackupMail(zip_path):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = "Backup Completed Successfully"

    body = f"""
Backup completed successfully.

Zip file: {zip_path}

Attachments:
- Zip backup
- Log file
"""
    msg.set_content(body)

    # attach zip
    if os.path.exists(zip_path):
        with open(zip_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="zip",
                filename=os.path.basename(zip_path),
            )

    # attach log
    log_file = getTodayLogFile()
    if os.path.exists(log_file):
        with open(log_file, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="text",
                subtype="plain",
                filename=os.path.basename(log_file),
            )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

    print("Email sent successfully")


# ---------------- BACKUP JOB ----------------
def marvellousDataShieldStart(source="Data"):
    border = "_" * 50

    print(border)
    print("Backup started:", time.ctime())
    print(border)

    writeLog("Backup started: " + time.ctime())

    backup_folder = "MarvellousBackup"

    files = backupFiles(source, backup_folder)
    zip_name = makeZip(backup_folder)

    writeLog("Zip created: " + zip_name)
    writeLog("Files copied: " + str(len(files)))
    writeLog("Backup finished")

    print("Backup complete")
    print("Zip:", zip_name)
    print("Files copied:", len(files))
    print(border)

    # send email
    sendBackupMail(zip_name)


# ---------------- RESTORE ----------------
def restoreBackup(zipName, destination):
    if not os.path.exists(zipName):
        writeLog("ERROR: Zip file not found: " + zipName)
        print("Zip file not found")
        return

    os.makedirs(destination, exist_ok=True)

    writeLog("Restore start: " + time.ctime())
    writeLog("Zip: " + zipName)
    writeLog("Destination: " + destination)

    z = zipfile.ZipFile(zipName, "r")

    for name in z.namelist():
        z.extract(name, destination)
        writeLog("Extracted: " + name)

    z.close()

    writeLog("Restore completed")
    print("Restore completed successfully")


# ---------------- MAIN ----------------
def main():
    border = "_" * 50
    print(border)
    print("------ Data Shield System ------")
    print(border)

    # restore mode
    if len(sys.argv) == 4 and sys.argv[1] == "--restore":
        restoreBackup(sys.argv[2], sys.argv[3])
        return

    # help
    if len(sys.argv) == 2 and sys.argv[1].lower() == "--h":
        print("Script features:")
        print("• Periodic backup")
        print("• Incremental copy")
        print("• Zip archive")
        print("• Email notification")
        print("• Restore option")
        return

    if len(sys.argv) == 2 and sys.argv[1].lower() == "--u":
        print("Usage:")
        print("Backup scheduler:")
        print("  Script.py <minutes> <source_folder>")
        print("Restore:")
        print("  Script.py --restore <zipfile> <destination>")
        return

    # scheduler mode
    if len(sys.argv) == 3:
        minutes = int(sys.argv[1])
        source = sys.argv[2]

        schedule.every(minutes).minutes.do(
            marvellousDataShieldStart, source
        )

        print("Scheduler started. Interval:", minutes, "minutes")
        print("Press Ctrl+C to stop")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid arguments. Use --h or --u")


if __name__ == "__main__":
    main()
