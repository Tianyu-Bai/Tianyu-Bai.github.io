import json
import os

if __name__ == '__main__':
    _header = '## Hi there 👋'
    # 设定素材文件夹路径
    base_dir = '../_pages/includes/'
    # 设定爬虫产生的数据文件路径
    # 注意：这里假设 JSON 文件在 google_scholar_crawler/results/ 目录下
    data_file = '../google_scholar_crawler/results/gs_data.json'
    
    # 1. 尝试读取引用数据
    citations = "N/A"
    h_index = "N/A"
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r') as f:
                data = json.load(f)
                # 假设 JSON 格式中有 'total_citations' 和 'h_index' 字段
                citations = str(data.get('total_citations', 'N/A'))
                h_index = str(data.get('h_index', 'N/A'))
        except Exception as e:
            print(f"Error reading JSON: {e}")

    # 2. 读取素材并进行变量替换
    def read_and_replace(filename):
        path = os.path.join(base_dir, filename)
        if os.path.exists(path):
            content = open(path).read().strip()
            # 将模板中的 {{citations}} 替换为实际数字
            content = content.replace('{{citations}}', citations)
            content = content.replace('{{h_index}}', h_index)
            return content
        return ""

    _intro = read_and_replace('intro.md')
    _homepage = read_and_replace('homepage.md')
    _pub = read_and_replace('pub_short.md')
    _news = read_and_replace('news.md')

    # 3. 拼接并写入 README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(_header)
        f.write('\n\n')
        f.write(_intro)
        if _homepage:
            f.write('\n\n##')
            f.write(_homepage)
        if _news:
            f.write('\n\n##')
            f.write(_news)
        if _pub:
            f.write('\n\n##')
            f.write(_pub)
            
    print(f"Successfully updated README.md with {citations} citations.")
