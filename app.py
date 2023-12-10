# from flask import Flask, request, jsonify
# from googlesearch import search
# import re

# app = Flask(__name__)

# def extract_names(suggestions):
#     # Extract names from suggestions (remove non-alphanumeric characters)
#     names = [re.sub(r'\W+', ' ', suggestion.split('-')[0]).strip() for suggestion in suggestions]
#     return names

# @app.route('/name-suggest', methods=['GET'])
# def name_suggest():
#     query = request.args.get('query')

#     if not query:
#         return jsonify({'error': 'Query parameter is missing'}), 400

#     try:
#         suggestions = list(search(query, num=5, stop=5, pause=2))
#         names = extract_names(suggestions)
#         return jsonify({'name_suggestions': names})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/<query>', methods=['GET'])
def autocomplete(query):
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={query}"
    response = requests.get(url)
    suggestions = response.json()[1]

    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)

