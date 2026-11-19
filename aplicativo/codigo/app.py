from flask import Flask, request, render_template, redirect, url_for
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
app = Flask(__name__, 
template_folder=BASE_DIR / 'interface' / 'templates',
static_folder=BASE_DIR / 'interface' / 'static'
)
@app.route('/Login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        return redirect(url_for('dashboard', data= form_data))
    else:
        return render_template('login.html')  
@app.route('/Dashboard', methods=['POST', 'GET'])
def dashboard():
    if request.method == 'POST':
        pass
    else:   
        return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True) 