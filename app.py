import os, json
from flask import Flask, render_template, request, redirect, url_for

os.system("cls")

app = Flask(__name__)

with open("data.json", "r", encoding="UTF-8") as f:
	data = json.loads(f.read())

@app.route("/", methods = ["GET", "POST"])
def search():
	if request.method == "POST":
		id = request.form.get("id")
		
		if id != "":
			return redirect(url_for("id", id = id))

	return render_template(
		"search.html"
	)

@app.route("/all")
def all():
	return render_template(
		"all.html",
		data = data,
		r = len(data)
	)

@app.route("/id<id>")
def id(id):
	return render_template(
		"id.html",
		name = data[id]["name"],
		food = data[id]["food"],
		icon = data[id]["links"]["icon"],
		rank = data[id]["links"]["rank"],
		tribe = data[id]["links"]["tribe"],
		attribute = data[id]["links"]["attribute"]
	)

if __name__ == "__main__":
	app.run(debug=True)