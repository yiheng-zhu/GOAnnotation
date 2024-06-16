import sys


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


def read_date_from_information_file(information_file):

    f = open(information_file, "r")
    date = f.readline()
    f.close()

    return date

def extract_sequence_by_date(sequence_file1, sequence_file2, info_dir, date1, date2):

    sequence_dict = read_sequence_dict(sequence_file1)

    f = open(sequence_file2, "w")

    for name in sequence_dict:
        date = read_date_from_information_file(info_dir + "/" + name)
        if(date>=date1 and date<=date2):
            print(date)
            f.write(">" + name + "\n" + sequence_dict[name] + "\n")
    f.close()

extract_sequence_by_date(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])