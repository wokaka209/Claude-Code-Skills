#!/usr/bin/env python3
"""
预算计算器
帮助学习预算管理
"""

def calculate_budget_50_30_20(income):
    """
    使用50/30/20法则计算预算分配

    参数:
    income: 月收入

    返回:
    预算分配字典
    """
    # 50/30/20法则:
    # 50%用于必要支出（住房、食物、交通等）
    # 30%用于个人消费（娱乐、购物等）
    # 20%用于储蓄和还债

    needs = income * 0.50
    wants = income * 0.30
    savings = income * 0.20

    return {
        'needs': needs,
        'wants': wants,
        'savings': savings,
        'income': income
    }

def calculate_emergency_fund(monthly_expenses, months=6):
    """
    计算应急基金目标

    参数:
    monthly_expenses: 月支出
    months: 建议覆盖月数（默认6个月）

    返回:
    应急基金目标金额
    """
    return monthly_expenses * months

def calculate_savings_rate(income, savings):
    """
    计算储蓄率

    参数:
    income: 收入
    savings: 储蓄金额

    返回:
    储蓄率（百分比）
    """
    if income == 0:
        return 0
    return (savings / income) * 100

def demonstrate_budget_basics():
    """演示预算基础"""
    print("=" * 60)
    print("预算管理基础演示")
    print("=" * 60)

    # 假设月收入
    income = 10000  # 1万元

    print(f"\n假设月收入: {income:,.2f} 元")

    # 计算50/30/20预算
    budget = calculate_budget_50_30_20(income)

    print("\n50/30/20预算法则:")
    print("-" * 40)
    print(f"必要支出 (50%): {budget['needs']:,.2f} 元")
    print("  - 住房: 租金/房贷")
    print("  - 食物: 日常饮食")
    print("  - 交通: 通勤费用")
    print("  - 保险: 医疗保险等")
    print(f"个人消费 (30%): {budget['wants']:,.2f} 元")
    print("  - 娱乐: 电影、聚餐")
    print("  - 购物: 衣物、电子产品")
    print("  - 兴趣: 爱好、旅行")
    print(f"储蓄还债 (20%): {budget['savings']:,.2f} 元")
    print("  - 应急基金: 紧急备用金")
    print("  - 还债: 信用卡、贷款")
    print("  - 投资: 长期储蓄")

def demonstrate_emergency_fund():
    """演示应急基金"""
    print("\n" + "=" * 60)
    print("应急基金规划")
    print("=" * 60)

    monthly_expenses = 7000  # 假设月支出7000元

    print(f"\n假设月支出: {monthly_expenses:,.2f} 元")

    # 计算不同月数的应急基金
    print("\n应急基金目标:")
    print("-" * 40)

    for months in [3, 6, 9, 12]:
        fund = calculate_emergency_fund(monthly_expenses, months)
        print(f"{months}个月应急基金: {fund:,.2f} 元")

    print("\n应急基金建议:")
    print("1. 从3个月开始，逐步增加到6个月")
    print("2. 存放在高流动性账户（如货币基金）")
    print("3. 只用于真正的紧急情况")
    print("4. 定期补充，保持目标金额")

def demonstrate_savings_rate():
    """演示储蓄率"""
    print("\n" + "=" * 60)
    print("储蓄率计算")
    print("=" * 60)

    # 不同收入水平的储蓄率示例
    examples = [
        {"income": 5000, "savings": 500, "desc": "低收入高储蓄"},
        {"income": 10000, "savings": 2000, "desc": "中等收入标准储蓄"},
        {"income": 20000, "savings": 6000, "desc": "高收入高储蓄"},
        {"income": 10000, "savings": 0, "desc": "月光族"},
    ]

    print("\n不同储蓄率示例:")
    print("-" * 50)

    for example in examples:
        rate = calculate_savings_rate(example["income"], example["savings"])
        print(f"{example['desc']}:")
        print(f"  收入: {example['income']:,.2f} 元")
        print(f"  储蓄: {example['savings']:,.2f} 元")
        print(f"  储蓄率: {rate:.1f}%")
        print()

def interactive_budget_calculator():
    """交互式预算计算器"""
    print("\n" + "=" * 60)
    print("个人预算计算器")
    print("=" * 60)

    try:
        income = float(input("\n请输入月收入（元）: "))

        if income <= 0:
            print("收入必须大于0！")
            return

        # 计算50/30/20预算
        budget = calculate_budget_50_30_20(income)

        print("\n基于50/30/20法则的预算分配:")
        print("-" * 50)
        print(f"月收入: {income:,.2f} 元")
        print(f"必要支出 (50%): {budget['needs']:,.2f} 元")
        print(f"个人消费 (30%): {budget['wants']:,.2f} 元")
        print(f"储蓄还债 (20%): {budget['savings']:,.2f} 元")

        # 询问实际支出
        print("\n请输入实际支出情况:")
        actual_needs = float(input("必要支出（住房、食物、交通等）: "))
        actual_wants = float(input("个人消费（娱乐、购物等）: "))

        actual_total = actual_needs + actual_wants
        actual_savings = income - actual_total
        actual_rate = calculate_savings_rate(income, actual_savings)

        print("\n实际预算分析:")
        print("-" * 50)
        print(f"总支出: {actual_total:,.2f} 元")
        print(f"实际储蓄: {actual_savings:,.2f} 元")
        print(f"实际储蓄率: {actual_rate:.1f}%")

        # 与建议比较
        print("\n与建议比较:")
        print("-" * 50)
        if actual_needs > budget['needs']:
            print(f"⚠️  必要支出超支: {actual_needs - budget['needs']:,.2f} 元")
        else:
            print(f"✅ 必要支出在预算内")

        if actual_wants > budget['wants']:
            print(f"⚠️  个人消费超支: {actual_wants - budget['wants']:,.2f} 元")
        else:
            print(f"✅ 个人消费在预算内")

        if actual_savings >= budget['savings']:
            print(f"✅ 储蓄达标，多存了: {actual_savings - budget['savings']:,.2f} 元")
        else:
            print(f"⚠️  储蓄不足，差: {budget['savings'] - actual_savings:,.2f} 元")

        # 给出建议
        print("\n改进建议:")
        print("-" * 50)
        if actual_rate < 20:
            print("1. 考虑减少非必要支出")
            print("2. 寻找增加收入的机会")
            print("3. 设定自动储蓄计划")
        elif actual_rate < 30:
            print("1. 储蓄率良好，可以设定更高目标")
            print("2. 考虑将多余储蓄用于投资")
        else:
            print("1. 储蓄率优秀！")
            print("2. 可以考虑更多投资选择")

    except ValueError:
        print("输入错误，请输入有效的数字！")

def main():
    """主函数"""
    print("投资理财学习 - 预算计算器")
    print("这个工具帮助你学习预算管理")

    while True:
        print("\n请选择功能:")
        print("1. 50/30/20预算法则演示")
        print("2. 应急基金规划")
        print("3. 储蓄率计算")
        print("4. 个人预算计算器")
        print("5. 退出")

        choice = input("\n请输入选择 (1-5): ")

        if choice == '1':
            demonstrate_budget_basics()
        elif choice == '2':
            demonstrate_emergency_fund()
        elif choice == '3':
            demonstrate_savings_rate()
        elif choice == '4':
            interactive_budget_calculator()
        elif choice == '5':
            print("感谢使用预算计算器！")
            break
        else:
            print("无效选择，请重新输入！")

if __name__ == "__main__":
    main()
