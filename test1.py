a = 1  # int
b = True  # bool
c = 3.14  # float
d = 2 + 3j  # 复数complex
print(a, b, c, d)

# 使用三引号(''' 或 """)可以指定一个多行字符串
# 转义符 \
word = '字符串'
sentence = "这是一个句子。"
paragraph = "这是一个段落，\
可以由多行组成"
paragraph2 = """这是一个段落，
可以由多行组成"""
print(word, sentence, paragraph)
# 0,1,[2... 即从第三个字符开始一直到末尾
print(paragraph[2:])
# 0,1,[2,3,4,5,6],7 即从第三个字符开始一直到第七个
print(paragraph[2:7])
print(paragraph[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(paragraph * 2)  # 输出字符串两次
print(paragraph + '你好')  # 连接字符串
print(sentence[0:-1])  # 输出第一个到倒数第二个的所有字符

# 这里的 r 指 raw，即 raw string，会自动将反斜杠转义，例如：
print('\n')  # 输出空行
print(r'\n')  # 输出 \n
print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

print('----------------------')
# 不换行输出
print(c)
print(a, end=" ")
print(b, end=" ")
