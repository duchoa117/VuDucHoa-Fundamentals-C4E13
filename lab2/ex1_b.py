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
    "Name" : a_s.string.upper(),
    "Artist" : a_a.string,
    "Link" : a_s['href']})
# print(excel_song)

name = input("The song's name: ").upper()
for infor_song in excel_song:
    if infor_song["Name"]==name:
        print('Name:',name)
        print('Artist:',infor_song["Artist"])
        # print('Linl:',infor_song["Link"])

        while True:
            choice = input(('Is this the song you want?(Y/N/B) ')).upper()
        # Trường hợp có 2 bài giống tên khác người thực hiện.
        # while True:
            if choice == 'Y':
                from youtube_dl import YoutubeDL
                options = {
                    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
                    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
                    'format': 'bestaudio/audio'
                }
                dl = YoutubeDL(options)
                dl.download([name])
                break
            elif choice == 'N':
                continue
            elif choice == 'B':
                break

            else:
                print("Wrong enter")
