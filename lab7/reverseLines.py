def reverse_lines(input_file, output_file):
    file_in = open(input_file, "r", encoding="utf-8")
    file_out = open(output_file, "w", encoding="utf-8")
    
    lines = file_in.readlines()
    
    for line in lines:
        reversed_line = line.rstrip('\n')[::-1]
        file_out.write(reversed_line + '\n')
    
    file_in.close()
    file_out.close()

reverse_lines("reverseLines.txt", "output.txt")
print("Fisierul a fost procesat. Verificati output.txt")
