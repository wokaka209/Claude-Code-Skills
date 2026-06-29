#!/usr/bin/env python3
"""
投资回报率计算器
帮助理解投资回报的概念
"""

def calculate_roi(initial_investment, final_value):
    """
    计算投资回报率（ROI）

    参数:
    initial_investment: 初始投资额
    final_value: 最终价值

    返回:
    ROI百分比
    """
    if initial_investment == 0:
        return 0
    roi = ((final_value - initial_investment) / initial_investment) * 100
    return roi

def calculate_annualized_return(initial_investment, final_value, years):
    """
    计算年化收益率

    参数:
    initial_investment: 初始投资额
    final_value: 最终价值
    years: 投资年数

    返回:
    年化收益率百分比
    """
    if initial_investment == 0 or years == 0:
        return 0
    # 年化收益率公式: (最终价值/初始投资)^(1/年数) - 1
    annualized_return = ((final_value / initial_investment) ** (1 / years) - 1) * 100
    return annualized_return

def calculate_total_return(initial_investment, final_value, dividends=0):
    """
    计算总回报（包括股息）

    参数:
    initial_investment: 初始投资额
    final_value: 最终价值
    dividends: 收到的股息

    返回:
    总回报金额和百分比
    """
    total_return = final_value - initial_investment + dividends
    total_return_percentage = (total_return / initial_investment) * 100 if initial_investment != 0 else 0

    return {
        'total_return': total_return,
        'total_return_percentage': total_return_percentage,
        'capital_gain': final_value - initial_investment,
        'dividends': dividends
    }

def demonstrate_roi_basics():
    """演示投资回报率基础"""
    print("=" * 60)
    print("投资回报率基础演示")
    print("=" * 60)

    # 示例投资
    examples = [
        {"name": "股票投资", "initial": 10000, "final": 12000, "years": 1},
        {"name": "基金投资", "initial": 50000, "final": 55000, "years": 2},
        {"name": "房产投资", "initial": 1000000, "final": 1200000, "years": 5},
        {"name": "定期存款", "initial": 20000, "final": 21000, "years": 1},
    ]

    print("\n不同投资回报率比较:")
    print("-" * 70)
    print(f"{'投资类型':<12} {'初始投资':<12} {'最终价值':<12} {'投资年数':<8} {'ROI':<10} {'年化收益率':<12}")
    print("-" * 70)

    for example in examples:
        roi = calculate_roi(example["initial"], example["final"])
        annualized = calculate_annualized_return(example["initial"], example["final"], example["years"])
        print(f"{example['name']:<12} {example['initial']:>10,.2f} {example['final']:>10,.2f} {example['years']:>6}年 {roi:>8.2f}% {annualized:>10.2f}%")

def demonstrate_dividend_impact():
    """演示股息对回报的影响"""
    print("\n" + "=" * 60)
    print("股息对投资回报的影响")
    print("=" * 60)

    initial_investment = 100000
    final_value = 110000
    dividends = 5000

    print(f"\n初始投资: {initial_investment:,.2f} 元")
    print(f"最终价值: {final_value:,.2f} 元")
    print(f"收到股息: {dividends:,.2f} 元")

    # 计算不含股息的回报
    return_without_dividends = calculate_total_return(initial_investment, final_value, 0)

    # 计算含股息的回报
    return_with_dividends = calculate_total_return(initial_investment, final_value, dividends)

    print("\n回报分析:")
    print("-" * 50)
    print("不含股息:")
    print(f"  资本利得: {return_without_dividends['capital_gain']:,.2f} 元")
    print(f"  总回报: {return_without_dividends['total_return']:,.2f} 元")
    print(f"  回报率: {return_without_dividends['total_return_percentage']:.2f}%")

    print("\n包含股息:")
    print(f"  资本利得: {return_with_dividends['capital_gain']:,.2f} 元")
    print(f"  股息收入: {return_with_dividends['dividends']:,.2f} 元")
    print(f"  总回报: {return_with_dividends['total_return']:,.2f} 元")
    print(f"  回报率: {return_with_dividends['total_return_percentage']:.2f}%")

    print("\n股息贡献:")
    print(f"  股息占总回报: {dividends / return_with_dividends['total_return'] * 100:.2f}%")

