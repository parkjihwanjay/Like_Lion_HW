import requests
import csv
from bs4 import BeautifulSoup
from book_processing import extracting

final_result = []

for i in range(8):
    book_html = requests.get(f"https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}")
    book_soup = BeautifulSoup(book_html.text, "html.parser")
    book_list_box = book_soup.find("ol",{"class": "basic"})
    print(book_list_box)
    book_list = book_list_box.find_all("li")

    final_result = final_result + extracting(book_list)



file = open("naver_books.csv", mode="w",encoding='utf-8', newline='')
writer = csv.writer(file)
writer.writerow(["title", "image_link", "detail_link","authoir", "publisher", "price"])

for book in final_result:
    row = []
    row.append(book['title'])
    row.append(book['price'])
    row.append(book['image_link'])
    row.append(book['detail_link'])
    row.append(book['author'])
    row.append(book['publihser'])
    row.append(book['price'])
    writer.writerow(row)

print("크롤링 끝!")