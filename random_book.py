from random import choice

books = [['The Paris Apartment', 'mystery'],
         ['Seven Days', 'thriller'],
         ['It Ends with Us', 'fiction'],
         ['The Huntress', 'suspense'],
         ['A Good Girls Guide to Murder', 'crime']]

print a random book from books
print("What genre do you like to read?")
genre = input()
for i in books:
    if i[1] == genre:
        print('Genre: ' + genre + '.' + ' Book: ' + i[0] + '.')
