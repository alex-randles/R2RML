import pandas as pd

csv_file = "people.csv"


def read_file(file_name):
    data = pd.read_csv(file_name)
    print(data)
    return data


def get_column_names(file_name=csv_file):
    column_names = list(read_file(file_name).columns)
    return column_names


def create_output():
    output = """"""
    # class_type = "<http://www.txample.com/people/voc/Person>"
    class_type = input("What type of class is this data? ")
    subject = input("What is the subject of the data? ")
    subject_prefix = subject = subject[:-1] + "/{}" + subject[-1]
    print(subject)
    data = read_file("people.csv")
    columns = data.columns.values
    number_entries = len(data)
    # subject = "<http://www.txample.com/people/voc/Person{}>\n".format(data[columns[0]][i])
    # subject = input("What is the subject prefix?")
    for i in range(0, 4):
        columns = list(data.columns.values)
        subject = subject_prefix.format(data[columns[0]][i]) + "\n"
        # print(subject, data[columns[0]][i])
        class_instance = "  a     {}   ;\n".format(class_type)
        output += subject
        output += class_instance
        prefix = "  <http://www.txample.com/people/voc/{}>"
        for column in columns[1:]:
            current_value = data[column][i]
            predicate = prefix.format(column) + "\n"
            if columns.index(column) == len(columns)-1:
                object_value = '        "{}" {}\n'.format(current_value, ".")
            else:
                object_value = '          "{}" {}\n'.format(current_value, ";")
            output += predicate
            output += object_value
        write_file("output_file.ttl", output)


def write_file(output_file, text):
    output_file = open("output_file.ttl", "w")
    output_file.write(text)
    print("Output written to {}.....".format(output_file))


if __name__ == "__main__":
    print(get_column_names())
    # create_output()
