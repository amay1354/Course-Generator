#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from latest_ai_development2.crew import LatestAiDevelopment2

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

STATIC_CONTENT = """
Machine learning is a field of artificial intelligence that focuses on developing algorithms that allow computers to learn from and make predictions or decisions based on data. It includes supervised, unsupervised, and reinforcement learning. Supervised learning uses labeled data, while unsupervised learning finds hidden patterns in unlabeled data. Reinforcement learning involves agents that learn to make decisions through trial and error. Machine learning has wide applications in healthcare, finance, transportation, and more. Understanding model evaluation, overfitting, and the bias-variance tradeoff is essential for building effective models. Tools like Python, scikit-learn, and TensorFlow are popular in this field.
"""

def run():
    inputs = {
        'topic': 'Machine Learning',
        'content': STATIC_CONTENT,
        'current_year': str(datetime.now().year)
    }

    try:
        LatestAiDevelopment2().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    inputs = {
        "topic": "Machine Learning Fundamentals",
        "content": STATIC_CONTENT,
        "current_year": str(datetime.now().year)
    }
    try:
        LatestAiDevelopment2().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    try:
        LatestAiDevelopment2().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    inputs = {
        "topic": "Machine Learning Fundamentals",
        "content": STATIC_CONTENT,
        "current_year": str(datetime.now().year)
    }
    try:
        LatestAiDevelopment2().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


