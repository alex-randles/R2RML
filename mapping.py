import pandas as pd
from flask import render_template
from pandas import ExcelWriter
from pandas import ExcelFile


csv_file = "people.csv"


def read_file(file_name):
    file_extension = (file_name.split(".")[1]).lower()
    print(file_extension)
    if file_extension == "csv":
        data = pd.read_csv(file_name)
    elif file_extension == "json":
        data = pd.read_json(file_name)
    else:
        data = pd.read_excel(file_name)
    return data


def get_column_names(file_name=csv_file):
    column_names = list(read_file(file_name).columns)
    return column_names


def create_output(file_name, output_file_name,  subject_prefix, id_selected_index, column_prefixes):
    output = """"""
    data = read_file(file_name)
    for i in range(0, len(data)):
        columns = get_column_names(file_name)
        output += subject_prefix.split(">")[0] + "/" + str(data[columns[id_selected_index]][i]) + subject_prefix.split(">")[1] + ">" + "\n"
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
    print(output)
    return render_template("result.html", result=output)


def write_file(output_file, text):
    output_file = open(output_file, "w")
    output_file.write(text)
    print("Output written to {}.....".format(output_file))


if __name__ == "__main__":
    # read_excel("test_excel.xls")
    # create_output("people.csv", "output.ttl", "<http://www.txample.com/people/voc/Person>", [ "<http://www.NAME.com/people/voc/Person/>", "<http://www.FIRST.com/people/voc/Person/>", "<http://www.LAST.com/people/voc/Person/>", "<http://www.MIDDLE.com/people/voc/Person/>", "<http://www.EMAIL.com/people/voc/Person/>", "<http://www.PHONE.com/people/voc/Person/>", "<http://www.FAX.com/people/voc/Person/>", "<http://www.TITLE.com/people/voc/Person/>"])
    #namespace = '<http://www.txample.com/people/voc/Person>'
    create_output("test_excel.xls", "test_output.ttl", '<http://www.txample.com/people/voc/Person>', 0,  ['<http://www.txample.com/people/voc/Person>','<http://www.txample.com/people/voc/Person>','<http://www.txample.com/people/voc/Person>', '<http://www.txample.com/people/voc/Person>','<http://www.txample.com/people/voc/Person>'])

