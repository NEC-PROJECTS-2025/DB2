from flask import Flask, render_template, request

app = Flask(__name__)

# Route for Home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for About Project page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Predictions page
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    result = None
    image_path = None

    if request.method == 'POST':
        # Retrieve form inputs
        source = request.form['source']
        destination = request.form['destination']
        airline_name = request.form['airline_name']  # Updated variable name
        weather = request.form['weather']
        num_flights = int(request.form['num_flights'])
        peak_hours = request.form['peak_hours']
        traffic_density = request.form['traffic_density']

        # Updated prediction logic
        if "rainy" in weather.lower() or "storm" in weather.lower():
            result = "Delay Detected due to bad weather"
            image_path = "static/images/delay_weather.png"  # Replace with your weather delay image path
        elif peak_hours == "Yes" or traffic_density == "High":
            result = "Delay Detected due to busy air traffic"
            image_path = "static/images/delay_traffic.png"  # Replace with your air traffic delay image path
        elif num_flights > 100:
            result = "Delay Detected due to high flight volume"
            image_path = "static/images/delay_traffic.png"
        else:
            result = "No Delay Detected"
            image_path = "static/images/no_delay.png"  # Replace with your no delay image path

    return render_template('prediction.html', result=result, image_path=image_path)

# Route for Model Evaluation page
@app.route('/model-eval')
def model_eval():
    return render_template('model_eval.html')

# Route for Project Flowchart page
@app.route('/flowchart')
def flowchart():
    return render_template('flowchart.html')

if __name__ == '__main__':
    app.run(debug=True)
