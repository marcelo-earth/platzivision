from flask import request, jsonify, Response
import openai
import json
from openai import OpenAI

def chat():
    try:
        # TODO: Implementar chat de PlatziVision
        pass
    except Exception as e:
        print(f"Chat request failed: {str(e)}")
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500
