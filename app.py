from flask import Flask, render_template, request, jsonify

import math

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tile = request.form["tile"]
        zoom = request.form["zoom"]
        error = None

        try:
            x, y = map(int, tile.split(","))
        except ValueError:
            error = "Введите номер плитки в формате X, Y"
            return render_template("index.html", error=error)

        n = 2 ** int(zoom)
        lon_deg = x / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y / n)))
        lat_deg = lat_rad * 180.0 / math.pi

        return render_template("index.html", tile_x=x, tile_y=y, zoom=zoom, lat=lat_deg, lon=lon_deg)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
