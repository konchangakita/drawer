from bs4 import BeautifulSoup
import requests
import re

# URLからHTMLを取得
url = '{ダウンロード対象Webページ}'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#img_tag = soup.find_all('img')

# ダウンロード対象の画像のURLを特定
imgs = soup.find_all('img', src=re.compile('^https://img..*\.jpg'), width="300") # サンプル
print(len(imgs))

# 画像を1枚づつダウンロード
for img in imgs:
        print(img['src'])
        file_name = img['src'].split('/')[6] #img srcのURLからfile名を取得
        r = requests.get(img['src'])
        with open(str('./picture/')+str(file_name),'wb') as file:
                file.write(r.content)