import random

'''
input: int -> count of jokes number which need to build
output: list -> built jokes
description: there is five different nouns, adverbs and adjectives for jokes. User may choose how much jokes he need
to get, then function will randomly build jokes and will return them with list.
'''


def get_jokes(jokes_count: int):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    output_list = []
    if jokes_count > len(nouns):
        return "Количество запрашиваемых шуток превышает количество вариантов для составления шуток"
    for i in range(jokes_count):
        random_num = random.randint(0, len(nouns) - 1)
        random_noun = nouns[random_num]
        nouns.pop(random_num)

        random_num = random.randint(0, len(adverbs) - 1)
        random_adverb = adverbs[random_num]
        adverbs.pop(random_num)

        random_num = random.randint(0, len(adjectives) - 1)
        random_adjective = adjectives[random_num]
        adjectives.pop(random_num)

        output_list.append(random_noun + " " + random_adverb + " " + random_adjective)

    return output_list
