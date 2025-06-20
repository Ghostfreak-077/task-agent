from flask import Flask, jsonify, request
from flask_cors import CORS
from agents.simple_react_agent import research_agent

app = Flask(__name__)
CORS(app)

@app.route('/api/livecheck', methods=['GET'])
def status():
    return jsonify({"status": "ok", "message": "Server is running!"})

@app.route('/api/agent/invoke', methods=['POST'])
def invoke_agent():
    req = request.get_json()
    
    if not req or 'prompt' not in req:
        return jsonify({"error": "Invalid request"}), 400
    
    prompt = req['prompt']
    response = research_agent.invoke({"messages": [{"role": "user", "content": prompt}]})

    return jsonify({
        "status": "ok",
        "response": response['messages'][-1].content
    })