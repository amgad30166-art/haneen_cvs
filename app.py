from flask import Flask, render_template, request, send_file
from generate_cv import generate_cv
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = {
        "full_name": request.form.get("full_name"),
        "full_name_ar": request.form.get("full_name_ar"),
        "gender": request.form.get("gender"),
        "age": request.form.get("age"),
        "nationality": request.form.get("nationality"),
        "religion": request.form.get("religion"),
        "marital_status": request.form.get("marital_status"),
        "passport_number": request.form.get("passport_number"),
        "profession": request.form.get("profession"),
        "monthly_salary": request.form.get("monthly_salary"),
        "height_cm": request.form.get("height_cm"),
        "weight_kg": request.form.get("weight_kg"),
        "medical_fit": True
    }

    output_path = generate_cv(data)

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

