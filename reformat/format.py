import requests
from bs4 import BeautifulSoup

url = 'https://intrigue.dating/interesnoe/500-slov-dlya-igry-v-krokodila-spisok-smeshnyh-slojnyh-i-vzroslyh/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)

words = soup.find_all('ol')
print(words)

s = ''

for i in words:
    name = i.find('li').text
    print(name)
    
# #     try:
# #         disc = i.find('p', class_='item-compact__tagline').text
# #         s += f'{name} ({disc})\n'
# #     except:
# #         s += f'{name}\n'
    
    
# # with open('D:/!python/celebs_and_activity/reformat/output.txt', 'r+', encoding='utf-8') as f:
# #     f.write(s)