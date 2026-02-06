from flask import Flask, jsonify, request

app = Flask(__name__)

# GET
# 1. 전체 게시글을 불러오는 API
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    data = {
        'result': 'success',
        'data': {'feed1': 'data1', 'feed2': 'data2'}
    }
    return jsonify(data)

# 2. 특정 게시물을 불러오는 API
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    data = {
        'result': 'success',
        'data': {'feed_id': feed_id}
    }
    return jsonify(data)

# POST
# 1. 게시물을 작성하는 API
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    data = request.get_json()  # form 대신 JSON 사용
    name = data.get('name')
    age = data.get('age')

    return jsonify({
        'result': 'success',
        'data': {
            'name': name,
            'age': age
        }
    })

datas = [{"items": [{"name": "item1", "price": 10}]}]

@app.route('/api/v1/datas', methods=['GET'])  # 데코레이터 통일
def get_datas():
    return jsonify({
        'result': 'success',
        'data': datas
    })

@app.route('/api/v1/datas', methods=['POST'])  # 데코레이터 통일
def create_datas():
    data = request.get_json()
    new_data = {'items': data.get('items', [])}
    datas.append(new_data)

    return jsonify({
        'result': 'success',
        'data': new_data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
