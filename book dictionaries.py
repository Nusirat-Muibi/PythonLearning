#BOOK STORE

book = {
    "title" : "The Alchemist",
    "author" : "Paulo Coelho",
    "price" : 15,
    "stock" : 30
}
print(book["title"])
print(book["author"])

book["price"] = 20
print(book["price"])
book["genre"] = "Fiction"
print(book["genre"])

del book["stock"]
print(book)

for key, value in book.items():
    print(key, ":", value)
print(book.keys())
print(book.values())
print(book.get("title"))
print(book.get("stock"))
book.update({"price": 20, "stock": 50})
print(book)

