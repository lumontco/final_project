import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create the payload with the text to be analyzed
    my_obj = { "raw_document": { "text": text_to_analyse } }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=my_obj, headers=header)

    # If the response status code is 200, parse the response from the API
    if response.status_code == 200:
        output_response = json.loads(response.text)
        output_response["emotionPredictions"][0]["emotion"]["dominant_emotion"] = max(
            output_response["emotionPredictions"][0]["emotion"],
            key=output_response["emotionPredictions"][0]["emotion"].get
            )
    # If the response status code is 400, build response and set all to None
    elif response.status_code == 400:
        output_response = dict()
        output_response["anger"] = None
        output_response["disgust"] = None
        output_response["fear"] = None
        output_response["joy"] = None
        output_response["sadness"] = None
        output_response["dominant_emotion"] = None
    
    return output_response
