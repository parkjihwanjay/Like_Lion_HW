import requests
import csv
from bs4 import BeautifulSoup
from book_processing import extracting

final_result = []

book_html = requests.get("https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page=1")
book_soup = BeautifulSoup(book_html.text, "html.parser")
book_list_box = book_soup.find("ol",{"class": "basic"})
book_list = book_list_box.find_all("li")

sample = book_list[11]

#print(extracting(book_list))
#print(sample.find("em",{"class":"price"}))
print(sample.find("em"))
print(sample)