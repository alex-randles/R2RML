# imported modules
from flask import Flask, render_template, request, send_file, send_from_directory
from mapping import get_column_names
# api framework
app = Flask(__name__)

from flask_caching import Cache
from werkzeug import secure_filename
import os
app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# to prevent caching of previous result
file_counter = 0
app.config["allowed_file_extensions"] = ["csv"]
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["AUDIO_FOLDER"] =  "/home/alex/PycharmProjects/R2RML/static/audio_files"


class API:

    def __init__(self):
        app.run(host="127.0.0.1", port="5000", threaded=True, debug=True)

    @app.route("/", methods=["GET", "POST"])
    def display_results():
        if request.method == "POST":
            prefix_1 = request.values.get('prefix_1')
            prefix_2 = request.values.get("prefix_2")
            # get file uploaded
            file = request.files['file']

            if file:
                # will default to None

                # save file
                filename = secure_filename(file.filename)
                file_extension = filename.split(".")[1]
                print(file, file.filename)
                print(file_extension)
                # if file_extension in app.config["allowed_file_extensions"]:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                print("file path:", file_path)
                saved_file = file.save(file_path)

                prefixes = [prefix_1, prefix_2]
                print("prefixes", prefixes)
            return render_template("post.html", results=get_column_names(file_path), prefixes=prefixes)
        else:
            return render_template("get.html")



if __name__ == "__main__":
    # start api
    API()