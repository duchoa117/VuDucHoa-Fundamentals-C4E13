cout = 0
kbietghibiennao = ['tittle',
'Quý 4-2016',
'Quý 1-2017',
'Quý 2-2017',
'Quý 3-2017',
'Tăng trưởng']
import pyexcel
records_content = []
from urllib.request import urlopen
url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
html_content = urlopen(url).read()
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content,'html.parser')
div = soup.find('div',style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
rows_list = div.find_all('tr')
for r in rows_list:
    take = r.find_all('td','b_r_c')
    if len(take) == 0 :
        continue
    excel = {}
    for i in range(6):
        excel[kbietghibiennao[i]]=take[i].string
        # print(excel)



        # kbietghibiennao[i]
    records_content.append(excel)

    # print(take[1])

pyexcel.save_as(records = records_content,dest_file_name='2_2.xlsx')
