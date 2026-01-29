def count_words_in_file(filename):
    file = open(filename, "r")
    
    text = file.read()
    file.close()
    
    count = 0
    
    words = text.split()
    for _ in range(len(words)):
        count += 1
    
    return count

result = count_words_in_file("countWordInFile.txt")
print("Numarul de cuvinte din fisier este de: ", result)