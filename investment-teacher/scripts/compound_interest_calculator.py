#!/usr/bin/env python3
"""
复利计算器
帮助理解复利效应的威力
"""

def calculate_compound_interest(principal, rate, years, compounds_per_year=12):
    """
    计算复利

    参数:
    principal: 本金（初始投资额）
    rate: 年利率（小数形式，如5%为0.05）
    years: 投资年数
    compounds_per_year: 每年复利次数（默认12，即每月复利）

    返回:
    最终金额
    """
    # 复利公式: A = P(1 + r/n)^(nt)
    # A: 最终金额
    # P: 本金
    # r: 年利率
    # n: 每年复利次数
    # t: 年数
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)
    return amount

def calculate_simple_interest(principal, rate, years):
    """
    计算单利

    参数:
    principal: 本金
    rate: 年利率（小数形式）
    years: 年数

    返回:
    最终金额
    """
    # 单利公式: A = P(1 + rt)
    amount = principal * (1 + rate * years)
    return amount

def demonstrate_compound_vs_simple():
    """演示复利与单利的区别"""
    print("=" * 60)
    print("复利 vs 单利 演示")
    print("=" * 60)

    principal = 10000  # 1万元
    rate = 0.05  # 5%年利率
    years = 30  # 30年

    print(f"\n初始投资: {principal:,.2f} 元")
    print(f"年利率: {rate*100:.1f}%")
    print(f"投资期限: {years} 年")

    # 计算单利
    simple_amount = calculate_simple_interest(principal, rate, years)
    simple_interest = simple_amount - principal

    # 计算复利（每月复利）
    compound_amount = calculate_compound_interest(principal, rate, years, 12)
    compound_interest = compound_amount - principal

    print("\n单利计算:")
    print(f"  最终金额: {simple_amount:,.2f} 元")
    print(f"  总利息: {simple_interest:,.2f} 元")

    print("\n复利计算（每月复利）:")
    print(f"  最终金额: {compound_amount:,.2f} 元")
    print(f"  总利息: {compound_interest:,.2f} 元")

    print("\n复利优势:")
    print(f"  多赚: {compound_interest - simple_interest:,.2f} 元")
    print(f"  复利是单利的: {compound_interest / simple_interest:.2f} 倍")

def calculate_years_to_double(rate):
    """
    使用72法则计算资金翻倍所需年数

    参数:
    rate: 年利率（百分比形式，如5表示5%）

    返回:
    翻倍所需年数
    """
    # 72法则: 翻倍年数 ≈ 72 / 年利率(%)
    years = 72 / rate
    return years

def demonstrate_72_rule():
    """演示72法则"""
    print("\n" + "=" * 60)
    print("72法则演示")
    print("=" * 60)
    print("\n72法则: 资金翻倍所需年数 ≈ 72 / 年利率(%)")
    print("\n不同利率下的翻倍时间:")
    print("-" * 40)

    rates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for rate in rates:
        years = calculate_years_to_double(rate)
        print(f"年利率 {rate:2d}%: 约 {years:.1f} 年翻倍")

def interactive_calculator():
    """交互式计算器"""
    print("\n" + "=" * 60)
    print("复利计算器")
    print("=" * 60)

    try:
        principal = float(input("\n请输入本金（元）: "))
        rate = float(input("请输入年利率（%，如5表示5%）: ")) / 100
        years = int(input("请输入投资年数: "))
        compounds = int(input("每年复利次数（12为月复利，4为季复利，1为年复利）: "))

        amount = calculate_compound_interest(principal, rate, years, compounds)
        interest = amount - principal

        print("\n计算结果:")
        print(f"初始本金: {principal:,.2f} 元")
        print(f"年利率: {rate*100:.2f}%")
        print(f"投资期限: {years} 年")
        print(f"复利频率: 每年 {compounds} 次")
        print(f"最终金额: {amount:,.2f} 元")
        print(f"总收益: {interest:,.2f} 元")
        print(f"收益率: {interest/principal*100:.2f}%")

        # 显示每年增长情况
        print("\n每年增长情况:")
        print("-" * 50)
        for year in range(1, years + 1):
            yearly_amount = calculate_compound_interest(principal, rate, year, compounds)
            yearly_interest = yearly_amount - principal
            print(f"第 {year:2d} 年: {yearly_amount:,.2f} 元 (收益: {yearly_interest:,.2f} 元)")

    except ValueError:
        print("输入错误，请输入有效的数字！")

def main():
    """主函数"""
    print("投资理财学习 - 复利计算器")
    print("这个工具帮助你理解复利效应的威力")

    while True:
        print("\n请选择功能:")
        print("1. 复利 vs 单利 演示")
        print("2. 72法则演示")
        print("3. 交互式复利计算器")
        print("4. 退出")

        choice = input("\n请输入选择 (1-4): ")

        if choice == '1':
            demonstrate_compound_vs_simple()
        elif choice == '2':
            demonstrate_72_rule()
        elif choice == '3':
            interactive_calculator()
        elif choice == '4':
            print("感谢使用复利计算器！")
            break
        else:
            print("无效选择，请重新输入！")

if __name__ == "__main__":
    main()
