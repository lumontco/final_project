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

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    formatted_response["emotionPredictions"][0]["emotion"]["dominant_emotion"] = max(
        formatted_response["emotionPredictions"][0]["emotion"],
        key = formatted_response["emotionPredictions"][0]["emotion"].get
        )

    # Return the label and score in a dictionary
    return formatted_response
