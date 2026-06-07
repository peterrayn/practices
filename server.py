from flask import Flask,request
from PIL import Image
from predictfromserver import predict
app= Flask(__name__)

@app.route("/upload",methods=['POST'])
def upload():
    img_list=[Image.open(v) for v in request.files.values()]
    
    return predict(img_list),200

if __name__=="__main__":
    app.run()