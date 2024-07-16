"""
This module sets up a Flask web server for emotion detection.
It includes endpoints for rendering the main page and processing
emotion detection requests.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
        Endpoint to process emotion detection requests.
        Expects JSON input with a 'text' field and returns a
        JSON response with detected emotions and a formatted message.
    """
    data = request.get_json()
    text = data.get('text', '')
    emotions = emotion_detector(text)
    if emotions['dominant_emotion'] is None:
        formatted_response = "Invalid text! Please try again."
    else:
        formatted_response = (
            f"For the given statement, the system response is 'anger': {emotions['anger']}, "
            f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, \
             'joy': {emotions['joy']} "
            f"and 'sadness': {emotions['sadness']}. \
            The dominant emotion is {emotions['dominant_emotion']}."
        )

    return jsonify({"message": formatted_response})

@app.route('/')
def index():
    """
        Endpoint to render the main page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
