# 定义一个Bicycle类，有run方法，调用时显示骑行里程m（传入的数据）
class Bicycle:
    def run(self, m):
        # 字面量插值，传递 m 参数
        print(f"脚蹬了{m}m，好累呀！")


# 定义一个EBicycle类，继承Bicycle,Bicycle要写在括号里，不能写入参数
class EBicycle(Bicycle):
    # 类属性：在类中，方法之外，如：valume=1000
    # 添加一个电池电量valume属性，通过参数传入（注意：类的参数要在构造方法里去写）
    # 构造方法，里面可以定义传入的参数
    def __init__(self, valume):
        # 实例属性：在类中，在方法中，并且以"self.变量名"的方式定义,加了self后，在类中其他的方法中也可以调用这个参数了
        self.valume = valume
        # 普通属性：在类中，方法中，称为局部变量，只能在当前的方法中使用，如：valume=valume，没有self

    # fill_charge(vol)用来充电，vol为充电量
    def fill_charge(self, vol):
        # 充电后的电量
        self.valume = self.valume + vol
        print(f"电动车已充电{vol}度")
        print(f"充完电后有{self.valume}度电")

    def run(self, m):
        # 用电池骑行的千里数（1度电可以骑1000m）
        e_m = self.valume * 1000
        # 如果总路程小于等于电可以骑的路程，输出用电骑的路程，并输出“有电动车就是好！”
        if m <= e_m:
            print(f"用电骑了{m}m，有电动车就是好！")
        # 如果总路程大于用电可以骑的路程，输出用电骑的路程和用脚蹬的路程
        elif m - e_m >= 1000:
            print(f"用电骑了{e_m}m")
            # 调用父类方法（能同时调用父类的方法和子类的方法）：super().方法名() ,有参数则需要传参
            super().run(m - e_m)
        else:
            print(f"用电骑了{e_m}m")
            print(f"用脚骑了{m - e_m}m")


# 实例化。子类继承父类，可以调用父类的属性和方法
# 实例化的时候，需要传入构造方法的参数
ebike = EBicycle(1)  # 此处传入的是电动车已有电量
ebike.fill_charge(3)  # 此处传入电动车已经充了的电量
ebike.run(5000)  # 此处传入总的路程
