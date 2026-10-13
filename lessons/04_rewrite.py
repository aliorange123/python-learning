# 第 4 课自检
#
# 规则：
#   1. 【关掉 04_if_loop.py】，不许回头看
#   2. 下面 5 题，不看任何资料写
#   3. 写完直接点右上角 ▶ 运行
#
# 五题都写出来 → 第 4 课过关
# 有写不出来的 → 停下来把那题重写一遍，不要往下走
#
# ⚠️ 重要：**每题要用的变量，都要你自己写出来。**
#    比如第 1 题的「n = 7」，是让你写一行 `n = 7`，
#    不是「环境里已经有了」。


# 1. 先写 n = 7，然后用 if / elif / else 判断它是正数、负数还是零
#    写完把 n 改成 -3 和 0 各跑一次，确认三条分支都能走到
n = 7
if n >0:
    print("正数")
elif n == 0:
    print("零")
else:
    print("负数")

# 2. 用 for + range 打印 1 到 20 里的所有奇数
for i in range(1,21,2):
    print(i)

# 3. 用 for + if 打印 1 到 20 里所有能被 3 整除的数
for i in range(1,21):
    if i%3 == 0:
        print(i)

# 4. FizzBuzz（只打印 1 到 20）
for i in range(1,21):
    if i%3 ==0 and i%5 ==0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

# 5. 用 while 从 10 倒着数到 1
i = 10
while i >0:
    print(i)
    i -=1
