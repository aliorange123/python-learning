# 第 6 课：函数
#
# 怎么用这个文件：
#   1. 先做第 0 节的热身（**不许看 05 那两个文件**）
#   2. 从上往下做【练习】；【猜】先写猜测再运行
#   3. 全做完后关掉本文件，新建 06_rewrite.py 从零重写
#
# 卡住了就来问我。这个文件里没有答案。
#
# 📌 本课要解决的一件事：**把「一堆代码」变成「一个能反复用的工具」**
#
#    第 5 课你的词频统计是「一次性」的：换了句子就得重写一遍。
#    学了函数，你可以写一个 count_words(text)，传什么句子都行。
#
# 📌 本课最重要的一对概念：**return 和 print 不是一回事**


# ============================================================
# 0. 热身（约 10 分钟）
# ============================================================
# 【热身】**不看 05_list_dict.py / 05_rewrite.py**，写出词频统计的完整逻辑：
#
#     text = "a b a c b a"
#
#   1. split 成单词列表
#   2. 用空字典统计每个词出现的次数
#   3. 打印结果（期望 {'a': 3, 'b': 2, 'c': 1}）
#
# 写不出来 → 回去看 05 的文件，再关掉重写一遍。


# ============================================================
# 1. 定义函数：def
# ============================================================
# C:   int add(int a, int b) { return a + b; }
# Py:  def add(a, b):  return a + b
#
# ⚠️ 没有返回类型、没有花括号、参数不用写类型——**冒号 + 缩进**

def greet(name):
    return f"你好，{name}"

# 定义好了要「调用」它才会执行
print(greet("orange"))
print(greet("world"))

# 【猜 1】下面这行会打印什么？先猜，再运行：
#         print(greet)
#         我猜：

# 【练习 2】写一个函数 add(a, b)，返回 a + b
#           然后调用它打印 add(3, 5)
def add(a,b):
    return a + b

print(add(3,5))
# 【练习 3】写一个函数 square(n)，返回 n 的平方
#           调用它打印 square(7)
def square(n):
    return n * n
print(square(7))
# 【练习 4】写一个函数 max_of_three(a, b, c)，返回三个数里最大的
#           提示：可以用内置的 max(a, b, c) —— 但那就没意思了
#           试试用 if 比较，或者 max(a, max(b, c))
def max_of_three(a,b,c):
    return max(a,max(b,c))
print(max_of_three(1,2,3))

# ============================================================
# 2. ⭐ return 和 print 不是一回事（本节重点）
# ============================================================

def add_print(a, b):
    print(a + b)          # 打印出来

def add_return(a, b):
    return a + b          # 交回去

# 【猜 5】先猜再运行，看这四行分别输出什么：

add_print(2, 3)               # 我猜输出：
print(add_print(2, 3))        # 我猜输出：

add_return(2, 3)              # 我猜输出：
print(add_return(2, 3))       # 我猜输出：

# 【猜 6】下面这行会怎样？先猜再运行：
#
#         x = add_print(2, 3)
#         print(x)
#
#         我猜 x 是：None

# 【练习 7】把下面的「打印版」改成「返回版」：
#
#   def area(w, h):
#       print(w * h)
def area(w,h):
    return w*h
print(area(3,4))
#   改完之后，用 print(area(3, 4)) 打印出来，应该是 12

# 【猜 8】一个函数里**没有 return**，那它返回什么？
#         我猜：None


# ============================================================
# 3. 参数：默认值、关键字参数
# ============================================================

def intro(name, age=18, city="beijing"):
    return f"{name}, {age}岁, 来自{city}"

# 【猜 9】先猜再运行：
print(intro("orange"))                      
print(intro("orange", 25))                  
print(intro("orange", city="shanghai"))     

# 【练习 10】给下面的函数加一个默认参数 prefix="Hi"，
#            不传的时候用 "Hi"，传了就用传的
def hello(name,prefix="Hi "):
  return f"{prefix}{name}"
print(hello("orange"))
print(hello("orange", "Hello "))
print(hello("orange", prefix="Yo "))
# 【练习 11】调用 intro 时用**关键字参数**，故意把顺序倒过来：
#            intro(city="guangzhou", name="bob")
#            看看能不能跑
print(intro(city="guangzhou", name="bob"))

# ============================================================
# 4. 为什么要函数（这节不讲语法，讲动机）
# ============================================================
# 对比一下：三个句子都要统计词频。

