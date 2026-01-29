print("Acest program va comprima un text folosind Run-Length Encoding")

def run_length_encoding(text):
    if len(text) == 0:
        return ""
    
    result = ""
    i = 0
    
    while i < len(text):
        current_char = text[i]
        count = 1
        
        # Numără caracterele consecutive identice
        while i + count < len(text) and text[i + count] == current_char:
            count += 1
        
        result += current_char + str(count)
        i += count
    
    print(f"Text original: {text}")
    print(f"Text comprimat: {result}")
    
    return result


while True:
    text = input("Introduceti un text: ")

    if text.strip() == "":
        print("Nu a fost introdus nimic!")
        continue

    break

run_length_encoding(text)

