from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant_emotion'], 'joy')

        # Test case for anger
        result1 = emotion_detector("I am really mad about this")
        self.assertEqual(result1['dominant_emotion'], 'anger')

        # Test case for disgust
        result1 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result1['dominant_emotion'], 'disgust')

        # Test case for sadness
        result1 = emotion_detector("I am so sad about this")
        self.assertEqual(result1['dominant_emotion'], 'sadness')

        # Test case for fear
        result1 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result1['dominant_emotion'], 'fear')

unittest.main()