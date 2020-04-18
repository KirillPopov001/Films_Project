with open('input.txt', 'r', encoding="utf-8") as f:
    txt = f.readlines()


for i in range(0, len(txt)):
    txt[i] = str(txt[i]).split(": ")

films = {}

for i in txt:
    films[i[0]] = i[1]


a = input()
b = input()

film1 = films[a]        #список актеров, участвующих в фильме №1
film2 = films[b]        #список актеров, участвующих в фильме №2

film1, film2 = film1.replace("\n", "").split(", "), film2.replace("\n", "").split(", ") #убираются запятые и пробелы из
                                                                                        #списков

film1 = set(film1)
film2 = set(film2)


f = 1
print("В фильмах снимались: ", end = "")
for j in (film1 | film2):
    if f != len(film1 | film2):
        print(j, end=", ")
    if f == len(film1 | film2):
        print(j)
    f += 1


f = 1
print("Актёр/актёры, принимающий/принимающие участие в обоих фильмах: ", end = "")
if len(film1 & film2) == 0:
    print("Таких фильмов нет.")
else:
    for j in (film1 & film2):
        if f != len(film1 & film2):
            print(j, end=", ")
        if f == len(film1 & film2):
            print(j)
        f += 1


print("Актёр/актёры, принимающий/принимающие участие только в первом фильме: ", end = "")
f = 1
for i in range(len(film1 - film2)):
    for j in (film1 - film2):
        if f != len(film1 - film2):
            print(j, end=", ")
        if f == len(film1 - film2):
            print(j)
        f += 1
    break


actorC = set()
actorD = set()


c = input()
d = input()

for i in films:                            #В множества добавляются фильмы, в которых участвовали актёры
    films[i] = films[i].split(", ")
    for j in films[i]:
        if j == c:
            actorC.add(i)
        if j == d:
            actorD.add(i)


print("Фильмы, в которых снимались актёры: ", end="")
f = 1
for j in (actorC | actorD):
    if f != len(actorC | actorD):
        print(j, end=", ")
    if f == len(actorC | actorD):
        print(j)
    f += 1

print("Фильмы, в которых снимались оба актёра: ", end = "")
f = 1

if len(actorC & actorD) == 0:
    print("Таких фильмов нет.")
else:
    for j in (actorC & actorD):
        if f != len(actorC & actorD):
            print(j, end=", ")
        if f == len(actorC & actorD):
            print(j)
        f += 1


print("Фильмы, в которых снимался первый актёр, но не снимался второй: ", end="")
f = 1
for j in (actorC - actorD):
    if f != len(actorC - actorD):
        print(j, end=", ")
    if f == len(actorC - actorD):
        print(j)
    f += 1
