from flask import Flask
import mbta_helper
print(mbta_helper.find_stop_near("Boston Common"))
# Beacon St opp Walnut St



app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')
def hello():
    return "Hello World!"

@app.route('/nearest_mbta', methods=['POST'])
def nearest_mbta():
    address = request.form.get('address')
    stop_name, accessible = find_nearest_mbta_stop(address)
    return render_template('mbta_station.html', stop_name=stop_name, accessible=accessible)



print(mbta_helper.find_stop_near("Boston Common"))

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
