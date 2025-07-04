# from agents.simple_react_agent import research_agent

# if __name__ == "__main__":
#     # This is just to ensure that the module can be run directly for testing purposes.
#     print("Research Agent is ready to use.")
#     prompt = input("Enter your research query: ")
#     response = research_agent.invoke({"messages": [{"role": "user", "content": prompt}]})
#     # for chunk in research_agent.stream({"messages": [{"role": "user", "content": prompt}]}):
#     #     print(chunk, end='', flush=True)
#     print("Response from Research Agent:", response['messages'][-1])


from server import app as server_app

if __name__ == "__main__":
    # This is just to ensure that the module can be run directly for testing purposes.
    print("Starting server...")
    server_app.run(debug=True, host='0.0.0.0', port=5000)
    # The server will be accessible at http://localhost:5000/api/livecheck