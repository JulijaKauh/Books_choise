
books = [["mystery", "The Paris Apartment"],
         ["thriller", "Seven Days"],
         [ "fiction", "It Ends with Us"],
         ["suspense", "The Huntress"],
         ["crime", "A Good Girl's Guide to Murder"]]

genre = input("What genre do  you want  to read? ")
for i in books:
    if i[0] == genre:
        print('Genre: ' + genre + '.' + ' Book: ' + i[1] + '.')
