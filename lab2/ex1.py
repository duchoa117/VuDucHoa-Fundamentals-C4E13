

import pyexcel
from urllib.request import urlopen
url = 'https://www.apple.com/itunes/charts/songs/'
html_content = urlopen(url).read().decode('utf8')
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content,'html.parser')
# html_file = open('itunestosong.html','wb')
# html_file.write(html_content)
# html_file.close()
section = soup.find('section','section chart-grid')
# print(section)
li_list_song = section.find_all('li')
# print(li_list_song)
excel_song = []
# list_song = ['Name','Artist', 'Link' ]
for li in li_list_song:
    a_s=li.h3.a
    a_a=li.h4.a
    # print(a_s.string)
    # print(a_a.string)
    # print(a_s['href'])
    excel_song.append({
    "Name" : a_s.string,
    "Artist" : a_a.string,
    "Link" : a_s['href']})
    # print(infor_song)
# print(excel_song)
pyexcel.save_as(records=excel_song,dest_file_name='infor_topsong.xlsx')
