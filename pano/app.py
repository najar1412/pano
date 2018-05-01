import os
import pathlib

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

import module.pano_io as pano_io
import module.database
import config


ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)

class Pano(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    desc = db.Column(db.String)
    fg_img = db.Column(db.String)
    alpha_img = db.Column(db.String)
    emissive_img = db.Column(db.String)
    bg_img = db.Column(db.String)
    floorplan_img = db.Column(db.String)
    thumb_img = db.Column(db.String)

    def __repr__(self):
        return f'<Pano: {self.name}>'


db.create_all()

@app.route('/')
def index():
    panos = pano_io.PanoIo().get_all_from_server()
    test = module.database.Pano(model=Pano).get_all()

    print(test)

    return render_template('index.html', panos=panos, test=test)


@app.route('/pano/<int:id>')
def pano(id):
    pano = pano_io.PanoDb().get(1)
    test = module.database.Pano(model=Pano).get_by_id(id)

    return render_template('pano.html', pano=pano, test=test)


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')


def secure_and_save(pano_name, file):
    if file and allowed_file(file.filename):
        pano_folder = os.path.join(config.Config().app_root, 'static', 'pano', pano_name)

        if os.path.exists(pano_folder): 
            filename = secure_filename(file.filename)
            file.save(os.path.join(pano_folder, filename))

            return filename

        else:
            os.makedirs(pano_folder)
            filename = secure_filename(file.filename)
            file.save(os.path.join(pano_folder, filename))

            return filename


@app.route('/uploading', methods=['POST'])
def uploading():
    if request.method == 'POST':
        form = request.form.to_dict()
        files = request.files.to_dict()
        params = {
            'pano_fg_img': None,
            'pano_alpha_img': None,
            'pano_emissive_img': None,
            'pano_bg_img': None,
            'pano_floorplan_img': None,
            'pano_thumb_img': None
            }

        for k, image in files.items():
            if k in params:
                saved_file = secure_and_save(form['pano_name'], image)
                params[k] = saved_file

        dto = module.database.dto(
            form['pano_name'], form['pano_desc'], params['pano_fg_img'], 
            params['pano_alpha_img'], params['pano_emissive_img'], params['pano_bg_img'], 
            params['pano_floorplan_img'], params['pano_thumb_img']
        )

        module.database.Pano(db=db, model=Pano).new(dto)


        return redirect(url_for('index'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)