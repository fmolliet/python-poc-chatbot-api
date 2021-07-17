#Importando o modulo flask
import json
import os
from bot import Bot
from flask import Flask, request, jsonify, Response, render_template

app = Flask(__name__)
app.config["DEBUG"] = True
chatbot = Bot().train()

@app.route('/chat',  methods=["POST"])
def classify():
    try:
        res = request.json
        if res.get('text') and res['text'] != '':
            ret = chatbot.process( res['text'] )

            #resp = request.get_json(silent=True)
            return jsonify({"response":ret})
        else: 
            return jsonify( {"message": "Formato inválido de requisição" }), 400
            #print(auth)
    except Exception as err:
        return f"{err.__class__.__name__}: {err}"
     

@app.route("/", methods=["GET", "POST"])
def health():
    return jsonify( {"status": "UP" })

port = int(os.environ.get('PORT', 5000))
app.run(host = '0.0.0.0', port = port)
