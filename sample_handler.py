"""Sample aws lambda function."""
import json

def handler(event, context):
"""Returns sample data with 200 response."""
    data = {
        "response" : 200,
        "message" : "Thanks for creating a demo lambda function"
    }

    return data
