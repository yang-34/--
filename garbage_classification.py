# 导入GUI库
import tkinter as tk
from tkinter import ttk, messagebox

# 垃圾分类数据库（字典结构）
# 键：垃圾类别名称，值：该类别包含的物品列表
GARBAGE_DB = {
    "可回收物": ["纸张", "塑料瓶", "玻璃", "金属", "布料"],
    "有害垃圾": ["电池", "药品", "灯管", "油漆桶", "杀虫剂"],
    "厨余垃圾": ["剩饭", "果皮", "菜叶", "骨头", "茶叶渣"],
    "其他垃圾": ["卫生纸", "陶瓷", "尿布", "烟蒂", "灰土"]
}

class GarbageApp:
    def __init__(self, master):
        self.master = master
        master.title("智能垃圾分类系统 v1.0")  # 设置窗口标题
        
        # 初始化界面组件
        self.create_widgets()
    
    def create_widgets(self):
        """创建并布局所有GUI组件"""
        # 输入提示标签
        lbl_title = ttk.Label(self.master, text="请输入垃圾物品名称：", font=('微软雅黑', 12))
        lbl_title.pack(pady=10)  # 垂直间距10像素
        
        # 文本输入框
        self.entry = ttk.Entry(self.master, width=30)
        self.entry.pack(pady=5)
        
        # 分类按钮（绑定点击事件）
        btn_classify = ttk.Button(self.master, text="分类识别", command=self.classify)
        btn_classify.pack(pady=5)
        
        # 结果展示文本框
        self.result_text = tk.Text(self.master, 
                                 height=8,       # 8行高度
                                 width=40,       # 40字符宽度
                                 font=('宋体', 11), 
                                 wrap=tk.WORD)   # 按单词换行
        self.result_text.pack(pady=10, padx=20)  # 水平和垂直边距
        
        # 设置窗口背景色
        self.master.configure(bg='#F0F0F0')  # 浅灰色背景
    
    def classify(self):
        """执行分类的核心逻辑"""
        item = self.entry.get().strip()  # 获取并清理输入
        if not item:
            messagebox.showwarning("提示", "请输入要分类的物品名称！")
            return
        
        # 遍历数据库查找匹配项
        found = False
        for category, items in GARBAGE_DB.items():
            if item in items:
                result = f"物品 '{item}' 属于：\n【{category}】\n\n处理建议：{self.get_tips(category)}"
                found = True
                break
        
        # 未找到时的默认提示
        if not found:
            result = f"未找到 '{item}' 的分类信息\n建议参考最新垃圾分类标准"
        
        self.show_result(result)
    
    def get_tips(self, category):
        """获取分类对应的处理建议"""
        tips = {
            "可回收物": "请保持清洁干燥，避免污染",
            "有害垃圾": "轻放轻投，密封处理",
            "厨余垃圾": "滤干水分，去除包装",
            "其他垃圾": "尽量沥干水分后投放"
        }
        return tips.get(category, "")
    
    def show_result(self, text):
        """更新结果显示区域"""
        self.result_text.delete(1.0, tk.END)  # 清空现有内容
        self.result_text.insert(tk.END, text)  # 插入新内容
        # 设置文本居中显示
        self.result_text.tag_add('center', 1.0, tk.END)
        self.result_text.tag_configure('center', justify='center')

# 程序入口
if __name__ == "__main__":
    root = tk.Tk()              # 创建主窗口
    root.geometry("400x350")    # 设置初始窗口尺寸
    app = GarbageApp(root)      # 初始化应用实例
    root.mainloop()             # 启动主事件循环