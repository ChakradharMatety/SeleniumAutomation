squares =[]
for i in range(1,11):
    squares.append(i**2)
print(squares)

squares2 = [i**2 for i in range(1,11)]
print(squares2)

movies = ['Annamalai','Andharivadu','BluffMaster','ChandraMukhi','Chiruta','DonBosco','Entheeran','Fun&Frustration']
amovies = []

for title in movies:
    if title.startswith('A'):
        amovies.append(title)
print(amovies)

cmovies = [title for title in movies if title.startswith('C')]
print(cmovies)


list=[2,3,4]
print([i*2 for i in list])
print(5*list)