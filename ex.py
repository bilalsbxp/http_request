import requests

#sebelum menjalankannya install requests melalui pip
#pip install requests


url = "https://utomp3.com/en"
headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 11; V2026 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.86 Mobile Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'cache-control': "max-age=0",
  'sec-ch-ua': "\"Chromium\";v=\"130\", \"Android WebView\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'upgrade-insecure-requests': "1",
  'dnt': "1",
  'x-requested-with': "mark.via.gp",
  'sec-fetch-site': "none",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'referer': "https://www.google.com/",
  'accept-language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=0, i"
}

response = requests.get(url, headers=headers)

print(response.text)
