"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""


# 定义一个 fight 函数
def fight():
    # 定义变量——血量
    blue_hp = 1000
    red_hp = 1000
    # 定义变量——共计值
    blue_power = 100
    red_power = 100
    # 一轮游戏后，蓝红双方剩余血量
    blue_hp = blue_hp - red_power
    red_hp = red_hp - blue_power
    if blue_hp>red_hp:
        print("蓝方胜！")
    elif blue_hp<red_hp:
        print("红方胜！")
    else:
        print("平局")
# # 调用 fight 函数
fight()