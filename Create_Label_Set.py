import os
import sys

def read_term_file(termfile):   # read term file

    f=open(termfile, "rU")
    text=f.read()
    f.close()
    return text.splitlines()

def create_single_label(term_list, label_list):  # create single label

    label_vector=[0 for i in range(len(term_list))]

    for term in label_list:
        if(term in term_list):
            label_vector[term_list.index(term)]=1

    return label_vector

def create_Label(labelfile, termfile, one_hot_label_file):  #create label

    term_list = read_term_file(termfile)

    f = open(labelfile, "rU")
    text = f.read()
    f.close()

    f = open(one_hot_label_file, "w")

    for line in text.splitlines():

        values = line.strip().split()
        label_list = values[1].split(",")
        label_vector = create_single_label(term_list, label_list)
        new_line = ""
        for hot in label_vector:
            new_line = new_line+str(hot)+" "
        new_line = new_line.strip()
        f.write(new_line+"\n")

    f.flush()
    f.close()


if __name__ == '__main__':

    dir=sys.argv[1]

    type_list=["MF"]

    for type in type_list:

        labelfile = dir + "/" +  type + "/train_gene_label"
        termfile = dir + "/" +  type + "/term_list"
        one_hot_label_file = dir + "/" + type + "/train_label_one_hot"
        create_Label(labelfile, termfile, one_hot_label_file)

        labelfile = dir + "/" + type + "/evaluate_gene_label"
        termfile = dir + "/" + type + "/term_list"
        one_hot_label_file = dir + "/" + type + "/evaluate_label_one_hot"
        create_Label(labelfile, termfile, one_hot_label_file)

        labelfile = dir + "/" + type + "/test_gene_label"
        termfile = dir + "/" + type + "/term_list"
        one_hot_label_file = dir + "/" + type + "/test_label_one_hot"
        create_Label(labelfile, termfile, one_hot_label_file)







