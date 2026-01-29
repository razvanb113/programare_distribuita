def filter_lines(input_file, output_file, cuvant_cheie):
    file_in = open(input_file, 'r', encoding="UTF-8")
    file_out = open(output_file, 'w', encoding="UTF-8")

    lines = file_in.readline()

    for line in lines:
        if cuvant_cheie in line:
            line.rstrip("\n")
            file_out.write(line + '\n')
        else:
            continue
    file_in.close()
    file_out.close()

cuvant_cheie = input("Introduceti cuvantul cheie: ")

filter_lines("filterLines.txt", "outputFilterLines.txt", cuvant_cheie)
    