# 【练习 12】**先不用函数**，把词频统计的代码连写三遍（复制粘贴），
#            分别统计这三句：
#
#   t1 = "a b a"
#   t2 = "x y x z"
#   t3 = "hello hello world"
# 第 1 遍
t1 = "a b a"
words1 = t1.lower().split()
counts1 = {}
for word in words1:
    if word in counts1:
        counts1[word] = counts1[word] + 1
    else:
        counts1[word] = 1
print(counts1)

# 第 3 遍
t3 = "hello hello world"
words3 = t3.lower().split()
counts3 = {}
for word in words3:
    if word in counts3:
        counts3[word] = counts3[word] + 1
    else:
        counts3[word] = 1
print(counts3)
# 第 3 遍
t2 = "x y x z"
words2 = t2.lower().split()
counts2 = {}
for word in words2:
    if word in counts2:
        counts2[word] = counts2[word] + 1
    else:
        counts2[word] = 1
print(counts2)
#            ⚠️ 写的时候体会一下：三遍有多烦？变量名会不会打架？

# 【练习 13】用函数重写：
#
#   def count_words(text):
#       # 里面就是你的词频统计逻辑
#       return counts
def count_words(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
    else:
        counts[word] = 1
    return counts
#   然后：
print(count_words("a b c"))
print(count_words("x y x z"))
print(count_words("hello hello world"))
#
#           体会一下：**同样的逻辑，只写一次。**
#           这就是函数的全部价值。
print("XXXXXXXXXX")

# ============================================================
# 5. 作用域：函数里的变量，外面看不见
# ============================================================

x = "我是一个全局变量"

def show_scope():
    y = "我是一个局部变量"
    print(x)          # 能看见外面的
    print(y)          # 能看见自己的

show_scope()

# 【猜 14】先猜再运行：
#         print(y)
#         我猜：
#
#         print(x)
#         我猜：

# 【练习 15】在函数里改全局变量会怎样？先猜再试：
#
#   def change():
#       x = "被改了"
#
#   change()
#   print(x)
#
#   我猜：


# ============================================================
# 6. ⭐ lambda：补上第 5 课没做完的「按次数排序」
# ============================================================
# lambda 是「一行小函数」，没有名字，用完就扔。
#
#   普通函数：def add(a, b): return a + b
#   lambda：  lambda a, b: a + b
#
# 参数在前，冒号，返回值在后（不用写 return）。

# 【练习 16】下面两个等价，先各跑一次确认：
#
#   f1 = lambda a, b: a + b
#   print(f1(2, 3))
#
#   def f2(a, b):
#       return a + b
#   print(f2(2, 3))

# 【练习 17】⭐ **第 5 课没做完的那一步：按词频从多到少排序**
#
#   text = "the quick brown fox jumps over the lazy dog the fox"
#   counts = {...}                    ← 先用你的 count_words 算出来
#
#   然后排序：
#
#   items = list(counts.items())      # 转成列表，才能排序
#   items.sort(key=lambda x: x[1], reverse=True)
#
#   for word, count in items:
#       print(word, count)
#
#   ⚠️ 关键看这一句：`key=lambda x: x[1]`
#      - `counts.items()` 的每一项是 `('the', 3)` 这样的一对
#      - `lambda x: x[1]` 的意思是「**按第 2 个元素排**」也就是「按次数」
#      - `reverse=True` = 从大到小
#
#   期望输出：
#      the 3
#      fox 2
#      quick 1
#      ...
#
# 【练习 18】把 reverse=True 去掉，看看变成什么顺序（从少到多）


# ============================================================
# 7. 综合：把词频统计装进函数，并且能排序
# ============================================================

# 【练习 19】写两个函数：
#
#   def count_words(text):
#       """返回 {词: 次数} 的字典"""          ← 文档字符串，用三引号
#
#   def top_words(counts, n=5):
#       """返回出现次数最多的前 n 个词，按次数从多到少"""
#
#   然后：
#   counts = count_words("the quick brown fox jumps over the lazy dog the fox")
#   print(top_words(counts))
#   print(top_words(counts, 3))
#
#   ⚠️ top_words 里要用 sorted 或 sort + lambda


# ============================================================
# 自检：全做完之后再打开这一节
# ============================================================
# 新建一个空文件 06_rewrite.py，关掉本文件，不看任何资料写出：
#
#   1. 写一个函数 add(a, b) 返回和，调用并打印 add(3, 5)
#   2. 写一个函数 is_even(n) 返回 True/False，打印 is_even(4) 和 is_even(7)
#   3. 写一个函数 max_of_three(a, b, c) 返回最大值
#   4. 写一个函数 count_words(text)，返回词频字典
#   5. 用 count_words 统计 "a b a c b a"，打印结果
#
# 五题都写出来 → 第 6 课过关，告诉我，我批改并推送。
