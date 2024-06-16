import sys
import os


def read_protein_go_dict(protein_term_map_file):   # read go dict

    f = open(protein_term_map_file, "rU")
    text = f.read()
    f.close()

    go_dict = dict()

    for line in text.splitlines():
        line = line.strip()
        values = line.split()
        go_dict[values[0]] = values[1]

    return go_dict

def read_sequence_dict(sequence_file):

    f = open(sequence_file, "r")
    text = f.read()
    f.close()

    sequence_dict = dict()
    for line in text.splitlines():
        line = line.strip()
        if(line.startswith(">")):
            name = line
        else:
            sequence_dict[name[1:]] = line

    return sequence_dict



def extract(sequence_file, go_file, label_file, name_file):

    sequence_dict = read_sequence_dict(sequence_file)
    go_dict = read_protein_go_dict(go_file)

    f1 = open(label_file, "w")
    f2 = open(name_file, "w")

    for name in sequence_dict:
        if(name in go_dict):
            f1.write(name+"  "+go_dict[name]+"\n")
            f2.write(name+"\n")

    f1.flush()
    f1.close()
    f2.flush()
    f2.close()

if __name__ == '__main__':

    workdir = sys.argv[1]
    type_list = ["MF", "BP", "CC"]
    data_type_list = ["train", "evaluate", "test"]

    for data_type in data_type_list:
        for type in type_list:

            sequence_file = workdir + "/" + data_type + "_sequence.fasta"
            go_file = "/data/yihengzhu/GOA/" + type + "_Terms"
            label_file = workdir + "/" + type + "/" + data_type + "_gene_label"
            name_file = workdir + "/" + type + "/" + data_type + "_gene_list"
            extract(sequence_file, go_file, label_file, name_file)




