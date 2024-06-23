# 如果跑出来的图片中不显示中文，则把第19行的注释取消，并将20行进行注释
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取文件内容
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# 使用 jieba 进行中文分词
def jieba_cut(content):
    words = jieba.cut(content, cut_all=False)
    return ' '.join(words)

# 生成词云图
def generate_wordcloud(text):
    # wordcloud = WordCloud(font_path='simhei.ttf', width=800, height=400, background_color='white').generate(text)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('wordcloud.png')
    plt.show()

# 主函数
def main():
    content = read_file('interview.txt')
    text = jieba_cut(content)
    generate_wordcloud(text)

if __name__ == '__main__':
    main()
