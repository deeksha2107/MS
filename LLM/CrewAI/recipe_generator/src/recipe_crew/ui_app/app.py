from flask import Flask, render_template, request, send_from_directory
from recipe_crew.crew import RecipeGenerator
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recipe = None
    error = None
    pdf_available = False

    if request.method == "POST":
        topic = request.form.get("topic")
        try:
            crew = RecipeGenerator()
            result = crew.crew().kickoff(inputs={"topic": topic})
            recipe = result if isinstance(result, str) else str(result)
            pdf_path = os.path.join("static", "recipe.pdf")
            pdf_available = os.path.exists(pdf_path)
        except Exception as e:
            error = str(e)

    return render_template("index.html", recipe=recipe, error=error, pdf_available=pdf_available)

if __name__ == "__main__":
    app.run(debug=True)
