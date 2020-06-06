movies = {1: "pulpfiction",
          2: "Titanic",
          3: "Jurassicpark",
          4: "KIllbill"

}
# find if the key is present
# to add a new key value into the dictionary
movies[5]= "Dillagi"
print(4 in movies)
print(5 in movies)
# get method in dictionary
print(movies.get(1))
print(movies.get(5,"movie not found"))
print(movies[1])
print(movies[2])
print(movies.get(3))
# loop
for x in movies:
    print(movies)
for x in movies:
    print(movies[x])
# length
print(len(movies))
# check for the key
if 1 in movies:
    print("Yes,'pulpfiction' is in the dictionaries")
print(movies)
# To remove a key and value from dictionary
movies.pop(5)
print(movies)
movies.popitem()
print(movies)
#copy a dictionary
newmovies= movies.copy()
del movies[3]
print(movies)
print(newmovies)