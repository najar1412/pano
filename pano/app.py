import os
import pathlib
import json

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

    options = db.relationship('PanoOption', backref='pano', lazy=True)

    def __repr__(self):
        return f'<Pano: {self.name}>'


class PanoOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CA = db.Column(db.String)
    FGLightMap = db.Column(db.String)
    FGLightMapColor = db.Column(db.String)
    bg_brightness = db.Column(db.String)
    exposure = db.Column(db.String)
    bloomStrength = db.Column(db.String)
    bloomThreshold = db.Column(db.String)
    bloomRadius = db.Column(db.String)
    focalLength = db.Column(db.String)
    enableMinimap = db.Column(db.String)
    fg_alpha = db.Column(db.String)

    pano_id = db.Column(db.Integer, db.ForeignKey('pano.id'),
        nullable=False)


    def __repr__(self):
        return f'<PanoOption: {self.id}>'


db.create_all()

@app.route('/')
def index():
    panos = module.database.Pano(model=Pano).get_all()
    options = module.database.PanoOption(model=PanoOption).get_all()


    return render_template('index.html', panos=panos, options=options)


@app.route('/pano/<int:id>')
def pano(id):
    pano = module.database.Pano(model=Pano).get_by_id(id)


    return render_template('pano.html', pano=pano)


@app.route('/pano/delete/<int:id>')
def pano_delete(id):
    deleting_pano = module.database.Pano(db=db, model=Pano).delete(id)
    if deleting_pano:
        print('items deleted')
    else:
        print('its not deleted')

    return redirect(url_for('index'))


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


@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    converted = module.database.js_object(request.form)

    clone_data = {
        'CA': 'false', 
        'FGLightMap': '1', 
        'FGLightMapColor': '#ffffff', 
        'bg_brightness': '0.3', 
        'exposure': '2', 
        'bloomStrength': '0', 
        'bloomThreshold': '0', 
        'bloomRadius': '0', 
        'focalLength': '50', 
        'enableMinimap': 'true', 
        'fg_alpha': '1',
        'pano_id': '1'
    }

    pano_option_dto = module.database.pano_option_dto(
        CA = converted['CA'],
        FGLightMap = converted['FGLightMap'],
        FGLightMapColor = converted['FGLightMapColor'],
        bg_brightness = converted['bg_brightness'],
        exposure = converted['exposure'],
        bloomStrength = converted['bloomStrength'],
        bloomThreshold = converted['bloomThreshold'],
        bloomRadius = converted['bloomRadius'],
        focalLength = converted['focalLength'],
        enableMinimap = converted['enableMinimap'],
        fg_alpha = converted['fg_alpha'],
        pano_id = converted['pano_id']
    )

    module.database.PanoOption(db=db, model=PanoOption).new(pano_option_dto.pano_id, pano_option_dto)

    print('Posting new Option')

    return 'one one'


@app.route('/delete_option/<int:id>')
def delete_option(id):
    module.database.PanoOption(db=db, model=PanoOption).delete(id)


    return redirect(url_for('index'))


@app.route('/edit/pano/<int:pano_id>/<int:option_id>')
def pano_edit(pano_id, option_id):
    print('---------------------')
    print(pano_id)
    print(type(pano_id))
    print(option_id)
    print(type(option_id))
    pano = module.database.Pano(model=Pano).get_by_id(pano_id)
    pano_option = module.database.PanoOption(model=PanoOption).get_by_id(option_id)
    print(':::::::::::::::')
    print(pano)
    print(':::::::::::::::')
    print(pano_option)


    return render_template('pano.html', pano=pano)




if __name__ == '__main__':
    app.run(debug=True, port=5000)