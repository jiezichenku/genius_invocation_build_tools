import random


def unique_permutations(n, l):
    # 创建一个集合来存储唯一排列
    unique_perms = set()
    l_len = len(l)

    while len(unique_perms) < n:
        # 生成一个随机排列
        perm = tuple(random.sample(l, l_len))
        unique_perms.add(perm)

    return list(unique_perms)


# 示例用法
n = 1000000
l = list(range(30))
result = unique_permutations(n, l)
print(result)
print(len(result))
