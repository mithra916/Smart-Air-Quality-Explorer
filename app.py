from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data once globally
df = pd.read_csv('cleaned_air_quality.csv')
df['AQI Value'] = pd.to_numeric(df['AQI Value'], errors='coerce')
df = df.dropna(subset=['AQI Value'])

@app.route('/')
def index():
    return render_template("index.html", data=df.to_dict(orient='records'))

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question'].lower()

    answer = "Sorry, I don't understand your question."

    if "worst" in question or "highest aqi" in question:
        worst_row = df.loc[df['AQI Value'].idxmax()]
        answer = f"The worst air quality is in {worst_row['Country']} with an AQI of {worst_row['AQI Value']} on {worst_row['Date']}."

    elif "best" in question or "lowest aqi" in question:
        best_row = df.loc[df['AQI Value'].idxmin()]
        answer = f"The best air quality is in {best_row['Country']} with an AQI of {best_row['AQI Value']} on {best_row['Date']}."

    return render_template("index.html", data=df.to_dict(orient='records'), answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
