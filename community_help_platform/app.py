from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Temporary storage (OK for Round-1)
help_requests = []

@app.route("/")
def home():
    return render_template("help.html")

@app.route("/help", methods=["POST"])
def post_help():
    data = request.json
    data["status"] = "Open"
    help_requests.append(data)
    return jsonify({"message": "Help request posted successfully"})

@app.route("/admin")
def admin_view():
    return render_template("help_admin.html", requests=help_requests)

if __name__ == "__main__":
    app.run(debug=True)
