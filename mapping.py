import pandas as pd
from flask import Flask, render_template, request, send_file, send_from_directory


csv_file = "people.csv"


def read_file(file_name):
    data = pd.read_csv(file_name)
    return data


def get_column_names(file_name=csv_file):
    column_names = list(read_file(file_name).columns)
    return column_names


def create_output(file_name, output_file_name,  subject_prefix, column_prefixes):
    output = """"""
    data = read_file(file_name)
    for i in range(0, len(data)):
        columns = get_column_names(file_name)
        output += subject_prefix.split(">")[0] + str(data[columns[0]][i])+ subject_prefix.split(">")[1] + ">" + "\n"
        class_instance = "  a     {} ;\n".format(subject_prefix)
        output += class_instance
        for column in columns[1:]:
            current_value = data[column][i]
            # predicate = prefix.format(column) + "\n"
            index = columns.index(column) - 1
            predicate = '  {}/{}>\n'.format(column_prefixes[index][:-1], column)
            if columns.index(column) == len(columns)-1:
                object_value = '        "{}" {}\n'.format(current_value, ".")
            else:
                object_value = '          "{}" {}\n'.format(current_value, ";")
            output += predicate
            output += object_value
    write_file(output_file_name, output)
    return render_template("result.html", result=output)


def write_file(output_file, text):
    output_file = open(output_file, "w")
    output_file.write(text)
    print("Output written to {}.....".format(output_file))


if __name__ == "__main__":
    # create_output("people.csv", "output.ttl", "<http://www.txample.com/people/voc/Person>", [ "<http://www.NAME.com/people/voc/Person/>", "<http://www.FIRST.com/people/voc/Person/>", "<http://www.LAST.com/people/voc/Person/>", "<http://www.MIDDLE.com/people/voc/Person/>", "<http://www.EMAIL.com/people/voc/Person/>", "<http://www.PHONE.com/people/voc/Person/>", "<http://www.FAX.com/people/voc/Person/>", "<http://www.TITLE.com/people/voc/Person/>"])
    create_output("static/uploads/EMP.CSV", "test_output.ttl", '<http://www.txample.com/people/voc/Person>',  ['<http://www.txample.com/people/voc/Person>','<http://www.txample.com/people/voc/Person>','<http://www.txample.com/people/voc/Person>', '<http://www.txample.com/people/voc/Person>','<http://www.txample.com/people/voc/Person>'])

