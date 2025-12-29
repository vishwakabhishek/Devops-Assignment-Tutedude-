from flask import Flask,render_template,request
import requests
BACKEND_URL="http://127.0.0.1:8000"
app=Flask(__name__)
@app.route('/')
def index():
    name=request.args.get('name')
    password=request.args.get('password')
    return render_template('index.html',name=name,password=password)
@app.route('/submit',methods=['POST'])
def post_data():
    form_data=dict(request.form)
    requests.post(f"{BACKEND_URL}/submit",json=form_data)
    print(form_data)
    return "data submitted"
@app.route('/get_data')
def get_data():
    response=requests.get(BACKEND_URL+"/show")
    return response.json()

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)