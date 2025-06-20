dogs = {'Fido':8, 'Sara':14, 'Matt':20, 'Fido':20}

dogs ['Sara']= 12

del(dogs['Sara'])

print(dogs)


words = ["Sus","Spange","Lie-Fi"]
definitions = ["Suspicious","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]


cool_dictionary = {}


for index in range(3):
    cool_dictionary[words[index]] = definitions[index]


print(cool_dictionary)