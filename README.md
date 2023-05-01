# Тренировка по алгоритмам 3.0

Планирую решить все задачи по алгоритмам от Яндекса. Программа курса:
[https://yandex.ru/yaintern/algorithm-training](https://yandex.ru/yaintern/algorithm-training)

## 1. Гистограмма

Задача #1. Гистограмма

Задается неопределенное количество строк.
Решение задачи: считаем словарем сколько раз какой символ встречался и делаем красивый вывод.

<details>
<summary>Условие задачи ...</summary>
Тут текст который вы хотим скрыть

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 64 мегабайт

Вовочка ломает систему безопасности Пентагона. Для этого ему понадобилось узнать, какие символы в секретных зашифрованных посланиях употребляются чаще других. Для удобства изучения Вовочка хочет получить графическое представление встречаемости символов. Поэтому он хочет построить гистограмму количества символов в сообщении. Гистограмма — это график, в котором каждому символу, встречающемуся в сообщении хотя бы один раз, соответствует столбик, высота которого пропорциональна количеству этих символов в сообщении.

### Формат входных данных

Входной файл содержит зашифрованный текст сообщения. Он содержит строчные и прописные латинские буквы, цифры, знаки препинания («.», «!», «?», «:», «-», «,», «;», «(», «)»), пробелы и переводы строк. Размер входного файла не превышает 10000 байт. Текст содержит хотя бы один непробельный символ. Все строки входного файла не длиннее 200 символов.Для каждого символа c кроме пробелов и переводов строк выведите столбик из символов «#», количество которых должно быть равно количеству символов c в данном тексте. Под каждым столбиком напишите символ, соответствующий ему. Отформатируйте гистограмму так, чтобы нижние концы столбиков были на одной строке, первая строка и первый столбец были непустыми. Не отделяйте столбики друг от друга. Отсортируйте столбики в порядке увеличения кодов символов.

### Формат выходных данных

Для каждого символа c кроме пробелов и переводов строк выведите столбик из символов «#», количество которых должно быть равно количеству символов c в данном тексте. Под каждым столбиком напишите символ, соответствующий ему. Отформатируйте гистограмму так, чтобы нижние концы столбиков были на одной строке, первая строка и первый столбец были непустыми. Не отделяйте столбики друг от друга. Отсортируйте столбики в порядке увеличения кодов символов.

### Пример

**input.txt**

```
Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.
```

**output.txt**

```
         #
         #
         #
         #
         #
         #         #
         #  #      #
      #  # ###  ####
      ## ###### ####
      ##############
      ##############  ##
#  #  ############## ###
########################
,.;ADTabdeghilmnorstuvwy
```

</details>

### [Решение](Гистограмма/)

## 2. Красивая строка

Метод двух указателей

Задача #2. Красивая строка

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 64 мегабайт

Красотой строки назовем максимальное число идущих подряд одинаковых букв. (красота строки abcaabdddettq равна 3)
Сделайте данную вам строку как можно более красивой, если вы можете сделать не более k операций замены символа.

## Формат входных данных

В первой строке записано одно целое число k (0 ≤ k ≤ 109)
Во второй строке дана непустая строчка S (|S| ≤ 2 ⋅ 105). Строчка S состоит только из маленьких латинских букв.

### Формат выходных данных

Выведите одно число — максимально возможную красоту строчки, которую можно получить.

### Примеры

**input.txt**

```
2
abcaz
```

**output.txt**

```
4
```

**input.txt**

```
2
helto
```

**output.txt**

```
3
```

</details>

### [Решение](Красивая_строка/)

## 3. Коллекционер Диего

Сортировка и бинарный поиск.

<details>
<summary>Условие задачи ...</summary>
Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 2 секунды

Ограничение по памяти: 256 мегабайт

Диего увлекается коллекционированием наклеек. На каждой из них написано число, и каждый коллекционер мечтает собрать наклейки со всеми встречающимися числами.

Диего собрал N наклеек, некоторые из которых, возможно, совпадают. Как-то раз к нему пришли K коллекционеров. i-й из них собрал все наклейки с номерами не меньшими, чем pi. Напишите программу, которая поможет каждому из коллекционеров определить, сколько недостающих ему наклеек есть у Диего. Разумеется, гостей Диего не интересуют повторные экземпляры наклеек.

### Формат входных данных

В первой строке содержится единственное число N (0 ≤ N ≤ 100 000) — количество наклеек у Диего.

В следующей строке содержатся N целых неотрицательных чисел (не обязательно различных) — номера наклеек Диего. Все номера наклеек не превосходят 109.

В следующей строке содержится число K (0 ≤ K ≤ 100 000) — количество коллекционеров, пришедших к Диего. В следующей строке содержатся K целых чисел pi (0 ≤ pi ≤ 109), где pi — наименьший номер наклейки, не интересующий i-го коллекционера.

## Формат выходных данных

Для каждого коллекционера в отдельной строке выведите количество различных чисел на наклейках, которые есть у Диего, но нет у этого коллекционера.

### Примеры

**input.txt**

```
1
5
2
4 6
```

**output.txt**

```
0
1
```

**input.txt**

```
3
100 1 50
3
300 0 75
```

**output.txt**

```
3
0
2
```

</details>

### [Решение](Коллекционер_Диего/)

## 4. Контрольная работа

Математическая задача. Задача решена подбором подходящей формулы для вывода места Васи.

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 64 мегабайт

Петя и Вася — одноклассники и лучшие друзья, поэтому они во всём помогают друг другу. Завтра у них контрольная по математике, и учитель подготовил целых K вариантов заданий.

В классе стоит один ряд парт, за каждой из них (кроме, возможно, последней) на контрольной будут сидеть ровно два ученика. Ученики знают, что варианты будут раздаваться строго по порядку: правый относительно учителя ученик первой парты получит вариант 1, левый — вариант 2, правый ученик второй парты получит вариант 3 (если число вариантов больше двух) и т.д. Так как K может быть меньше чем число учеников N, то после варианта K снова выдаётся вариант 1. На последней парте в случае нечётного числа учеников используется только место 1.

Петя самым первым вошёл в класс и сел на своё любимое место. Вася вошёл следом и хочет получить такой же вариант, что и Петя, при этом сидя к нему как можно ближе. То есть между ними должно оказаться как можно меньше парт, а при наличии двух таких мест с равным расстоянием от Пети Вася сядет позади Пети, а не перед ним. Напишите программу, которая подскажет Васе, какой ряд и какое место (справа или слева от учителя) ему следует выбрать. Если же один и тот же вариант Вася с Петей писать не смогут, то выдайте одно число  - 1.

### Формат входных данных

В первой строке входных данных находится количество учеников в классе 2 ≤ N ≤ 109. Во второй строке — количество подготовленных для контрольной вариантов заданий 2 ≤ K ≤ N. В третьей строке — номер ряда, на который уже сел Петя, в четвёртой — цифра 1, если он сел на правое место, и 2, если на левое.

### Формат выходных данных

Если Вася никак не сможет писать тот же вариант, что и Петя, то выведите  - 1. Если решение существует, то выведите два числа — номер ряда, на который следует сесть Васе, и 1, если ему надо сесть на правое место, или 2, если на левое. Разрешается использовать только первые N мест в порядке раздачи вариантов.

### Пример

**input.txt**

```
25
2
1
2
```

**output.txt**

```
2 2
```

**input.txt**

```
25
13
7
1
```

**output.txt**

```
-1
```

### Примечание

В первом примере вариантов 2, поэтому наилучшее место для Васи находится сразу за Петей. Во втором примере Петя будет единственным, кто получит вариант 13.

</details>

### [Решение](Контрольная_работа/)

## 5. Хорошая строка

Максимизировали хорошесть поиском минимума из количества букв, которые есть у нас и следующей буквы по алфавиту

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 64 мегабайта

На день рождения маленький Ипполит получил долгожданный подарок — набор дощечек с написанными на них буквами латинского алфавита. Теперь-то ему будет чем заняться долгими вечерами, тем более что мама обещала подарить ему в следующем году последовательность целых неотрицательных чисел, если он хорошо освоит этот набор. Ради такого богатства Ипполит готов на многое.

Прямо сейчас юный исследователь полностью поглощён изучением хорошести строк. Хорошестью строки называется количество позиций от 1 до L - 1 (где L — длина строки), таких, что следующая буква в строке является следующей по алфавиту. Например, хорошесть строки "abcdefghijklmnopqrstuvwxyz" равна 25, а строки "abdc" — только 1.

Ипполит размышляет над решением закономерно возникающей задачи: чему равна максимально возможная хорошесть строки, которую можно собрать, используя дощечки из данного набора? Вы-то и поможете ему с ней справиться.

### Формат входных данных

Первая строка ввода содержит единственное целое число N — количество различных букв в наборе (1 ≤ N ≤ 26). Обратите внимание: в наборе всегда используются N первых букв латинского алфавита.

Следующие N строк содержат целые положительные числа ci — количество букв соответствующего типа (1 ≤ ci ≤ 109). Таким образом, первое число означает количество букв "a", второе число задаёт количество букв "b" и так далее.

### Формат выходных данных

Выведите единственное целое число — максимально возможную хорошесть строки, которую можно собрать из имеющихся дощечек.

### Примеры

**input.txt**

```
3
1
1
1
```

**output.txt**

```
2
```

**input.txt**

```
2
3
4
```

**output.txt**

```
3
```

### Примечание

В первом тесте имеется по одной дощечке с каждой из 3 различных букв. Ответ 2 достигается на строке "abc"

</details>

### [Решение](Хорошая_строка/)

## 6. Операционные системы lite

Неоптимальное решение за O(N^2).
Перебор и удаление пересекающихся отрезков через создание нового списка.
Можно улучшить используя сбалансированное дерево поиска: сложность будет NlogN.

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунды

Ограничение по памяти: 64 мегабайт

Васин жесткий диск состоит из M секторов. Вася последовательно устанавливал на него различные операционные системы следующим методом: он создавал новый раздел диска из последовательных секторов, начиная с сектора номер ai и до сектора bi включительно, и устанавливал на него очередную систему. При этом, если очередной раздел хотя бы по одному сектору пересекается с каким-то ранее созданным разделом, то ранее созданный раздел «затирается», и операционная система, которая на него была установлена, больше не может быть загружена.

Напишите программу, которая по информации о том, какие разделы на диске создавал Вася, определит, сколько в итоге работоспособных операционных систем установлено и работает в настоящий момент на Васином компьютере.

### Формат входных данных

Сначала вводятся натуральное число M — количество секторов на жестком диске (1 ≤ M ≤ 109) и целое число N — количество разделов, которое последовательно создавал Вася (0 ≤ N ≤ 1000).

Далее идут N пар чисел ai и bi, задающих номера начального и конечного секторов раздела (1 ≤ ai ≤ bi ≤ M).

### Формат выходных данных

Выведите одно число — количество работающих операционных систем на Васином компьютере.

### Пример

**input.txt**

```
10
3
1 3
4 7
3 4
```

**output.txt**

```
1
```

**input.txt**

```
10
4
1 3
4 5
7 8
4 6
```

**output.txt**

```
3
```

</details>

### [Решение](Операционные_системы_lite/)

## 7. SNTP

round округляет до ближайшего четного числа. Поэтому для решение этой проблемы использовали тот факт, что каждое целое число будет иметь по крайней мере одно число, кратное двум, без остатка.
Для вывода времени использовался :02d. Он форматирует целое число (d) в поле минимальной ширины 2 (2) с заполнением нулем слева (впереди 0).

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 64 мегабайт

Для того чтобы компьютеры поддерживали актуальное время, они могут обращаться к серверам точного времени SNTP (Simple Network Time Protocol). К сожалению, компьютер не может просто получить время у сервера, потому что информация по сети передаётся не мгновенно: пока сообщение с текущим временем дойдёт до компьютера, оно потеряет свою актуальность. Протокол взаимодействия клиента (компьютера, запрашивающего точное время) и сервера (компьютера, выдающего точное время) выглядит следующим образом:

1. Клиент отправляет запрос на сервер и запоминает время отправления A (по клиентскому времени).

2. Сервер получает запрос в момент времени B (по точному серверному времени) и отправляет клиенту сообщение, содержащее время B.

3. Клиент получает ответ на свой запрос в момент времени C (по клиентскому времени) и запоминает его. Теперь клиент, из предположения, что сетевые задержки при передаче сообщений от клиента серверу и от сервера клиенту одинаковы, может определить и установить себе точное время, используя известные значения A, B, C.

Вам предстоит реализовать алгоритм, с точностью до секунды определяющий точное время для установки на клиенте по известным A, B и C. При необходимости округлите результат до целого числа секунд по правилам арифметики (в меньшую сторону, если дробная часть числа меньше 1/2, иначе в большую сторону).

Возможно, что, пока клиент ожидал ответа, по клиентскому времени успели наступить новые сутки, однако известно, что между отправкой клиентом запроса и получением ответа от сервера прошло менее 24 часов.

### Формат входных данных

Программа получает на вход три временные метки A, B, C, по одной в каждой строке. Все временные метки представлены в формате «hh:mm:ss», где «hh» – это часы, «mm» – минуты, «ss» – секунды. Часы, минуты и секунды записываются ровно двумя цифрами каждое (возможно, с дополнительными нулями в начале числа).

### Формат выходных данных

Программа должна вывести одну временную метку в формате, описанном во входных данных, – вычисленное точное время для установки на клиенте. В выводе не должно быть пробелов, пустых строк в начале вывода.

### Пример

**input.txt**

```
15:01:00
18:09:45
15:01:40
```

**output.txt**

```
18:10:05
```

</details>

### [Решение](SNTP/)

## 8. Минимальный прямоугольник

Просто найти минимумы и максимумы списков координат

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 64 мегабайт

На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник, со сторонами, параллельными линиям сетки, покрывающий все закрашенные клетки.

### Формат входных данных

Во входном файле, на первой строке, находится число K (1 ≤ K ≤ 100). На следующих K строках находятся пары чисел Xi и Yi – координаты закрашенных клеток (|Xi|, |Yi| ≤ 109).

### Формат выходных данных

Выведите в выходной файл координаты левого нижнего и правого верхнего углов прямоугольника.

### Примеры

**input.txt**

```
3
1 1
1 10
5 5
```

**output.txt**

```
3
1 1
1 10
5 5
```

</details>

### [Решение](Минимальный_прямоугольник/)

## 9. Сумма в прямоугольнике

Если реализовать обычным методом, то время O(Q\*N^2) = 10^11. Поэтому надо использовать префиксные суммы.
Одномерные суммы дадут сложность O(NQ) = 10^8. Поэтому используем двумерные префиксные суммы.

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 3 секунды

Ограничение по памяти: 256 мегабайт

Вам необходимо ответить на запросы узнать сумму всех элементов числовой матрицы N×M в прямоугольнике с левым верхним углом (x1, y1) и правым нижним (x2, y2)

### Формат входных данных

В первой строке находится числа N, M размеры матрицы (1 ≤ N, M ≤ 1000) и K — количество запросов (1 ≤ K ≤ 100000). Каждая из следующих N строк содержит по M чисел`— элементы соответствующей строки матрицы (по модулю не превосходят 1000). Последующие K строк содержат по 4 целых числа, разделенных пробелом x1 y1 x2 y2 — запрос на сумму элементов матрице в прямоугольнике (1 ≤ x1 ≤ x2 ≤ N, 1 ≤ y1 ≤ y2 ≤ M)

### Формат выходных данных

Для каждого запроса на отдельной строке выведите его результат — сумму всех чисел в элементов матрице в прямоугольнике (x1, y1), (x2, y2)

### Пример

**input.txt**

```
3 3 2
1 2 3
4 5 6
7 8 9
2 2 3 3
1 1 2 3
```

**output.txt**

```
28
21
```

</details>

### [Решение](Сумма_в_прямоугольнике/)

## 10. Скучная лекция

Задача про математику.
Нашли в скольких подстроках встречается буква и перемножили количество подстрок до и после буквы

<details>
<summary>Условие задачи ...</summary>
Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 64 мегабайт

Лёша сидел на лекции. Ему было невероятно скучно. Голос лектора казался таким далеким и незаметным...

Чтобы окончательно не уснуть, он взял листок и написал на нём свое любимое слово. Чуть ниже он повторил своё любимое слово, без первой буквы. Ещё ниже он снова написал своё любимое слово, но в этот раз без двух первых и последней буквы.

Тут ему пришла в голову мысль — времени до конца лекции все равно ещё очень много, почему бы не продолжить выписывать всеми возможными способами это слово без какой-то части с начала и какой-то части с конца?

После лекции Лёша рассказал Максу, как замечательно он скоротал время. Максу стало интересно посчитать, сколько букв каждого вида встречается у Лёши в листочке. Но к сожалению, сам листочек куда-то запропастился.

Макс хорошо знает любимое слово Лёши, а ещё у него не так много свободного времени, как у его друга, так что помогите ему быстро восстановить, сколько раз Лёше пришлось выписать каждую букву.

### Формат входных данных

На вход подаётся строка, состоящая из строчных латинских букв — любимое слово Лёши.
Длина строки лежит в пределах от 5 до 100 000 символов.

### Формат выходных данных

Для каждой буквы на листочке Лёши, выведите её, а затем через двоеточие и пробел сколько раз она встретилась в выписанных Лёшей словах (см. формат вывода в примерах). Буквы должны следовать в алфавитном порядке. Буквы, не встречающиеся на листочке, выводить не нужно.

### Примеры

**input.txt**

```
hello
```

**output.txt**

```
e: 8
h: 5
l: 17
o: 5
```

**input.txt**

```
abacaba
```

**output.txt**

```
a: 44
b: 24
c: 16
```

### Примечание

Пояснение к первому примеру. Если любимое Лёшино слово — "hello", то на листочке у Лёши будут выписаны следующие слова:

"hello"

"hell"

"ello"

"hel"

"ell"

"llo"

"he"

"el"

"ll"

"lo"

"h"

"e"

"l"

"l"

"o"

Среди этих слов 8 раз встречается буква "e", 5 раз — буква "h", 17 раз — буква "l" и 5 раз буква "o".

</details>

### [Решение](Скучная_лекция/)

## 11. Конвейер - A

Задача Дивизиона A.
Задача решена с помощью стека.
Сравнивались значения в сортированном списке и в стеке.

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 64 мегабайт

Для транспортирования материалов из цеха А в цех В используется конвейер. Материалы упаковываются в одинаковые контейнеры и размещаются на ленте один за одним в порядке изготовления в цехе А. Каждый контейнер имеет степень срочности обработки в цехе В. Для упорядочивания контейнеров по степени срочности используют накопитель, который находится в конце конвейера перед входом в цех В. Накопитель работает пошагово, на каждом шаге возможны следующие действия:

- накопитель перемещает первый контейнер из ленты в цех В;

- накопитель перемещает первый контейнер из строки в склад (в складе каждый следующий контейнер помещается на предыдущий);

- накопитель перемещает верхний контейнер из склада в цех В.

Напишите программу, которая по последовательности контейнеров определит, можно ли упорядочить их по степени срочности пользуясь описанным накопителем.

### Формат входных данных

Входной файл в первой строке содержит количество тестов N. Далее следует N строк, каждый из которых описывает отдельный тест и содержит целое число K (1 ≤ K ≤ 10000) — количество контейнеров в последовательности и K действительных чисел — степеней срочности контейнеров в порядке их поступления из цеха А (меньшим числам соответствует большая степень срочности).

### Формат выходных данных

Каждая строка выходного файла должна содержать ответ для одного теста. Необходимо вывести 1, если необходимое упорядочивание возможно, или 0 в противном случае.

### Примеры

**input.txt**

```
2
2 2.9 2.1
3 5.6 9.0 2.0

```

**output.txt**

```
1
0
```

</details>

### [Решение](Конвейер_А/)

## 11. Стек с защитой от ошибок - Б

Задача Дивизиона Б.
Для моделирования стандартной структурой данных stack использовал класс.
К методам обращался с помощью getattr.
Позволяет получить значение атрибута объекта по его имени.
Склеивали значения списка output_stack для более быстрого вывода результата.
Это быстрее чем вызов print по отдельности.

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 64 мегабайт

Научитесь пользоваться стандартной структурой данных stack для целых чисел. Напишите программу, содержащую описание стека и моделирующую работу стека, реализовав все указанные здесь методы. Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:

push n
Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.

pop
Удалить из стека последний элемент. Программа должна вывести его значение.

back
Программа должна вывести значение последнего элемента, не удаляя его из стека.

size
Программа должна вывести количество элементов в стеке.

clear
Программа должна очистить стек и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Перед исполнением операций back и pop программа должна проверять, содержится ли в стеке хотя бы один элемент. Если во входных данных встречается операция back или pop, и при этом стек пуст, то программа должна вместо числового значения вывести строку error.

### Формат входных данных

Вводятся команды управления стеком, по одной на строке

### Формат выходных данных

Программа должна вывести протокол работы стека, по одному сообщению на строке

### Примеры

**input.txt**

```
push 1
back
exit
```

**output.txt**

```
ok
1
bye
```

**input.txt**

```
size
push 1
size
push 2
size
push 3
size
exit
```

**output.txt**

```
0
ok
1
ok
2
ok
3
bye
```

**input.txt**

```
push 3
push 14
size
clear
push 1
back
push 2
back
pop
size
pop
size
exit
```

**output.txt**

```
ok
ok
2
ok
ok
1
ok
2
2
1
1
0
bye
```

</details>

### [Решение](Стек_с_защитой_от_ошибок_Б/)

## 12. Значение арифметического выражения - А

Задача Дивизиона А.
Преобразование исходных данных в список и минимальная проверка.
Преобразование инфиксной нотации в постфиксную.
Если ошибка при выполнении в except срабатывает вывод WRONG.

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 256 мегабайт

Задано числовое выражение. Необходимо вычислить его значение или установить, что оно содержит ошибку. В выражении могут встречаться знаки сложения, вычитания, умножения, скобки и пробелы (пробелов внутри чисел быть не должно). Приоритет операций стандартный. Все числа в выражении целые и по модулю не превосходят 2×10^9. Также гарантируется, что все промежуточные вычисления также не превосходят 2×10^9.

### Формат входных данных

В первой строке вводится выражение. Его длина не превосходит 100 знаков. После выражения идет переход на новую строчку.

### Формат выходных данных

Выведите значение этого выражения или слово "WRONG если значение не определено.

### Примеры

**input.txt**

```
1+(2*2 - 3)
```

**output.txt**

```
2
```

**input.txt**

```
1+a+1
```

**output.txt**

```
WRONG
```

**input.txt**

```
1 1 + 2
```

**output.txt**

```
WRONG
```

</details>

### [Решение](/Значение_арифметического_выражения/Task12.py)

### [Решение без использования стека](/Значение_арифметического_выражения/Task12_Simple.py)

## 12. Правильная скобочная последовательность - Б

Задача Дивизиона Б.
Классическая задача на стек. Баланс скобок.

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 64 мегабайт

Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. Программа дожна определить, является ли данная скобочная последовательность правильной. Пустая последовательность явлется правильной. Если A – правильная, то последовательности (A), [A], {A} – правильные. Если A и B – правильные последовательности, то последовательность AB – правильная.

### Формат входных данных

В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.

### Формат выходных данных

Если данная последовательность правильная, то программа должна вывести строку yes, иначе строку no.

### Примеры

**input.txt**

```
()[]
```

**output.txt**

```
yes
```

**input.txt**

```
([)]
```

**output.txt**

```
no
```

**input.txt**

```
(
```

**output.txt**

```
no
```

</details>

### [Решение](/Правильная_скобочная_последовательность/TaskB_12.py)

## 13. Значение логического выражения - А

Задача Дивизиона А.
Преобразование исходных данных в список.
Преобразование инфиксной нотации в постфиксную.
Вычисление логического выражения по постфиксной записи.

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 256 мегабайт

Задано логическое выражение. Необходимо вычислить его значение. В выражении могут встречаться знаки ! (отрицание), & (логическое «и»), | (логическое «или»), ̂ (XOR — «исключающее ИЛИ», «ровно одно из двух — истина») и скобки. Самый высокий приоритет у отрицания, меньше – у &, операции | и ̂ имеют самый низкий приоритет (одинаковый) и вычисляются слева направо. Все числа в выражении либо 0, либо 1.

### Формат входных данных

В первой строке вводится выражение. Его длина не превосходит 100 знаков. После выражения идет переход на новую строчку.

### Формат выходных данных

Выведите значение этого выражения (0 или 1).

### Примеры

**input.txt**

```
1|(0&0^1)
```

**output.txt**

```
1
```

</details>

### [Решение](/Значение_логического_выражения/Task13.py)

## 13. Постфиксная запись - Б

Преобразование исходных данных в список.
Вычисление арифметического выражения по постфиксной записи.

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 256 мегабайт

В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух чисел A и B записывается как A B +. Запись B C + D _ обозначает привычное нам (B + C) _ D, а запись A B C + D _ + означает A + (B + C) _ D. Достоинство постфиксной записи в том, что она не требует скобок и дополнительных соглашений о приоритете операторов для своего чтения.

### Формат входных данных

В единственной строке записано выражение в постфиксной записи, содержащее цифры и операции +, -, \*. Цифры и операции разделяются пробелами. В конце строки может быть произвольное количество пробелов.

### Формат выходных данных

Необходимо вывести значение записанного выражения.

### Пример

**input.txt**

```
8 9 + 1 7 - *
```

**output.txt**

```
-102
```

</details>

### [Решение](/Постфиксная_запись/Task13B.py)

## 14. Гистограмма и прямоугольник - А

Линейное время. Поиск ближайшего меньшего слева и справа осуществили, используя стек. Площадь вычислялась как произведение высоты столбца на разницу индексов ближайшего меньшего слева и справа. Потом находился максимум.

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 256 мегабайт

Гистограмма является многоугольником, сформированным из последовательности прямоугольников, выровненных на общей базовой линии. Прямоугольники имеют равную ширину, но могут иметь различные высоты. Например, фигура слева показывает гистограмму, которая состоит из прямоугольников с высотами 2, 1, 4, 5, 1, 3, 3. Все прямоугольники на этом рисунке имеют ширину, равную 1.

https://contest.yandex.ru/testsys/statement-image?imageId=3967ea10549ba4612e66f367a385c903993fe14589a36281f436773c0f85f019

Обычно гистограммы используются для представления дискретных распределений, например, частоты символов в текстах. Отметьте, что порядок прямоугольников очень важен. Вычислите область самого большого прямоугольника в гистограмме, который также находится на общей базовой линии. На рисунке справа заштрихованная фигура является самым большим выровненным прямоугольником на изображенной гистограмме.

### Формат входных данных

В первой строке входного файла записано число N (0 <= N <= 10^6) — количество прямоугольников гистограммы. Затем следует N целых чисел h1,...., hn, где 0 <= hi <= 10^9. Эти числа обозначают высоты прямоугольников гистограммы слева направо. Ширина каждого прямоугольника равна 1

### Формат выходных данных

Выведите площадь самого большого прямоугольника в гистограмме. Помните, что этот прямоугольник должен быть на общей базовой линии.

### Пример

**input.txt**

```
7 2 1 4 5 1 3 3
```

**output.txt**

```
8
```

</details>

### [Решение](/Гистограмма_и_прямоугольник/TaskA14.py)

## 14. Сортировка вагонов lite - Б

Задача на стек. Последний элемент стека сравнивается с порядковым номером вагона 1, ..., N.

<details>
<summary>Условие задачи ...</summary>

Имя входного файла: input.txt

Имя выходного файла: output.txt

Ограничение по времени: 1 секунда

Ограничение по памяти: 64 мегабайт

К тупику со стороны пути 1 (см. рисунок) подъехал поезд. Разрешается отцепить от поезда один или сразу несколько первых вагонов и завезти их в тупик (при желании, можно даже завезти в тупик сразу весь поезд). После этого часть из этих вагонов вывезти в сторону пути 2. После этого можно завезти в тупик еще несколько вагонов и снова часть оказавшихся вагонов вывезти в сторону пути 2. И так далее (так, что каждый вагон может лишь один раз заехать с пути 1 в тупик, а затем один раз выехать из тупика на путь 2). Заезжать в тупик с пути 2 или выезжать из тупика на путь 1 запрещается. Нельзя с пути 1 попасть на путь 2, не заезжая в тупик.

https://contest.yandex.ru/testsys/statement-image?imageId=6b47dd0f62b0e9704864ecb0be7b66943d3c0afd847bde6b2a7138ce61337b35

Известно, в каком порядке изначально идут вагоны поезда. Требуется с помощью указанных операций сделать так, чтобы вагоны поезда шли по порядку (сначала первый, потом второй и т.д., считая от головы поезда, едущего по пути 2 в сторону от тупика). Напишите программу, определяющую, можно ли это сделать.

## Формат входных данных

Вводится число N — количество вагонов в поезде (1 ≤ N ≤ 100). Дальше идут номера вагонов в порядке от головы поезда, едущего по пути 1 в сторону тупика. Вагоны пронумерованы натуральными числами от 1 до N, каждое из которых встречается ровно один раз.

### Формат выходных данных

Если сделать так, чтобы вагоны шли в порядке от 1 до N, считая от головы поезда, когда поезд поедет по пути 2 из тупика, можно, выведите сообщение YES, если это сделать нельзя, выведите NO.

### Примеры

**input.txt**

```
3
3 2 1
```

**output.txt**

```
YES
```

**input.txt**

```
4
4 1 3 2
```

**output.txt**

```
YES
```

**input.txt**

```
3
2 3 1
```

**output.txt**

```
NO
```

</details>

### [Решение](Сортировка_вагонов_lite/TaskB14.py)
