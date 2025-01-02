"""
Flask app for emotion detection from text.

It provides an endpoint to analyze text for emotions like anger, disgust, fear, joy, sadness, 
and dominant emotion, using the EmotionDetection module.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to analyze the emotions from the provided text.
    Returns a response with emotion scores or an error message.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)

    anger_score = response.get("anger", 0)
    disgust_score = response.get("disgust", 0)
    fear_score = response.get("fear", 0)
    joy_score = response.get("joy", 0)
    sadness_score = response.get("sadness", 0)
    dominant_emotion = response.get("dominant_emotion", "")

    # Check if any emotion score is None
    if None in [anger_score, disgust_score, fear_score, joy_score, sadness_score, dominant_emotion]:
        return "Invalid text! Please try again!."

    return {
    f"For the given statement, the system response is 'anger': {anger_score}, "
    f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} "
    f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."}


@app.route("/")
def render_index_page():
    """
    Renders the index HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
