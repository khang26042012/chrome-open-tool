import subprocess

  def mo_chrome(url):
      if not url.startswith(('http://', 'https://')):
          url = 'https://' + url
      subprocess.run([
          'am', 'start',
          '-a', 'android.intent.action.VIEW',
          '-d', url,
          '-n', 'com.android.chrome/com.google.android.apps.chrome.Main'
      ])
      print(f"Da mo Chrome: {url}")

  url = input("Nhap link: ").strip()
  mo_chrome(url)
  