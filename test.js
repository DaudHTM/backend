import fs from "fs"
import fetch from "node-fetch"
import FormData from "form-data";


async function uploadAudio(variableName, filePath) {

  const audioFile = fs.createReadStream(filePath);

  const formData = new FormData();
  formData.append('name', variableName);
  formData.append('audio_file', audioFile);

  try {
    const response = await fetch('http://127.0.0.1:5000/upload_audio', {
      method: 'POST',
      body: formData,
      headers: formData.getHeaders()
    });
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  }
}

uploadAudio('Jaaaden', './jad.mp3');
