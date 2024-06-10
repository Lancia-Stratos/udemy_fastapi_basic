# リスト
list_1 = [1, 2, 3]
list_1.append(4)
print(list_1)

my_list = [1, 2, 3]
another_list = [4,5,6]
my_list.extend(another_list)
print(my_list)

# タプル
my_tuple = (1, 2, 2, 3, 4)
count = my_tuple.count(3)
print(count)

# 辞書
my_dict = { "a": 1, "b": 2, "c": 3}
values = my_dict.values()
print(list(values))

# 文字列
text = "hello world"
new_text = text.replace("world", "Python")
print(new_text)

text_2 = "one, two, three"
words = text_2.split(",")
print(words)

text_3 = "hello world"
index = text_3.index("world")
print(index)