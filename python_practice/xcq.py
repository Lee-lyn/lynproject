class XiChenQi:
    # 吸尘器的手动清理功能
    def clean(self, area):
        print(f"吸尘器没电了，手动清扫{area}")


class MyXcq(XiChenQi):
    def __init__(self, power):
        self.power = power

    def charge(self, add):
        self.power = self.power + add
        if self.power == 5:
            print("充电已完成！")
            print(f"吸尘器电量：{self.power}")
        elif self.power > 5:
            raise Exception("您期望充电量超过量程，请重新设置期望充电量")
        else:
            print(f"充电中……已充电量{self.power}格")
            print(f"吸尘器电量：{self.power}")

    def clean(self, area):
        a_area = self.power * 10
        if a_area >= area:
            print("我的吸尘器真给力！把整个屋子都清扫了！")
        else:
            print(f"吸尘器自动清扫了{a_area}平方米")
            super().clean(area - a_area)


xiaokeai = MyXcq(1)  # 吸尘器本身电量
xiaokeai.charge(3)  # 吸尘器充了多少电
xiaokeai.charge(3)  # 吸尘器充了多少电
xiaokeai.clean(50)
