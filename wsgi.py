import subprocess, os
from flask import Flask, abort, flash, Response, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static'
app = Flask(__name__, static_url_path="/conda")

@app.route("/upload/<channel>/<arch>", methods=['POST'])
def upload(channel, arch):
    if arch not in ["linux-64", "win-64"]: 
        abort(404)
    # check if the post request has the file part
    if 'file' not in request.files:
        #flash('No file part')
        #return redirect(request.url)
        abort(Response('No file part'))
    file = request.files['file']
    filename = secure_filename(file.filename)
    channel = secure_filename(channel)
    upload_path = os.path.join(UPLOAD_FOLDER, channel, arch)
    os.makedirs(upload_path, exist_ok=True)
    file.save(os.path.join(upload_path, filename))
    subprocess.run(["conda", "index"], cwd=upload_path, shell=True)
    return "OK"