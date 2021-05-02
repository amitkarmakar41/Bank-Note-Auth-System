from flask import Flask,request,redirect,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predict', methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        variance = request.form['Variance']
        skewness = request.form['Skewness']
        curtosis = request.form['Curtosis']
        entropy = request.form['Entropy']
        result = model.predict([[float(variance), float(skewness), float(curtosis), float(entropy)]])

        return render_template('index.html',result = result[0])
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