def demonstrate_risk_return():
    """演示风险与回报的关系"""
    print("\n" + "=" * 60)
    print("风险与回报的关系")
    print("=" * 60)

    print("\n不同风险等级的投资:")
    print("-" * 60)

    risk_levels = [
        {"name": "国债", "risk": "低", "expected_return": "2-4%", "description": "政府信用担保，安全性高"},
        {"name": "定期存款", "risk": "极低", "expected_return": "1-3%", "description": "银行存款保险保障"},
        {"name": "货币基金", "risk": "低", "expected_return": "2-3%", "description": "流动性好，风险低"},
        {"name": "债券基金", "risk": "中低", "expected_return": "3-6%", "description": "分散投资，风险适中"},
        {"name": "股票基金", "risk": "中高", "expected_return": "6-12%", "description": "波动较大，长期回报高"},
        {"name": "个股投资", "risk": "高", "expected_return": "不确定", "description": "可能高回报，也可能亏损"},
    ]

    for level in risk_levels:
        print(f"{level['name']} ({level['risk']}风险):")
        print(f"  预期回报: {level['expected_return']}")
        print(f"  特点: {level['description']}")
        print()

def demonstrate_time_impact():
    """演示时间对投资回报的影响"""
    print("\n" + "=" * 60)
    print("时间对投资回报的影响")
    print("=" * 60)

    principal = 10000
    rate = 0.07  # 7%年回报率

    print(f"\n初始投资: {principal:,.2f} 元")
    print(f"年回报率: {rate*100:.1f}%")
    print("\n不同投资期限的回报:")
    print("-" * 50)

    for years in [1, 5, 10, 15, 20, 25, 30]:
        # 使用复利计算
        final_value = principal * (1 + rate) ** years
        total_return = final_value - principal
        roi = calculate_roi(principal, final_value)

        print(f"{years:2d}年: 最终价值 {final_value:>12,.2f} 元, 总回报 {total_return:>10,.2f} 典, ROI {roi:>8.2f}%")

    print("\n关键启示:")
    print("1. 时间是投资最重要的朋友")
    print("2. 复利效应需要时间才能显现")
    print("3. 尽早开始投资，即使金额很小")

def interactive_return_calculator():
    """交互式投资回报计算器"""
    print("\n" + "=" * 60)
    print("投资回报计算器")
    print("=" * 60)

    try:
        print("\n请输入投资信息:")
        initial_investment = float(input("初始投资金额（元）: "))
        final_value = float(input("最终价值（元）: "))
        years = int(input("投资年数: "))
        dividends = float(input("收到的股息/利息（元，没有则输入0）: "))

        if initial_investment <= 0:
            print("初始投资必须大于0！")
            return

        # 计算各种回报指标
        roi = calculate_roi(initial_investment, final_value)
        annualized_return = calculate_annualized_return(initial_investment, final_value, years)
        total_return = calculate_total_return(initial_investment, final_value, dividends)

        print("\n投资回报分析:")
        print("-" * 50)
        print(f"初始投资: {initial_investment:,.2f} 元")
        print(f"最终价值: {final_value:,.2f} 元")
        print(f"投资期限: {years} 年")
        print(f"股息收入: {dividends:,.2f} 元")

        print("\n回报指标:")
        print("-" * 50)
        print(f"总回报金额: {total_return['total_return']:,.2f} 元")
        print(f"总回报率: {total_return['total_return_percentage']:.2f}%")
        print(f"年化收益率: {annualized_return:.2f}%")
        print(f"资本利得: {total_return['capital_gain']:,.2f} 元")

        # 评估投资表现
        print("\n投资评估:")
        print("-" * 50)
        if annualized_return > 10:
            print("✅ 表现优秀！年化收益率超过10%")
        elif annualized_return > 5:
            print("✅ 表现良好！年化收益率在5-10%之间")
        elif annualized_return > 0:
            print("✅ 表现一般，年化收益率在0-5%之间")
        else:
            print("⚠️  表现不佳，出现亏损")

        # 与通胀比较
        inflation_rate = 3.0  # 假设通胀率3%
        real_return = annualized_return - inflation_rate
        print(f"\n实际收益率（扣除通胀）: {real_return:.2f}%")
        if real_return > 0:
            print("✅ 投资回报跑赢通胀")
        else:
            print("⚠️  投资回报未能跑赢通胀")

    except ValueError:
        print("输入错误，请输入有效的数字！")

def main():
    """主函数"""
    print("投资理财学习 - 投资回报计算器")
    print("这个工具帮助你理解投资回报的概念")

    while True:
        print("\n请选择功能:")
        print("1. 投资回报率基础演示")
        print("2. 股息对回报的影响")
        print("3. 风险与回报关系")
        print("4. 时间对投资的影响")
        print("5. 交互式投资回报计算器")
        print("6. 退出")

        choice = input("\n请输入选择 (1-6): ")

        if choice == '1':
            demonstrate_roi_basics()
        elif choice == '2':
            demonstrate_dividend_impact()
        elif choice == '3':
            demonstrate_risk_return()
        elif choice == '4':
            demonstrate_time_impact()
        elif choice == '5':
            interactive_return_calculator()
        elif choice == '6':
            print("感谢使用投资回报计算器！")
            break
        else:
            print("无效选择，请重新输入！")

if __name__ == "__main__":
    main()
