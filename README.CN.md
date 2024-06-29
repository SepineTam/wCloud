# wCloud
这是一个基于jieba和wordcloud制作词云的项目。

# 如何使用

## 1.获取项目
```bash
git clone https://github.com/sepinetam/wCloud.git
```

## 创建虚拟环境并安装依赖
```bash
cd wCloud
# macOS和Linux用户使用
python -m venv venv
source venv/bin/activate
# windows用户使用
# python -m venv venv
# cmd中
# venv\Scripts\activate.bat
# powershell中
# venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
有关python虚拟环境，详细参考[文档](https://docs.python.org/zh-cn/3.9/library/venv.html#creating-virtual-environments)

## 使用

1. 修改/导入txt文本到in文件夹
2. 确定使用的字体(默认为黑体)
3. 运行脚本

### 使用示例
示例文件为```"in/example.txt"```

停词文件为```"stop.txt"```

返回文件为```"out/example.png"```

字体选择宋体

```bash
python main.py example stop SimSun
```

### 示例解释

- 传入的文件为```"in/example.txt"```
- 停词的文件为```"stop.txt"```
- 返回的词云图为```"out/example.png"```
- 选择的字体为```"fonts/SimSun.ttf"```

### 参数说明
```bash
python main.py file stop font
```

- 参数1(file): 传入文件的名字(".txt"可有可无)，如不传入则默认为"test.txt"
- 参数2(stop): 停词文件(".txt"可有可无)，如不传入则默认为"stop.txt"
- 参数3(font): 字体(".ttf"可有可无)，如不传入则默认为"SimHei.ttf"

# 致谢
## 中文字体提供
感谢恒星中国[@StellarCN](https://github.com/StellarCN)提供的[字体SimHei](fonts/SimHei.ttf)，期待恒星中国发展越来越好。

## 需求提供
感谢上海大学社会学同学[顾萌](mailto:esme2004dash@163.com)提供的需求，让我能想起来写这么个小工具。

