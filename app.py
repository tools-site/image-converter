from flask import Flask, request, send_file, render_template, Response
from PIL import Image
import io

app = Flask(__name__)

# index.html
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# jpgtopng.html
@app.route("/jpgtopng", methods=["GET"])
def jpgtopng():
    return render_template("jpgtopng.html")

# pngtojpg.html
@app.route("/pngtojpg", methods=["GET"])
def pngtojpg():
    return render_template("pngtojpg.html")

# webptopng.html
@app.route("/webptopng", methods=["GET"])
def webptopng():
    return render_template("webptopng.html")

# bmptopng.html
@app.route("/bmptopng", methods=["GET"])
def bmptopng():
    return render_template("bmptopng.html")

# pngtopdf.html
@app.route("/pngtopdf", methods=["GET"])
def pngtopdf():
    return render_template("pngtopdf.html")

# convert jpg to png
@app.route("/api/jpgtopng", methods=["POST"])
def jpg_to_png():
    image = request.files["image"]
    image = Image.open(image)
    image = image.convert("RGBA")
    output = io.BytesIO()
    image.save(output, "PNG")
    output.seek(0)
    return send_file(output, mimetype='image/png', download_name='image.png',as_attachment=True)

# convert png to jpg
@app.route("/api/pngtojpg", methods=["POST"])
def png_to_jpg():
    image = request.files["image"]
    image = Image.open(image)
    image = image.convert("RGB")
    output = io.BytesIO()
    image.save(output, "JPEG")
    output.seek(0)
    return send_file(output, mimetype='image/jpeg', download_name='image.jpg', as_attachment=True)

# convert webp to png
@app.route("/api/webptopng", methods=["POST"])
def webp_to_png():
    image = request.files["image"]
    image = Image.open(image)
    output = io.BytesIO()
    image.save(output, "PNG")
    output.seek(0)
    return send_file(output, mimetype='image/png', download_name='image.png', as_attachment=True)

# convert bmp to png
@app.route("/api/bmptopng", methods=["POST"])
def bmp_to_png():
    image = request.files["image"]
    image = Image.open(image)
    output = io.BytesIO()
    image.save(output, "PNG")
    output.seek(0)
    return send_file(output, mimetype='image/png', download_name='image.png', as_attachment=True)

# convert png to pdf
@app.route("/api/pngtopdf", methods=["POST"])
def png_to_pdf():
    image = request.files["image"]
    image = Image.open(image)
    output = io.BytesIO()
    image.save(output, "PDF")
    output.seek(0)
    return send_file(output, mimetype='application/pdf', download_name='image.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
