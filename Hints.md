## random:  https://github.com/NataSola/python-summary/blob/master/docs/random.rst

**random.random()** — возвращает псевдослучайное число от 0.0 до 1.0

**random.uniform(<Начало>, <Конец>)** — возвращает псевдослучайное вещественное число в диапазоне от <Начало> до <Конец>:

**random.shuffle(<Список>)** — перемешивает последовательность (изменяется сама последовательность). Поэтому функция не работает для неизменяемых объектов. 

**random.choice(<Последовательность>)** — возвращает случайный элемент из любой последовательности (строки, списка, кортежа)

**random.randrange(<Начало>, <Конец>, <Шаг>)** — возвращает случайно выбранное число из последовательности.


## генерация списка https://pythonchik.ru/osnovy/spiski-v-python

    >>> c = [c + d for c in 'list' if c != 'i' for d in 'spam' if d != 'a']
    >>> print(c)
    ['ls', 'lp', 'lm', 'ss', 'sp', 'sm', 'ts', 'tp', 'tm']

## Список в обратном порядке

    >>> elements = [1, 2, 3, 4, 5, 6]
    >>> elements.reverse()

    >>> print(elements)
    [6, 5, 4, 3, 2, 1]

## Перевод списка в другой формат

    >>> fruits = ["яблоко", "груша", "ананас"]

    >>> print(', '.join(fruits))
    яблоко, груша, ананас

## Количество уникальных строк

    >>> words = ["one", "two", "one", "three", "one"]
    >>> len(set(words))
    3

    
## Перевернуть строку:
    >>> str = str[::-1]