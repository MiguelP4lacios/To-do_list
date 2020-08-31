from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = []

#The default route
@app.route("/")
def tasks():
	return render_template("tasks.html", todos=todos)

#The default method is GET so I need to add the POST method in order to send the form with the new tasks
@app.route("/add", methods=["GET", "POST"])
def add():
	if request.method == "GET":
		return render_template("add.html")
	else:
		todo = request.form.get("task")
		todos.append(todo)
		return redirect("/")