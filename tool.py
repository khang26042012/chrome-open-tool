import subprocess
import urllib.request
import urllib.error

KEYWORDS = ["TAC GIA", "TAC GIA", "NGAY DANG", "NGAY DANG", "LUOT XEM", "LUOT XEM", "GETCODE"]

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
        print("OK: Dang mo Chrome...")
        subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url, "-n", "com.android.chrome/com.google.android.apps.chrome.Main"])
    else:
        print("LOI: Trang khong co thong tin hop le")
except Exception as e:
    print("LOI: " + str(e))
