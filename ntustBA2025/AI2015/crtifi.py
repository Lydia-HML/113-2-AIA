import ssl
import certifi  # First, ensure the certifi library is installed by running: pip install certifi

ssl._create_default_https_context = ssl._create_unverified_context

print(certifi.where())  # 確保 SSL 憑證已更新

import yt_dlp

with yt_dlp.YoutubeDL() as ydl:
    info_dict = ydl.extract_info("https://www.youtube.com/watch?v=5u4xTa3LR2U", download=False)
    print(info_dict)




# 步驟 1：修復 SSL 憑證:
# 開 Terminal
# bash>/Applications/Python\ 3.9/Install\ Certificates.command
# 確認 python 版本：bash>python3 --version
# 另一個步驟 1：修復 SSL 憑證，若未安裝 certifi 則先執行: pip install certifi，然后: pip install --upgrade certifi




