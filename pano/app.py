from flask import Flask, render_template

import module.pano_io as pano_io

import config


app = Flask(__name__)
app.config.from_object(config.Config)

@app.route('/')
def index():
    panos = pano_io.PanoIo().get_all_from_server()
    return render_template('index.html', panos=panos)


@app.route('/pano/<int:id>')
def pano(id):
    pano = pano_io.PanoDb().get(1)
    return render_template('pano.html', pano=pano)


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)