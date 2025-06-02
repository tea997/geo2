# app.py
from flask import Flask, render_template, request, send_file
import pandas as pd
import io
from model import preprocess_data  # Only import preprocess_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preprocess', methods=['POST'])
def preprocess_file():
    if 'csvfile' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['csvfile']
    if file.filename == '':
        return "No selected file", 400

    try:
        df = pd.read_csv(file)
    except Exception as e:
        return f"Error reading CSV file: {e}", 400

    try:
        preprocessed_df = preprocess_data(df)
    except Exception as e:
        return f"Error during preprocessing: {e}", 500

    csv_buffer = io.StringIO()
    preprocessed_df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    return send_file(
        io.BytesIO(csv_buffer.getvalue().encode()),
        mimetype='text/csv',
        download_name='preprocessed_data.csv',
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)
