from analyzer import Analyzer
import os

# Test data
test_transcript = [
    "Hello everyone, welcome to the project kickoff.",
    "Today we are discussing the integration of Gemini API.",
    "John will handle the backend integration.",
    "Sarah will work on the frontend UI.",
    "We decided to use the 1.5-flash model for cost efficiency.",
    "The deadline for the first draft is next Friday."
]

analyzer = Analyzer()
print("Starting analysis...")
result = analyzer.analyze(test_transcript)
print("Analysis Result:")
print(result)
