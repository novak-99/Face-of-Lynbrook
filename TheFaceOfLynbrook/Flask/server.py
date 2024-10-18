from flask import Flask, request, send_from_directory, jsonify, redirect
import random
import os
import io
from datetime import datetime
from werkzeug.utils import secure_filename
from multiprocessing import Process

# ml 

import torch
import torchvision
from torchvision.models import resnet50
import torchvision.transforms as transforms
import pickle
import PIL
from PIL import Image
from skimage.color import rgba2rgb, gray2rgb
import numpy as np
import uuid

# SSL 

from werkzeug.middleware.proxy_fix import ProxyFix

from flask_sslify import SSLify
import ssl

def id_img(img_name):
    return f"{uuid.uuid4()}-{img_name}"

def rgb_img(img):
    img = np.array(img).transpose(1,0,2)
    if len(img.shape) == 2: 
      img = gray2rgb(img)
    else:
      if img.shape[2] == 2:
        img = gray2rgb(img)
      elif img.shape[2] == 4:
        img = rgba2rgb(img)
    return np.float32(img)

def transform_img(img):
    transform = transforms.Compose([transforms.ToTensor(), transforms.Resize((224,224)),
                    transforms.Normalize((0.5,0.5,0.5), (0.5,0.5,0.5)), 
                    transforms.RandomHorizontalFlip(),
                    transforms.RandomCrop(224, padding=8, padding_mode='reflect')])
    return transform(rgb_img(img))



device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

app = Flask(__name__)


#This is to force redirect from HTTP://x to HTTPS://x. 
@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        print("HI")
        code = 301
        return redirect(url, code=code)

sslify = SSLify(app)





# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('../public', 'index.html')

# Submit data
@app.route("/submit")
def submit():
    return send_from_directory('../public', 'index.html')

# Try it out! 
@app.route("/tryit")
def tryit():
    return send_from_directory('../public', 'index.html')

# BTS
@app.route("/behindthescenes")
def bts():
    return send_from_directory('../public', 'index.html')

@app.route("/generate")
async def generate():
    IMG_FILE = "gens/gen.png"

    with open('faol-model.pkl', 'rb') as f:
     G = pickle.load(f)['G_ema']
    z = torch.randn([1, G.z_dim])    # latent codes
    c = None                                # class labels (not used in this example)
    G = G.float()
    img = G(z, c, force_fp32=True)                           # NCHW, float32, dynamic range [-1, +1], no truncation

    img = (img.permute(0, 2, 3, 1) * 127.5 + 128).clamp(0, 255).to(torch.uint8)
    PIL.Image.fromarray(img[0].cpu().numpy(), 'RGB').save(f"../public/{IMG_FILE}")

    # Success = DONE. 
    ret_json = {"success": "False", "imgFile": "IMG_FILE"}
    return jsonify(
        success=False,
        imgFile=IMG_FILE
    )
    #return IMG_FILE 

# https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/
def is_file_ext_allowed(fileName):
    ALLOWED_EXT = ["png", "jpg", "jpeg"]
    return '.' in fileName and \
            fileName.rsplit('.', 1)[1].lower() in ALLOWED_EXT


@app.route("/saveUpload", methods=['POST', 'GET'])
def saveUpload():
    # uncomment try catch block later
    try:
        DATASET_FOLDER = "user_images"
        if(request.method == 'POST'):
            image = request.files['image']
            img_threshold = 0.5

            #image = Image.open(io.BytesIO(image.read()))
            model_img = transform_img(Image.open(io.BytesIO(image.read()))).unsqueeze(0)
            face_model = resnet50(pretrained=False)
            face_model.fc = torch.nn.Sequential(
                torch.nn.Linear(in_features=face_model.fc.in_features, out_features=1),
                torch.nn.Sigmoid()
            )
            face_model.load_state_dict(torch.load("FACE_MODEL_25.pth", map_location=device), strict=False)

            #face_model.eval()
            pred = face_model(model_img)

            print(pred)
            if(pred >= img_threshold):
                if(is_file_ext_allowed(image.filename)):
                    fileName = secure_filename(image.filename)

                    image.seek(0)
                    image.save(os.path.join(DATASET_FOLDER, id_img(fileName)))

                    return jsonify(
                        success=True,
                        err_id=None
                    )   
            else:
                return jsonify(
                    success=False,
                    err_id="ERR1"
                )  

        # If all other conditions failed, this failed. 
        return jsonify(
            success=False,
            err_id="ERR0"
        )
    except Exception as e:
        print(e)
        return jsonify(
            success=False,
            err_id="ERR2"
        )

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('../public', path)


@app.route("/rand")
def rand():
    return str(random.randint(0, 100))

if __name__ == "__main__":
    context = ssl.SSLContext()
    app.run(host="0.0.0.0", port=443, debug=True, ssl_context="adhoc")
