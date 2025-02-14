'''
Author: Jason Shi
Date: 22-01-2025 19:03:58
Last Editors: Jason
Contact Last Editors: D23090120503@cityu.edu.mo
LastEditTime: 22-01-2025 19:07:01
'''
# 计算最大公约数


def compute_gcd(a, b):
    smaller = min(a, b)
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
# 计算最小公倍数


def compute_lcm(a, b, gcd):
    return a * b // gcd


def main():
    try:
        num1 = int(input("请输入第一个整数: "))
        num2 = int(input("请输入第二个整数: "))
        gcd = compute_gcd(num1, num2)
        lcm = compute_lcm(num1, num2, gcd)
        print(f"最大公约数: {gcd}")
        print(f"最小公倍数: {lcm}")
    except ValueError:
        print("请输入整数")


if __name__ == "__main__":
    main()
