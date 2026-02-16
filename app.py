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

    def generate_cv(data):
    OUTPUT_DIR = r"D:\out"
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    file_name = f"{data['full_name']}_CV.pdf"
    output_path = os.path.join(OUTPUT_DIR, file_name)

    doc = SimpleDocTemplate(output_path, pagesize=A4)
    elements = []

    # Build your CV content here...

    doc.build(elements)

    return output_path

