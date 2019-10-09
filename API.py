# imported modules
from flask import Flask, render_template, request, send_file, send_from_directory
from werkzeug import secure_filename
from mapping import create_output, get_column_names
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# to prevent caching of previous result
file_counter = 0
app.config["allowed_file_extensions"] = ["csv", "xls"]
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
file_name = ""


class API:

    def __init__(self):
        app.run(host="127.0.0.1", port="5000", threaded=True, debug=True)

    @staticmethod
    def create_output_file(data,filename):
        output_file = open(filename, "w")
        output_file.write(data)

    @app.route("/", methods=["GET", "POST"])
    def display_results():
        if request.method == "POST":
            # get file uploaded
            file = request.files['file']
            filename = secure_filename(file.filename)
            file_extension = (filename.split(".")[1]).lower()
            global file_path
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if file and file_extension in app.config["allowed_file_extensions"]:
                saved_file = file.save(file_path)
                return render_template("post.html", results=get_column_names(file_path))
            elif not file:
                return "No file uploaded....."
            else:
                return "Please upload a CSV file"
        else:
            return render_template("get.html")

    @app.route("/result", methods=["GET", "POST"])
    def return_result():
        subject_prefix = request.values.get('subject_prefix')
        prefixes = []
        checkbox_values = []
        global file_path
        for i in range(0, len(get_column_names(file_path))):
            checkbox_values.append(request.values.get("id_selection_" + str(i)))
            prefixes.append(request.values.get("prefix_" + str(i)))
        id_selected_index = checkbox_values.index("on")
        print("****** id selections", checkbox_values, id_selected_index)
        return create_output(file_path, "test_output.ttl", subject_prefix, id_selected_index, prefixes)

    @app.route("/download-file/", methods=["GET"])
    def return_file():
        print("Downloading file.......")
        download_path = "test_output.ttl"
        return send_file(download_path, as_attachment=True, cache_timeout=0)


if __name__ == "__main__":
    # start api
    API()