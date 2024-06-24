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

def gen_fig(text, cloudname='wordcloud', font='SimHei.ttf'):
    wordcloud = WordCloud(
        font_path=font, width=800, height=400, background_color='white'
        ).generate(text)
    cloudname = f'out/{cloudname}.png'
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(cloudname)
    # plt.show()  # 显示化

def main(name, *args):
    content = read_file(name)
    if len(args) > 0:
        font = args[0]
    else:
        font = 'SimHei.ttf'
    gen_fig(
        text = cut(content),
        cloudname = name,
        font = font
    )

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        name = sys.argv[1]
        if '.txt' in name:
            name = name.split('.txt')[0]
        if len(sys.argv) > 2:
            font = sys.argv[2]
            if '.ttf' not in font:
                font = f"{font}.ttf"
            main(name, font)
        else:
            main(name)
    else:
        main("test")
