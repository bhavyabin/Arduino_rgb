from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    with open("color.txt", "r") as file:
        x = file.read()
    return render_template("index.html",x = x)

@app.route("/api", methods=["POST"])
def api():
    with open("color.txt", "w") as file:
        file.write(request.json["color"])

    print(request.json)
    return request.json["color"]


@app.route("/get")
def get():
    with open("color.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0")