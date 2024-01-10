from flask import Flask, Response, send_from_directory
from flask import send_file
from werkzeug.exceptions import NotFound

app = Flask(__name__)

video_file_paths = {
    0: 'sample720.mp4',
    1: 'sample.mp4',
    2: 'sample1080.mp4',
}
@app.route('/test')
def test():
    return "test"

@app.route("/video/<int:idval>")
def stream_video(idval):
    
    try:
        path = video_file_paths.get(idval)
        if path is None:
            raise NotFound(description="Video not found")

        # return Response(send_file(path, mimetype="video/mp4"), direct_passthrough=True)
        return send_from_directory('.', path, mimetype="video/mp4", as_attachment=True)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
