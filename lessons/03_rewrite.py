# 第 3 课自检
#
# 规则：
#   1. 【关掉 03_string.py】，不许回头看
#   2. 下面 5 题，不看任何资料写
#   3. 写完运行：python lessons\03_rewrite.py
#
# 五题都写出来 → 第 3 课过关
# 有写不出来的 → 停下来把那题重写一遍，不要往下走


# 1. 给定 s = "abcdefg"，用切片取出 "cde"
s = "abcdefg"
a = s[2:5]
print(a)
# 2. 用切片把 s 反转并打印
b = s[::-1]
print(b)
# 3. 给一句带首尾空格的话，去掉首尾空格，打印它和它的长度
#    提示：先用一个变量存那句话
c = " what are you doing "
d = c.strip()
print(d)
print(len(d))
# 4. 把 3.14159 格式化成保留 3 位小数并打印
e = 3.14159
print(f"{e:.3f}")
# 5. 给一个字符串，用 .count() 数出某个字符出现了几次
a = "1215645"
print(a.count("1"))
