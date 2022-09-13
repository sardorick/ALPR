from doctest import OutputChecker
from flask import Flask, render_template, request
import os 
from static.src.deeplearning import object_detection
from flask_assets import Bundle, Environment
from flask_sqlalchemy import SQLAlchemy
from static.src.save_results import save_results


app = Flask(__name__)
js = Bundle('scripts.js', output='gen/main.js')
assets = Environment(app)
assets.register('main.js', js)
BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH,'static/upload/')

db = SQLAlchemy(app)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        path_save = os.path.join(UPLOAD_PATH,filename)
        upload_file.save(path_save)
        text_list = object_detection(path_save,filename)
        save_results(text_list)

        print(text_list)

        return render_template('index.html',upload=True,upload_image=filename,text=text_list,no=len(text_list))

    return render_template('index.html',upload=False)


if __name__ =="__main__":
    app.run(debug=True)