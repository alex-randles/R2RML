import pandas as pd


csv_file = "/home/alex/r2rml/test_alan/people.csv"
data = pd.read_csv(csv_file)
columns = data.columns.values
number_entries = len(data)


def create_output():
    output = """"""
    # class_type = "<http://www.txample.com/people/voc/Person>"
    class_type = input("What type of class is this data? ")
    subject = input("What is the subject of the data? ")
    subject = subject = subject[:-1] + "{}" + subject[-1]
    print(subject)
    # subject = "<http://www.txample.com/people/voc/Person{}>\n".format(data[columns[0]][i])
    # subject = input("What is the subject prefix?")
    for i in range(0, number_entries):
        columns = list(data.columns.values)
        subject = subject.format(data[columns[0]][i])
        print(subject)
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
            # print(predicate)
            # print(object)
        # print(output)
        output_file = open("output_file.ttl", "w")
        output_file.write(output)


if __name__ == "__main__":
    create_output()
