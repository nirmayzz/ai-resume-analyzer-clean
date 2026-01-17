from flask import Flask, render_template, request
import os
from resume_analyzer import analyze_resume

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATES_DIR)

@app.route("/", methods=["GET", "POST"])
def home():
    feedback = None

    if request.method == "POST":
        resume_text = request.form["resume"]
        role = request.form["role"]
        analyze_resume(resume_text, role)

    return render_template("index.html", feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)

from resume_analyzer import analyze_resume