"""
This module is a Flask application for detecting emotions in text.

It provides an endpoint `/emotionDetector` that accepts text input and
returns the detected emotions along with their scores. The dominant emotion
is also identified and returned.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Handle requests to the /emotionDetector endpoint.

    Retrieves the text to analyze from the request arguments, processes it
    using the emotion_detector function, and returns the detected emotions
    and their scores. If the input is invalid, an error message is returned.

    Returns:
        str: A formatted string with the detected emotions and their scores,
             or an error message if the input is invalid.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_detect = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_detect)

    # Extract the score from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the label is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the emotion and score
    return (
    f"For the given statement, the system response is 'anger': {anger_score}, "
    f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and "
    f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
)

@app.route("/")
def render_index_page():
    """
    Render the index page.

    Returns:
        str: The rendered HTML content for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
