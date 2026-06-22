#movie Dictionary

movie = {
    "title": "inception",
    "director" : "Christopher Nolan",
    "year" : 2010,
    "rating" : 8.8
}
print(movie.keys())
print(movie.values())
print(movie.get("rating"))
print(movie.get("budget"))
movie.update({"budget":160, "rating":9.0})
print(movie)