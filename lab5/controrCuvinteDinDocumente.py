def citeste_numar_documente():
    print("Introduceti numarul de documente (siruri de caractere):")
    while True:
        try:
            n = int(input())
            if n > 0:
                return n
            print("Introduceti un numar pozitiv!")
        except ValueError:
            print("Introduceti un numar intreg!")


def citeste_documente(n):
    print("Introduceti documentele:")
    documente = []
    for _ in range(n):
        documente.append(input())
    return documente


def creeaza_index_invers(documente):
    index = {}

    for idx, document in enumerate(documente):
        for cuvant in document.split():
            if cuvant not in index:
                index[cuvant] = set()
            index[cuvant].add(idx)

    return index


numar_documente = citeste_numar_documente()
lista_documente = citeste_documente(numar_documente)

index_invers = creeaza_index_invers(lista_documente)
print(index_invers)
