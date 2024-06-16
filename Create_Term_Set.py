import sys
import os

def create_term_file(labelfile, termfile, term_cutoff): # create term file

    f = open(labelfile, "rU")
    text = f.read()
    f.close()

    term_count_dict = dict()

    for line in text.splitlines():
        values = line.strip().split("  ")
        term_list = values[1].split(",")
        for term in term_list:
            if (term in term_count_dict):
                term_count_dict[term] = term_count_dict[term] + 1
            else:
                term_count_dict[term] = 1

    f=open(termfile, "w")
    for term in term_count_dict:
        if(term_count_dict[term]>term_cutoff):
            f.write(term+"\n")
    f.flush()
    f.close()

if __name__ == '__main__':

    dir=sys.argv[1]
    type_list=["MF", "BP", "CC"]
    term_cutoff_list=[0, 0, 0]

    for i in range(len(term_cutoff_list)):
        labelfile = dir + "/"  + type_list[i] + "/train_gene_label"
        termfile = dir + "/" + type_list[i] + "/term_list"
        create_term_file(labelfile, termfile, term_cutoff_list[i])








