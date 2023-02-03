from flask import Flask,render_template
import pickle
modelss=pickle.load(open('elastic_model.pkl','rb'))


app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict_placement():
    cgpa=float(request.form.get('cgpa'))
    iq = int(request.form.get('iq'))
    profile_score = int(request.form.get('profile_score'))


    # prediction
    result=modelss.predict(np.array([cgpa,iq,profile_score]).reshape(1,3))
    return str(result)


if __name__ == '__main__':
    app.run(debug = True)