import requests
import csv
from bs4 import BeautifulSoup
#from corona_hospital import extracting_corona

final_result = []

corona_html= requests.get("https://www.mohw.go.kr/react/popup_200128_3.html")
corona_html.encoding=("utf-8")
corona_soup = BeautifulSoup(corona_html.text, "html.parser")
corona_list_box = corona_soup.find("tbody",{"class":"tb_center"}) 
corona_list_hosp = corona_list_box.find_all("tr")
# #print(corona_list_box)
# print(corona_list_hosp[0].contents)
# print(corona_list_hosp[0].contents[3].text)


entire_result = []
for hosp in corona_list_hosp:
    hosp = hosp.contents
    city = hosp[1].text
    district = hosp[2].text
    title = hosp[3].text
    number = hosp[4].text

    hosp_info={
        'city':city,
        'district':district,
        'title':title,
        'number':number
    }
    entire_result.append(hosp_info)

file = open("corona_hospital.csv", mode="w", encoding='euc-kr',newline='')
writer = csv.writer(file)
writer.writerow(["city", "district", "title","number"])

for hos_row in entire_result:
    row = []
    row.append(hos_row['city'])
    row.append(hos_row['district'])
    row.append(hos_row['title'])
    row.append(hos_row['number'])
    writer.writerow(row)

print("Crawling is over")
