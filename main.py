#!/bin/python
from flask import Flask, jsonify, request
from wtforms import Form, validators, StringField
from app import read_number_plates

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def status():
    return "alive"


class ReadForm(Form):
    url = StringField('Url to image', [
        validators.URL()
    ])


@app.route('/read')
def read():
    form = ReadForm(request.args)

    if form.validate():
        url = form.url.data
        number_plates, region_names = read_number_plates(url)

        return jsonify({
            'success': True,
            'url': url,
            'number_plates': number_plates,
            'region_names': region_names,
        })

    return jsonify({
        'success': False,
        'errors': form.errors

    })

if __name__ == "__main__":
    app.run()
