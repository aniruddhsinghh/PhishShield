from flask import Flask, render_template, request
from utils.scanner import analyze_url

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        result = analyze_url(url)
        return render_template('index.html', result=result, scanned_url=url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
