from flask import Flask, render_template, request

app = Flask(__name__)

memos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST" :
        content = request.form.get("input")
        memos.append(content)
    return render_template("index.html", memos=memos)

if __name__ == '__main__' :
    app.run(debug=True)