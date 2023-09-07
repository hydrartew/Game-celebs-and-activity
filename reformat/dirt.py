import nltk

# загружаем список слов
words = nltk.corpus.reader.words('news')


# определяем уровень сложности каждого слова
def complexity(word):
    return nltk.metrics.perplexity(nltk.probability.CategoricalProbabilisticModel([word])).item()


word_complexity = [complexity(word) for word in words]
print(word_complexity)
