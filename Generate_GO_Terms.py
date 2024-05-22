import sys
def generate_go_terms(goffile, outputfile, type):

    f = open(goffile, "r")
    line = f.readline()
    term_dict = dict()

    while line:

        line = line.strip()
        values = line.split()
        id = values[0]
        go_term = values[1]
        go_type = values[2]

        if(go_term.startswith("GO:")):

            if(go_type==type[1]):

                if(id not in term_dict):
                    term_dict[id]=[go_term]
                else:
                    term_dict[id].append(go_term)

            if(go_type!="F" and go_type!="P" and go_type!="C"):
                print(line)

        else:
            print(line)

        line =  f.readline()

    f.close()

    f = open(outputfile, "w")
    for term in term_dict:
        current_list = list(set(term_dict[term]))
        line=term+"  "+current_list[0]
        for i in range(1, len(current_list)):
            line = line +","+current_list[i]
        f.write(line+"\n")


    f.flush()
    f.close()



if __name__ == '__main__':

    generate_go_terms(sys.argv[1], sys.argv[2], sys.argv[3])





