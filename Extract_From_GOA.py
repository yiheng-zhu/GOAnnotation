import os
import sys

def extract(filename, outputfile, is_train):

    f = open(filename, "r")
    fo = open (outputfile, "w")

    for i in range(9):
        line = f.readline()

    while line:

        is_select, new_list = judge(line, is_train)

        if(is_select):

            new_line=new_list[1]+" "+new_list[4]+" "+new_list[8] + " " + new_list[13]
            fo.write(new_line+"\n")

        line = f.readline()

    f.close()
    fo.flush()
    fo.close()

def judge_evidence(evidence, is_train):

    if(is_train==True):

        no_evidence_list=["ND"]

        if(evidence not in no_evidence_list):
            return True
        else:
            return False
    else:

        evidence_list=["EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "TAS", "IC"]

        if(evidence in evidence_list):
            return True
        else:
            return False

def judge_exclude_GO_terms(term):

    #excludeGO_list = ["GO:0005515"]
    excludeGO_list = []

    if(term not in excludeGO_list):
        return True

    return False

def judge_database_source(database):

    database_list = ["UniProtKB"]

    if(database in database_list):
        return True

    return False

def judge_qualifier(qualifier):

    qualifier_list = ["NOT", "NOT|contributes_to", "NOT|colocalizes_with"]

    if(qualifier not in qualifier_list):
        return True

    return False


def judge(line, is_train):

    line = line.strip()
    new_list = line.split("\t")
    is_select=False

    if(judge_database_source(new_list[0]) and judge_qualifier(new_list[3]) and judge_exclude_GO_terms(new_list[4]) and judge_evidence(new_list[6], is_train)):
        is_select=True

    return is_select, new_list



if __name__ == '__main__':

    filename = sys.argv[1]
    outputfile = sys.argv[2]
    if(sys.argv[3]=="1"):
        is_train = True
    else:
        is_train = False

    extract(sys.argv[1], sys.argv[2], is_train)




