from flask import Flask,render_template,request
from pymongo.mongo_client import MongoClient
import pymongo
import os
from dotenv import load_dotenv
load_dotenv()
MONGO_URI=os.getenv("MONGO_URI")
client=MongoClient(MONGO_URI)
db=client.test
collection=db['flask_tutorial']

app=Flask(__name__)
@app.route('/submit',methods=['POST'])
def post_data():
    collection.insert_one(dict(request.json ))
    return render_template('/submit.html')
@app.route('/show')
def show():
    form_data=collection.find()
    data=list(form_data)
    for item in data:
     del item['_id']
     print(item)
    data={'data':data}
    return data

if __name__=="__main__":
    app.run(host="0.0.0.0",port=6000,debug=True)