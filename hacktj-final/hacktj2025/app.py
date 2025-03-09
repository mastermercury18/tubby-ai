from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    if file and file.filename.endswith('.csv'):
        # Save the file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Process the CSV file
        df = pd.read_csv(filepath)
        # Assuming the CSV has columns 'Category' and 'Value'
        if 'Category' in df.columns and 'Value' in df.columns:
            data_dict = df.set_index('Category')['Value'].to_dict()
            return jsonify(data_dict)
        else:
            return jsonify({"error": "CSV must contain 'Category' and 'Value' columns"}), 400
    return jsonify({"error": "Invalid file type"}), 400

if __name__ == '__main__':
    app.run(debug=True)# from flask import Flask, render_template, request, redirect, url_for
# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads'

# # Ensure the upload folder exists
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         # Check if a file is uploaded
#         if 'file' not in request.files:
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             return redirect(request.url)
#         if file and file.filename.endswith('.csv'):
#             # Save the file
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#             file.save(filepath)
#             return redirect(url_for('chart', filename=file.filename))
#     # return render_template(x'upload.html')

# @app.route('/chart/<filename>')
# def chart(filename):
#     filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     df = pd.read_csv(filepath)

#     # Generate a pie chart
#     if 'Category' in df.columns and 'Value' in df.columns:
#         plt.figure(figsize=(6, 6))
#         plt.pie(df['Value'], labels=df['Category'], autopct='%1.1f%%', startangle=140)
#         plt.title('Pie Chart from CSV Data')
#         chart_path = os.path.join(app.config['UPLOAD_FOLDER'], 'piechart.png')
#         plt.savefig(chart_path)
#         plt.close()
#         return render_template('chart.html', chart_url=chart_path)
#     else:
#         return "CSV file must contain 'Category' and 'Value' columns."

# if __name__ == '__main__':
#     app.run(debug=True)