
books = [["mystery", "The Paris Apartment", "aaa", "bbb", "ccc", "ddd", "eee"],
         ["thriller", "Seven Days"],
         [ "fiction", "It Ends with Us"],
         ["suspense", "The Huntress"],
         ["crime", "A Good Girl's Guide to Murder"]]

print("What genre do  you want  to read?")
genre = input()
for i in books:
    if i[1] == genre:
        print('Genre: ' + genre + '.' + ' Book: ' + i[0] + '.')
