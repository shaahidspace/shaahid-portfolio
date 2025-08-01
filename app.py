from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/qr", methods=["GET", "POST"])
def qr():
    if request.method == "POST":
        data = request.form["qrdata"]
        img = qrcode.make(data)
        buf = io.BytesIO()
        img.save(buf)
        buf.seek(0)
        return send_file(buf, mimetype='image/png', as_attachment=True, download_name='qr_code.png')
    return render_template("qr.html")

if __name__ == "__main__":
    app.run(debug=True)