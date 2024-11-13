from flask import Flask, redirect, render_template, request, url_for
import mbta_helper

print(mbta_helper.find_nearest_mbta_stop("Boston Common"))
# Beacon St opp Walnut St

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/nearest_mbta", methods=["POST", "GET"])
def nearest_mbta():
    if request.method == "POST":
        place_name = request.form.get("address")  # not correct

        if not place_name:
            # flash("Please enter a valid place name.")
            return redirect(url_for("index"))

        # Fetch the nearest station
        nearest_station, accessible = mbta_helper.find_nearest_mbta_stop(place_name)
        # nearest_station, accessible = "Bosotn Common", True # Fake it till you make it

        if nearest_station:
            return render_template(
                "mbta_station.html", stop_name=nearest_station, accessible=accessible
            )
    else:
        # flash("No MBTA station found for the provided location.")
        return redirect(url_for("index"))


print(mbta_helper.find_nearest_mbta_stop("Boston Common"))

if __name__ == "__main__":
    app.run(debug=True)
