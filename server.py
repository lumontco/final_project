''' Docstring required to improve pylint evaluation
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector


#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' This module is required server-side to run the app.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the label and score from the response
    customer_response = response
    # Return a formatted string with the emotion label and score
    if customer_response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is {customer_response}."
            .replace('{','').replace('}',''))

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
