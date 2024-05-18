"""
How it works:
- First a wikipedia scraper script finds a random wikipedia article title
- Then a random fair variable decides whether the content will be AI generated or scraped off wikipedia
- If AI generated, the title previously generated is passed to Gemini within a prompt
- Otherwise the abstract of the wikipedia article is extracted
- The user chooses their guess and gets verified
Additional: some things in wikipedia make it obvious that it is from wikipedia
Either try to find a way to filter those
OR ask gemini to mimic wikipedia's style
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from start_game import Game
import json

class API_Connector:

    def __init__(self):

        self.app = Flask(__name__)
        self.app.debug = True
        self.cors = CORS(self.app)
        self.game = Game()
        self.stats_path = 'stats.json'
    


    def start(self):

        self.app.route('/start_game', methods=['GET'])(self.start_game)
        self.app.route('/get_result', methods=['POST'])(self.get_result)
        self.app.route('/get_stats', methods=['GET'])(self.get_stats)
        
        self.app.run(host='0.0.0.0', port=4091, threaded=True)  # 4091

    def start_game(self):
        self.game.get_random_option()
        self.game.get_wiki_title()
        paragraph = self.game.get_paragraph()
        return jsonify({'paragraph': paragraph})


    def get_result(self):
        response = request.json['answer']
        result = self.game.get_result(guess=response)
        with open(self.stats_path, 'r') as file:
            file_contents = file.read()
            stats = json.loads(file_contents)

        if result:
            stats['correct_guesses'] += 1
        else:
            stats['wrong_guesses'] += 1

        with open(self.stats_path, 'w') as file:
            json.dump(stats, file)

        return jsonify({'result':result})
    
    def get_stats(self):
        with open(self.stats_path, 'r') as file:
            file_contents = file.read()
            stats = json.loads(file_contents)
        return stats
    




if __name__ == "__main__":
    app = API_Connector()
    app.start()
