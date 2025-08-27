from flask import Flask, request, jsonify
import fitz  # PyMuPDF
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000","https://skillsync-ebon.vercel.app"])

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume uploaded"}), 400
    
    file = request.files['resume']   # frontend sends "resume"
   

    # Open PDF with PyMuPDF
    doc = fitz.open(stream=file.read(), filetype="pdf")

    text = ""
    for page in doc:
        text += page.get_text("text")
    print(text)

    return jsonify({
        "resume_text": text
        
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


# source venv/bin/activate