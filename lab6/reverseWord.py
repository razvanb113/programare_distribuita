text = input("Introduceti o propozitie: ").split()
text_invers = ""

for i in range(len(text) - 1, -1, -1):
    text_invers += text[i] + " "

print(text_invers)
