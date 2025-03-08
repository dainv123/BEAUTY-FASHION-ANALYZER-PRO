import cv2
import numpy as np
from deepface import DeepFace
from suggestions import get_beauty_suggestion, get_fashion_suggestion
import logging

logger = logging.getLogger(__name__)

def analyze_image(image_path, suggestion=None):
    logger.debug(f"Analyzing image: {image_path}")
    img = cv2.imread(image_path)
    if img is None:
        logger.error("Cannot read image")
        return {"error": "Không thể đọc ảnh"}

    try:
        # Thêm timeout để tránh treo
        analysis = DeepFace.analyze(img_path=image_path, actions=['age', 'emotion'], enforce_detection=False, silent=True)
        if not analysis or len(analysis) == 0:
            logger.warning("No face detected")
            nhan_sac = ["Không thể phân tích khuôn mặt. Tải ảnh rõ mặt hơn."]
        else:
            age = analysis[0]['age']
            dominant_emotion = analysis[0]['dominant_emotion']
            age_group = "young_age" if age < 35 else "mature_age"
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            brightness = np.mean(gray)
            skin_type = "bright_skin" if brightness > 100 else "dark_skin"
            nhan_sac = get_beauty_suggestion(skin_type, age_group, suggestion)
            logger.debug(f"Beauty analysis: {nhan_sac}")
    except Exception as e:
        logger.error(f"DeepFace error: {str(e)}")
        nhan_sac = [f"Không thể phân tích khuôn mặt: {str(e)}. Tải ảnh rõ mặt hơn."]

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue = np.mean(hsv[:,:,0])
    color_type = "warm_colors" if hue < 30 else "cool_colors"
    style = "casual_style" if brightness > 80 else "formal_style"
    fashion = get_fashion_suggestion(color_type, style, suggestion)
    logger.debug(f"Fashion analysis: {fashion}")

    result = {
        "nhan_sac": nhan_sac,
        "fashion": fashion
    }
    if suggestion:
        result["suggestion"] = f"Đã áp dụng gợi ý: {suggestion}"

    return result