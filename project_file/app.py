import os

from flask import Flask, render_template, request

app = Flask(__name__)

UPLOAD_FOLDER = 'uploaded_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.errorhandler(413)
def to_large(e):
    return "File too large. Maximum size is 5 MB.", 413


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/upload", methods=['POST'])
def upload_file():
    if "image" not in request.files:
        return "No image file provided", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    if not allowed_file(file.filename):
        return "File type not allowed. Please upload an image 'png', 'jpg', 'jpeg', 'gif'", 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    return f"Image upload successfully! Saved to {file_path}"


if __name__ == "__main__":
    app.run(debug=True)

