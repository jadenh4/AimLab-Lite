from flask import Flask, render_template, request
from calculators import edpi, cm_per_360, convert_sens

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        tool = request.form.get("tool")

        if tool == "edpi":
            dpi = float(request.form.get("dpi", 0))
            sens = float(request.form.get("sens", 0))
            result = {
                "title": "eDPI Result",
                "lines": [
                    f"DPI: {dpi:g}",
                    f"Sensitivity: {sens:g}",
                    f"eDPI: {edpi(dpi, sens):.2f}"
                ]
            }

        elif tool == "cm360":
            dpi = float(request.form.get("dpi", 0))
            sens = float(request.form.get("sens", 0))
            yaw = float(request.form.get("yaw", 0.022))  # common baseline
            result = {
                "title": "360° Distance Result",
                "lines": [
                    f"DPI: {dpi:g}",
                    f"Sensitivity: {sens:g}",
                    f"Yaw/Scale: {yaw:g}",
                    f"Distance for 360°: {cm_per_360(dpi, sens, yaw):.2f} cm"
                ]
            }

        elif tool == "convert":
            source_game = request.form.get("source_game")
            target_game = request.form.get("target_game")
            source_sens = float(request.form.get("source_sens", 0))
            converted = convert_sens(source_game, target_game, source_sens)
            result = {
                "title": "Sensitivity Conversion",
                "lines": [
                    f"From: {source_game}",
                    f"To: {target_game}",
                    f"Source Sens: {source_sens:g}",
                    f"Converted Sens (approx): {converted:.4f}"
                ]
            }

    return render_template("Gameindex.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
