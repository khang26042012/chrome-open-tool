import subprocess
import urllib.request
import time
import os

KEYWORDS = ["TAC GIA", "NGAY DANG", "LUOT XEM", "GETCODE"]

os.environ["RISH_APPLICATION_ID"] = "com.termux"
RISH = os.path.expanduser("~/rish")

url = input("Nhap link: ").strip()
if not url.startswith(("http://", "https://")):
    url = "https://" + url

print("Dang kiem tra trang web...")
try:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode("utf-8", errors="ignore").upper()
    found = any(k.upper() in html for k in KEYWORDS)
    if found:
        print("OK: Trang hop le. Dang mo Chrome...")
        subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url, "-n", "com.android.chrome/com.google.android.apps.chrome.Main"])
        print("Doi 5 giay cho trang load...")
        time.sleep(5)
        print("Dang cuon xuong...")
        for i in range(4):
            subprocess.run([RISH, "-c", "input swipe 540 1600 540 900 800"])
            time.sleep(0.5)
        print("Xong! Kiem tra man hinh xem anh da hien chua.")
    else:
        print("LOI: Trang khong co thong tin hop le")
except Exception as e:
    print("LOI: " + str(e))
