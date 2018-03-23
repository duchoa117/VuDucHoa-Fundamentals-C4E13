cout = 0
import pyexcel
excel = []
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
    # print(take[1])
    for t in take:
        # print(t.string)
        # print('***********************')
        excel.append(t.string)
l = len(excel)//6
for i in range(l):
    records_content.append({
                'Tittle': excel[6*i],
                'Quý 4-2016': excel[6*i+1],
                'Quý 1-2017': excel[6*i+2],
                'Quý 2-2017': excel[6*i+3],
                'Quý 3-2017': excel[6*i+4],
                'Tăng trưởng' :excel[6*i+5],

    })



pyexcel.save_as(records=records_content, dest_file_name='bai2_1.xlsx')
