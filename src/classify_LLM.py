import os
import shutil
from openai import OpenAI  # 假设使用DeepSeek API

def init_client(api_key, base_url):
    """初始化并返回DeepSeek客户端"""
    return OpenAI(api_key=api_key, base_url=base_url)

def read_markdown_content(file_path, max_chars=200):
    """读取Markdown文件的标题和前200个字符"""
    with open(file_path, 'r', encoding='utf-8') as file:
        title = ""
        content = ""
        for line in file:
            if not title and line.startswith('# '):
                title = line.strip('# ').strip()
            else:
                content += line
                if len(content) >= max_chars:
                    break
    return title, content[:max_chars]

def get_file_label(title, content, predefined_labels, client, model):
    """使用DeepSeek API从预定义标签中选择文件标签"""
    labels_str = ", ".join(predefined_labels)
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": f"你是一个文件分类助手。请为给定的文件标题和内容从以下预定义标签中选择最合适的一个：{labels_str}。直接返回标签，不要添加任何额外的文字。"},
                {"role": "user", "content": f"文件标题: {title}\n\n文件内容前200字: {content}"}
            ],
            stream=False
        )
        label = response.choices[0].message.content.strip()
        print(f"API返回的标签: {label}")  # 调试输出
        return label if label in predefined_labels else "其他"
    except Exception as e:
        print(f"API调用出错: {e}")  # 调试输出
        return "其他"

def organize_files(source_folder, target_folder, predefined_labels, client, model):
    """根据Markdown文件标题和内容整理文件"""
    for filename in os.listdir(source_folder):
        if filename.endswith('.md'):
            file_path = os.path.join(source_folder, filename)
            title, content = read_markdown_content(file_path)
            label = get_file_label(title, content, predefined_labels, client, model)
            print(f"文件 {filename} 的标签: {label}")  # 调试输出
            
            # 创建标签文件夹
            label_folder = os.path.join(target_folder, label)
            os.makedirs(label_folder, exist_ok=True)
            
            # 复制文件
            shutil.copy(file_path, os.path.join(label_folder, filename))
            print(f"已将文件 {filename} 复制到 {label} 文件夹")

# 删除这里的使用示例，因为现在从main.py调用