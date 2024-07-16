"""
Emotion Detection Module

This module provides functionality for detecting emotions from text data.
It utilizes a pre-trained model to analyze input text and categorize the
emotional tone. The module includes functions for preprocessing text,
making predictions, and formatting results.

Example usage:
    from EmotionDetection.emotion_detection import detect_emotion
    result = detect_emotion("I am very happy today!")

Author: Konstantinos Mixios
Date: 2023-07-16
"""

import requests


def emotion_detector(text_to_analyze):
    """
    From a text get the feeling of it

    Args:
        text_to_analyze (string): Any phrase

    Returns:
        dict: Percentage of the feeling detected.
    """

    if not text_to_analyze:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/' + \
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()

        emotions = {
            'anger': data['emotionPredictions'][0]['emotion']['anger'],
            'disgust': data['emotionPredictions'][0]['emotion']['disgust'],
            'fear': data['emotionPredictions'][0]['emotion']['fear'],
            'joy': data['emotionPredictions'][0]['emotion']['joy'],
            'sadness': data['emotionPredictions'][0]['emotion']['sadness']
        }
        print(emotions)

        dominant_emotion = max(emotions, key=emotions.get)

        emotions['dominant_emotion'] = dominant_emotion

        return emotions

    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }


if __name__ == '__main__':
    print(emotion_detector(" I am so happy I am doing this"))
