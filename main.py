import os
from src.classify_LLM import organize_files, init_client

# 定义文件夹名称
RESULT_FOLDER = "分类结果"
TO_CLASSIFY_FOLDER = "需要分类的文件"

# 定义标签列表
PREDEFINED_LABELS = ["政治与社会观察", "学习与生活方法论", "大模型与机器学习", "商业与金融、经济"] # 在这里修改你想要的标签

# 定义API密钥、基础URL和模型
API_KEY = "sk-xxx" # 在这里修改你想要的api_key
BASE_URL = "https://api.deepseek.com" # 在这里修改你想要的base_url
MODEL = "deepseek-chat" # 在这里修改你想要使用的模型

# 检查并创建必要的文件夹
def create_folders():
    folders = [RESULT_FOLDER, TO_CLASSIFY_FOLDER]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"已创建文件夹: {folder}")
        else:
            print(f"文件夹已存在: {folder}")

# 主函数
def main():
    # 创建必要的文件夹
    create_folders()
    
    # 初始化客户端
    client = init_client(API_KEY, BASE_URL)
    
    # 调用classify模块中的organize_files函数，并传递标签列表、客户端和模型
    print("开始整理文件...")
    organize_files(TO_CLASSIFY_FOLDER, RESULT_FOLDER, PREDEFINED_LABELS, client, MODEL)
    print("文件整理完成!")

if __name__ == "__main__":
    main()
