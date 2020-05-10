def extracting(book_info):
    result = []
    
    for book in book_info:
        title = book.find("dt").find("a").text
        print(title)
        image_link = book.find("img")["src"]
        detail_link = book.find("a", {"class": "N=a:bta.thumb"})["href"]
        author = book.find("a", {"class": "txt_name N=a:bta.author"}).text
        publisher = book.find("a",{"class": "N=a:bta.publisher"}).text
        semi_price = book.find("em", {"class":"price"})
        if semi_price == None:
            price= '없음'
        else :
            price = semi_price.string
        book_info ={
            'title': title,
            'image_link': image_link,
            'detail_link': detail_link,
            'author':author,
            'publisher': publisher,
            "price": price

        }
        result.append(book_info)

    return result