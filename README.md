一个使用深度求索的API进行文件分类的脚本

# 使用方法：
1.安装依赖：pip install -r requirements.txt
2.修改main.py中predefined_labels为你希望分类的标签
2.修改main.py中api_key和base_url，如果想要使用不同的模型，修改model
3.运行脚本：python main.py

# 未来计划：
1.使用大模型完成分类后可以自动导入到notion（但notion的api有单page上传的字符限制，所以现在先不急着做）