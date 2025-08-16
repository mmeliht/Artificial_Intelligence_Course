from flask import Flask , render_template , request
import pickle

app = Flask(__main__)

model = pickle.load(open('maas.pkl','rb'))
