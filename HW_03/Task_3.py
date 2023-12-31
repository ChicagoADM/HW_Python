# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

text = """Python - высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим \
управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, \
а также на обеспечение переносимости написанных на нём программ. Язык является полностью объектно-ориентированным в \
том плане, что всё является объектами. Необычной особенностью языка является выделение блоков кода пробельными отступами.\
Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации.\
Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов. Недостатками языка являются\
зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом,\
написанным на компилируемых языках, таких как C или С++"""


for symbol in ".,;:-":
    text = text.replace(symbol, " ")

words_list = text.split()
words_set = set(words_list)

word_dict = {}

for word in words_set:
    word_dict[word] = words_list.count(word)

sorted_tuple = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

for i in range(10):
    print(f"({') встречается в тексте:  '.join(str(item) for item in sorted_tuple[i])} раз")