from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with open("users.txt", "a") as f:
            f.write(f"{username},{password}\n")

        message = "Saved!"

    return render_template("index.html", msg=message)

app.run(host="0.0.0.0", port=10000)