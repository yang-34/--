from flask import Flask, jsonify, request, render_template
from garbage_classification import GARBAGE_DB

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    item = request.json.get('item', '').strip()
    
    for category, items in GARBAGE_DB.items():
        if item in items:
            return jsonify({
                'category': category,
                'tips': get_tips(category),
                'found': True
            })
    
    return jsonify({'found': False})

def get_tips(category):
    tips = {
        "可回收物": "请保持清洁干燥，避免污染",
        "有害垃圾": "轻放轻投，密封处理",
        "厨余垃圾": "滤干水分，去除包装",
        "其他垃圾": "尽量沥干水分后投放"
    }
    return tips.get(category, "")

if __name__ == '__main__':
    import webbrowser
    import threading
    
    def open_browser():
        webbrowser.open('http://localhost:5000/')
        
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True, port=5000, use_reloader=False)