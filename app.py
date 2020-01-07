from flask import Flask, render_template

app = Flask(__name__)

#home page template import

@app.route("/")
def home():
    return render_template('home.html')
# second page import

@app.route('/about/')
def about():
    return render_template('2.html')
    
if __name__ == "__main__":
    app.run(debug=True)
