import subprocess
import urllib.request
import urllib.error

KEYWORDS = ["TAC GIA", "TÁC GIẢ", "NGAY DANG", "NGÀY ĐĂNG", "LUOT XEM", "LƯỢT XEM", "GETCODE"]

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
        print("OK: Tim thay thong tin hop le. Dang mo Chrome...")
        subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url, "-n", "com.android.chrome/com.google.android.apps.chrome.Main"])
    else:
        print("LOI: Trang web khong co thong tin can thiet (thieu TÁC GIẢ / NGÀY ĐĂNG / LƯỢT XEM / GETCODE)")
except urllib.error.URLError as e:
    print("LOI: Khong the truy cap link - " + str(e))
except Exception as e:
    print("LOI: " + str(e))
