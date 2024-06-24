import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt

def load_stopwords(filepath='stop.txt'):
    stopwords = set()
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if word:  # 只添加非空的行
                stopwords.add(word)
    return stopwords

def read_file(filename):
    filename = f'in/{filename}.txt'
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    return content

def cut(content, stopwords=load_stopwords()):
    if stopwords is None:
        stopwords = set()
    words = jieba.cut(content, cut_all=False)
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)

def gen_fig(text, cloudname='wordcloud'):
    wordcloud = WordCloud(
        font_path='SimHei.ttf', width=800, height=400, background_color='white'
        ).generate(text)
    cloudname = f'out/{cloudname}.png'
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(cloudname)
    # plt.show()

def main(name):
    content = read_file(name)
    gen_fig(
        text = cut(content),
        cloudname = name
    )

if __name__ == "__main__":
    main('test')
