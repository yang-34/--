# 导入Flask及相关模块
from flask import Flask, jsonify, request, render_template
# 从本地模块导入垃圾分类数据库
from garbage_classification import GARBAGE_DB

# 初始化Flask应用
app = Flask(__name__)

# 根路由，返回前端页面
@app.route('/')
def index():
    return render_template('index.html')

# 分类接口，处理POST请求
@app.route('/classify', methods=['POST'])
def classify():
    # 从JSON数据中获取物品名称
    item = request.json.get('item', '').strip()
    
    # 遍历数据库查找匹配分类
    for category, items in GARBAGE_DB.items():
        if item in items:
            # 找到分类时返回JSON结果
            return jsonify({
                'category': category,      # 分类名称
                'tips': get_tips(category),# 处理建议
                'found': True              # 查询成功标志
            })
    
    # 未找到时返回失败状态
    return jsonify({'found': False})

# 获取分类对应的处理建议
def get_tips(category):
    # 建议字典（可扩展）
    tips = {
        "可回收物": "请保持清洁干燥，避免污染",
        "有害垃圾": "轻放轻投，密封处理",
        "厨余垃圾": "滤干水分，去除包装",
        "其他垃圾": "尽量沥干水分后投放"
    }
    return tips.get(category, "")

# 主程序入口
if __name__ == '__main__':
    import webbrowser
    import threading
    
    # 自动打开浏览器函数
    def open_browser():
        webbrowser.open('http://localhost:5000/')
        
    # 创建定时器（1秒后打开浏览器）
    threading.Timer(1.0, open_browser).start()
    # 启动Flask开发服务器
    app.run(debug=True, port=5000, use_reloader=False)