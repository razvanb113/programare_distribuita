documents = []
nr_documente = 0

def citireNumarDocumente():
    print("Introduceti numarul de documente pe care le veti introduce (siruri de caractere): ")
    while True:
        try:
            nr_documente = int(input())
            if nr_documente > 0:
                return nr_documente
            else:
                print("Introduceti un numar pozitiv!")
                continue
        except(ValueError):
            print("Introduceti un numar intreg!")
            continue

def citireDocumente(nr_documente):
    documents = []
    print("Introduceti documentele: ")
    for _ in range(nr_documente):
        documents.append(input())
    return documents

def inverted_index(documents):
    index = {}
    
    for i, document in enumerate(documents):
        words = document.split()
        
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(i)
    
    return index

nr_documente = citireNumarDocumente()
documents = citireDocumente(nr_documente)

result = inverted_index(documents)
print(result)