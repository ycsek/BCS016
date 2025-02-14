'''
Author: Jason Shi
Date: 22-01-2025 19:12:19
Last Editors: Jason
Contact Last Editors: D23090120503@cityu.edu.mo
LastEditTime: 22-01-2025 19:31:55
'''
def integer_square_root(x):
    # 判断输入是否正确
    if x < 0:
        raise ValueError("必须输入一个非负整数！")
    # 0和1的平方根为本身
    if x == 0 or x == 1:
        return x
    start, end = 0, x
    # 利用二分查找，通过不断缩小范围，逼近平方根的值
    while start <= end:
        mid = (start + end) // 2
        # 如果mid的平方等于x，直接返回mid
        if mid * mid == x:
            return mid
        # 如果mid的平方小于x，平方根在mid右侧，更新start
        elif mid * mid < x:
            start = mid + 1
            result = mid
        # 如果mid的平方大于x，平方根在mid左侧，更新end
        else:
            end = mid - 1
    return result

x = int(input("请输入一个非负整数: "))
print(f"{x}的平方根为：", integer_square_root(x))