from flask import Flask, redirect, url_for, render_template, request, send_file

import stegano as stg

app = Flask(__name__)


@app.route('/main_encode', methods=['POST', 'GET'])
def main_encode():
    return render_template('encode.html')

@app.route('/main_decode', methods=['POST', 'GET'])
def main_decode():
    return render_template('decode.html')

@app.route('/encode', methods = ['POST', 'GET'])  
def encode():  
    if request.method == 'POST':  
        file = request.files['file']
        if not stg.valid_filetype(file.filename):
            return render_template("error.html", error=stg.INVALID_FILETYPE_MSG%(file.filename))
        message = request.form['message']
        if (len(message) == 0):
            return render_template("error.html", error="Message is empty!")
        new_image = request.form['new_image']
        if not stg.valid_filetype(new_image):
            return render_template("error.html", error=stg.INVALID_FILETYPE_MSG%(new_image))
        stg.encode(file, message, new_image)
        #file.save(file.filename)  
        return render_template("download.html", name = new_image)  
    elif request.method == 'GET':
        return render_template('encode.html')
  
@app.route('/decode', methods = ['POST', 'GET'])  
def decode():  
    if request.method == 'POST':  
        file = request.files['file']
        if not stg.valid_filetype(file.filename):
            return render_template("error.html", error=stg.INVALID_FILETYPE_MSG%(file.filename))

        return render_template("success.html", message=stg.decode(file.filename))
    elif request.method == 'GET':
        return render_template('decode.html')
    
@app.route('/download', methods = ['POST', 'GET'])
def download():
    file = request.form['file_path']
    return send_file(file, download_name=file, as_attachment=True)

@app.route('/', methods = ['POST', 'GET'])
def mainPage():
    return redirect(url_for('index'))

@app.route('/index', methods = ['POST', 'GET'])
def index():
   return render_template("main.html")

if __name__ == '__main__':
	app.run(debug=True, port=80, host='0.0.0.0')
