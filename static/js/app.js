function classifyItem() {
    const input = document.getElementById('itemInput');
    const resultDiv = document.getElementById('result');
    
    if (!input.value.trim()) {
        resultDiv.innerHTML = '<p class="error">请输入要分类的物品名称！</p>';
        return;
    }

    fetch('/classify', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({item: input.value})
    })
    .then(res => res.json())
    .then(data => {
        if (data.found) {
            resultDiv.innerHTML = `
                <h3>${input.value}</h3>
                <div class="result-category">${data.category}</div>
                <p class="tips">${data.tips}</p>
            `;
        } else {
            resultDiv.innerHTML = `
                <p class="warning">未找到分类信息</p>
                <p>建议参考最新垃圾分类标准</p>
            `;
        }
    })
    .catch(() => {
        resultDiv.innerHTML = '<p class="error">分类服务暂不可用</p>';
    });
}

// 输入框回车事件
document.getElementById('itemInput').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') classifyItem();
});