import Find_Parents1 as fp
import sys
def create(originfile, dealfile):

    obo_dict = fp.get_obo_dict()
    f = open(originfile, "r")
    line = f.readline()
    fo = open(dealfile, "w")

    while line:

        values = line.strip().split()
        protein = values[0]
        termlist = values[1].strip().split(",")
        parentlist = []
        for term in termlist:
            parentlist = parentlist + fp.find_parents(obo_dict, term)

        parentlist = list(set(parentlist))
        if (len(parentlist) > 0):
            line = protein + "  "
            parentlist = sorted(parentlist)
            for parent in parentlist:
                line = line + parent + ","
            line = line.strip(",")
            fo.write(line+"\n")

        line = f.readline()

    f.close()
    fo.flush()
    fo.close()


if __name__=="__main__":

    dir = sys.argv[1]
    type_list = ["MF", "BP", "CC"]
    for type in type_list:
        create(dir+"/Original_"+ type+"_Terms", dir+"/"+type+"_Terms")

