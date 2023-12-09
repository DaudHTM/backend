from flask import *
from elevenlabs import clone, generate, play

from pathlib import Path

from dotenv import load_dotenv
import os
load_dotenv()  

from elevenlabs import set_api_key
api = os.getenv("API")
set_api_key(api)

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/upload_audio', methods=['POST'])
def upload_audio():

    name = request.form.get('name')
    
    if 'audio_file' not in request.files:
        return jsonify({'error': 'No audio file part in the request'}), 400
    
    audio_file = request.files['audio_file']
    
    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if audio_file:
      
        filename = f"{name}.mp3"
        audio_file.save(os.path.join('./', filename))
        try:
            voice = clone(
            name=name,
            files=["./"+filename],
            )
        except:
            return jsonify({'error': 'Unknown error occurred'}), 500
        
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200

    return jsonify({'error': 'Unknown error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
