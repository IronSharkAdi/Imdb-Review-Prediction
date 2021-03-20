from flask import Flask , render_template ,  request
app = Flask(__name__)
from flask_text import make_prediction

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict/' ,methods = ['POST', 'GET'])
def login():
   if request.method == 'POST': 
      review = request.form['text']
      prediction = make_prediction(review)   
      return render_template('app.html' , result = prediction[0])  
   else: 
      return render_template('success') 


if __name__ == '__main__':
   app.run(debug = True)    

