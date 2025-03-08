from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from analyze import analyze_image
import logging

app = Flask(__name__, static_folder='frontend', template_folder='frontend')
CORS(app)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    logger.debug("Received request to /analyze")
    if 'image' not in request.files:
        logger.error("No image uploaded")
        return jsonify({"error": "Không có ảnh được gửi"}), 400

    file = request.files['image']
    suggestion = request.form.get('suggestion', None)
    logger.debug(f"Suggestion received: {suggestion}")

    temp_path = "temp_image.jpg"
    try:
        file.save(temp_path)
        logger.debug(f"Image saved to {temp_path}")
    except Exception as e:
        logger.error(f"Failed to save image: {str(e)}")
        return jsonify({"error": f"Không thể lưu ảnh: {str(e)}"}), 500

    try:
        result = analyze_image(temp_path, suggestion)
        logger.debug(f"Analysis result: {result}")
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        os.remove(temp_path)
        return jsonify({"error": f"Lỗi phân tích: {str(e)}"}), 500

    if os.path.exists(temp_path):
        os.remove(temp_path)
        logger.debug("Temporary image removed")

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)