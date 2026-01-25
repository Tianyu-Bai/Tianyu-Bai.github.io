import os

def clean_content(content):
    """
    清理静态网页模板可能带有的 YAML Front Matter (--- ... ---)
    并确保内容前后没有多余空格
    """
    content = content.strip()
    if content.startswith('---'):
        # 找到第二个 --- 的位置并截取之后的内容
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2].strip()
    return content

if __name__ == '__main__':
    _header = '# 👋 Hi, I\'m Tianyu Bai'
    # 你的背景：达特茅斯 PhD Innovation Fellow
    base_dir = '../_pages/includes/'
    
    # 定义要拼接的模块
    files = ['intro.md', 'homepage.md', 'news.md', 'pub_short.md', 'honors.md']
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(_header + '\n\n')
        
        for file_name in files:
            path = os.path.join(base_dir, file_name)
            if os.path.exists(path):
                raw_text = open(path, 'r', encoding='utf-8').read()
                # 执行清理逻辑
                clean_text = clean_content(raw_text)
                if clean_text:
                    f.write(clean_text)
                    # 【核心修复】每个模块之后强制加两个换行符，确保 Markdown 解析正常
                    f.write('\n\n---\n\n') 
            else:
                print(f"警告: 找不到文件 {file_name}")

    print("README.md 拼接完成，已针对 GitHub Profile 渲染优化。")
