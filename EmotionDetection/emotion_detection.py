import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
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
    else:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
if __name__=='__main__':
    print(emotion_detector(" I am so happy I am doing this"))
    