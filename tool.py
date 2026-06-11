import subprocess

url = input("Nhap link: ").strip()
if not url.startswith(("http://", "https://")):
    url = "https://" + url
subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url, "-n", "com.android.chrome/com.google.android.apps.chrome.Main"])
print("Da mo Chrome: " + url)
