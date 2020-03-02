from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



app.config['MONGO_DBNAME'] = 'new_articles'
app.config['MONGO_URI'] = 'mongodb+srv://{insertdb:password}@cluster0-ww9bp.mongodb.net/new_articles?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/api/sentiment', methods=['GET'])
def get_all_articles():
    articles = mongo.db.blogitem
    print(articles)
    output = []

    for q in articles.find():
        output.append({'title': q['title'], 
                        'snippet': q['snippet'],
                        'sentiment': q['sentiment'] })

    return jsonify({'result': output })


@app.route('/api/avg', methods=['GET'])
def get_avg():
    avg = mongo.db.avgitem
    output = []

    for q in avg.find():
        output.append({'avg': q['sentiment_avg'], 
                          'date': q['date'] })

    return jsonify({'result': output })

if __name__ == '__main__':
    app.run(host="0.0.0.0")