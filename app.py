from flask import Flask, render_template, request  # type: ignore[reportMissingImports]
from Password_Checker import (
    calculate_score,
    check_length,
    check_upper,
    check_lower,
    check_number,
    check_special,
    generate_password
)

app = Flask(__name__)


def check_password_details(password):
    score = calculate_score(password)

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    requirements = {
        "length": check_length(password),
        "upper": check_upper(password),
        "lower": check_lower(password),
        "number": check_number(password),
        "special": check_special(password)
    }

    suggestions = []

    if not requirements["length"]:
        suggestions.append("Use at least 8 characters")

    if not requirements["upper"]:
        suggestions.append("Add an uppercase letter")

    if not requirements["lower"]:
        suggestions.append("Add a lowercase letter")

    if not requirements["number"]:
        suggestions.append("Add a number")

    if not requirements["special"]:
        suggestions.append("Add a special character")

    return score, strength, requirements, suggestions


@app.route("/", methods=["GET", "POST"])
def home():

    password = ""
    score = None
    strength = ""
    requirements = {
        "length": False,
        "upper": False,
        "lower": False,
        "number": False,
        "special": False
    }
    suggestions = []

    if request.method == "POST":
        password = request.form.get("password", "")

        score, strength, requirements, suggestions = check_password_details(password)

    return render_template(
        "index.html",
        password=password,
        score=score,
        strength=strength,
        requirements=requirements,
        suggestions=suggestions
    )


@app.route("/generate")
def generate():

    password = generate_password()

    score, strength, requirements, suggestions = check_password_details(password)

    return render_template(
        "index.html",
        password=password,
        score=score,
        strength=strength,
        requirements=requirements,
        suggestions=suggestions
    )


if __name__ == "__main__":
    app.run(debug=True)