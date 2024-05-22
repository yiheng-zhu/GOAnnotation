import sys
import os

def read_protein_list(go_term_file):

    f = open(go_term_file, "r")
    text = f.read()
    f.close()

    protein_id_list = []

    for line in text.splitlines():

        line = line.strip()
        protein_id = line.split()[0]
        protein_id_list.append(protein_id)

    return protein_id_list

def total_protein_number(workdir):

    all_protein_list = []
    type_list = ["MF", "BP", "CC"]
    for type in type_list:
        protein_id_list = read_protein_list(workdir + "/" + type + "_Terms")
        print("The number of " + type + " proteins: " + str(len(protein_id_list)))
        all_protein_list.extend(protein_id_list)

    all_protein_list = list(set(all_protein_list))

    print("The number of all proteins: " + str(len(all_protein_list)))

    f = open(workdir + "/all_protein_list", "w")
    for protein in all_protein_list:
        f.write(protein + "\n")
    f.close()

total_protein_number(sys.argv[1])
