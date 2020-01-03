from flask import Flask     
from flask import render_template,request
import pickle
app = Flask(__name__)
   
@app.route('/')       
def hello(): 
    return render_template('hello_form.html')   

@app.route('/predict',methods =['POST'])       
def get_result(): 
    poly = pickle.load(open('poly.pkl','rb'))
    model = pickle.load(open('model.pkl','rb'))
    query = [[float(request.form['text2'])]]
    toget = poly.transform(query)
    sal = model.predict(toget)
    return 'Dear ' +request.form["text1"] + ' Your predicted salary after ' + request.form["text2"] + ' experience is :' + toget   
  
if __name__=='__main__': 
   app.run(debug=True) 