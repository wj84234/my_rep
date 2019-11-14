def word_count(article_path):
    with open(article_path, 'rb') as infile:
        article = infile.read().decode('utf-8')

    punctuation = ",)(.;‘—:?/\’\”\“"

    for char in punctuation:
        article = article.replace(char, "").replace('\r', ' ').replace('\n', ' ').replace('\u200a', ' ').replace('-', ' ')

    article_list = article.lower().split(' ')

    my_dict = dict.fromkeys(article_list)

    for word in my_dict:
        my_dict.update({word: article_list.count(word)})

    my_dict.pop('', None)

    import operator

    return sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)


for key, value in word_count('article_python.txt'):
    print('The word: "' + key + '" appears ' + str(value) + ' time(s) in the given text.')
