from flask import Flask, request, jsonify
from qa_engine import initialize_engine

app = Flask(__name__)
query_engine = initialize_engine()

@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        data = request.get_json()
        query = data.get("query", "")
        
        if not query:
            return jsonify({"error": "Query field is required"}), 400

        response = query_engine.query(query)
        return jsonify({
            "query": query,
            "response": str(response)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
