import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting predictions emotion from the response
    emotion = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion_score = 0
    for k,v in emotion.items():
        if v > dominant_emotion_score:
            dominant_emotion = k
            dominant_emotion_score = v
    emotion['dominant_emotion'] = dominant_emotion

    # Return the response text from the API
    return emotion