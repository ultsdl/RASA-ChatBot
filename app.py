from flask import Flask, redirect, url_for, request, render_template
import requests
import json
import os

app = Flask(__name__, template_folder= 'Template')
context_set = ""

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        val = str(request.args.get('text'))
        user_id = str(request.args.get('name'))
        data = json.dumps({"sender": user_id,"message": val})
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
        res = res.json()
        
        if len(res)==1:
          val = res[0]['text']
          return render_template('index.html', val=val)
        elif len(res)==2:
          val = res[0]['text']
          image = res[1]['text']
          print(image)
          return render_template('index.html', val=val, image=image)
        


if __name__ == '__main__':
  app.run(debug=True)
