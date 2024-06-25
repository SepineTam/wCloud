import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt


def load_stopwords(filepath='stop.txt'):
    stopwords = set()
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip()
            if word:
                stopwords.add(word)
    if stopwords is None:
        stopwords = set()
    return stopwords


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def cut_text(text, stopwords):
    words = jieba.cut(text, cut_all=False)
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)


def gen_fig(text_name, stopwords_path='stop.txt', font='SimHei.ttf'):
    name, file_type = text_name.split('.')

    in_path = f'in/{text_name}'
    out_path = f'out/{name}.png'

    text = read_file(in_path)
    stopwords = load_stopwords(stopwords_path)

    word = cut_text(text, stopwords)

    wordcloud = WordCloud(
        font_path=font, width=800, height=500, background_color='white'
    ).generate(word)

    plt.figure(figsize=plt.figaspect(0.5), facecolor='white')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(out_path)
    return out_path


if __name__ == '__main__':
    gen_fig('test.txt')
