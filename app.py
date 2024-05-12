from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        data = pd.read_csv("C:\programs\minor\Disease_semi-final_draft_1.csv")

        # Fetch user input from the form
        gender = request.form['gender']
        fever = request.form['fever']
        cough = request.form['cough']
        fatigue = request.form['fatigue']
        breathing = request.form['breathing']
        blood_pressure = request.form['bloodPressure']
        cholesterol_level = request.form['cholesterol']

        # Add your prediction logic here using the fetched input
        filtered_data = data[
            (data['Fever'] == fever) &
            (data['Cough'] == cough) &
            (data['Fatigue'] == fatigue) &
            (data['Difficulty Breathing'] == breathing) &
            (data['Gender'] == gender) &
            (data['Blood Pressure'] == blood_pressure) &
            (data['Cholesterol Level'] == cholesterol_level)
        ]

        if not filtered_data.empty:
            total_matches = len(filtered_data)

            # Calculate probabilities
            disease_counts = filtered_data['Disease'].value_counts()
            probabilities = {disease: count / total_matches for disease, count in disease_counts.items()}

            print("Possible diseases you might be carrying:")
            lst=""
            for disease, probability in probabilities.items():
                lst+=f"- {disease} (Probability: {probability:.2%})"
                lst+="\t"
                print(f"- {disease} (Probability: {probability:.2%})")
        else:
            lst="No matching diseases found based on your input."

        # For tes return a simple response
        return render_template('predict.html', res=lst)
    else:
        return render_template('predict.html') 

if __name__ == '__main__':
    app.run(debug=True)
