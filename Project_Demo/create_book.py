import requests

url   = 'https://localhost:5000/api/v1/books'

book_obj = {'isbn':'5555', 'title':'book 55', 'author': 'me55'}

x = requests.post(url  , data = book_obj)

print(x.text)