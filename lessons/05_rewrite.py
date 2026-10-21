# 第 5 课自检
#
# 规则：
#   1. 【关掉 05_list_dict.py】，不许回头看
#   2. 下面 5 题，不看任何资料写
#   3. 写完直接点右上角 ▶ 运行
#
# 五题都写出来 → 第 5 课过关
# 有写不出来的 → 停下来把那题重写一遍，不要往下走
#
# ⚠️ 每题的变量都要你自己写出来（比如第 1 题的列表，你自己建一个）。


# 1. 建一个列表 [1, 2, 3, 4, 5]，打印：
#      - 它的长度
#      - 最大值
#      - 所有元素的和
lists = [1,2,3,4,5]
print(len(lists))
print(max(lists))
print(sum(lists))
# 2. 接着上面的列表：
#      - 往末尾加一个 6
#      - 把第一个元素改成 100
#      - 打印整个列表
lists.append(6)
lists[0] = 100
print(lists)
# 3. 建一个字典 {"name": 你的名字, "age": 你的年龄}：
#      - 打印所有键值对（用 .items() 遍历）
#      - 再加一个 "city" 键
#      - 打印整个字典
counts = {"name":"orange","age":25}
for x,y in counts.items():
    print(x,y)

counts["city"]="beijing"
print(counts)
# 4. 把 "a,b,c" 按逗号切成列表，再用 "-" 拼回去并打印
#      期望结果：a-b-c
s = "a,b,c"
parts = s.split(",")
print(parts)
parts2 = "-".join(parts)
print(parts2)
# 5. ⭐ 词频统计：
#      统计 "a b a c b a" 里每个词出现几次，并打印出来
#      期望结果：{'a': 3, 'b': 2, 'c': 1}
abc = "a,b,a,c,b,a"
words = abc.split(",")
count = {}
for x in words:
    if x in count:
        count[x] = count[x] +1
    else:
        count[x] = 1
print(count)