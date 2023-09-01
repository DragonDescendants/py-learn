# 乘法层
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y
        return out

    def backward(self, d_out):
        dx = d_out * self.y  # 反转x和y
        dy = d_out * self.x
        return dx, dy


# test
apple = 100  # 苹果单价
apple_num = 2  # 苹果数量
tax = 1.1  # 苹果税率

mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# forward
apple_price = mul_apple_layer.forward(apple, apple_num)
total_price = mul_tax_layer.forward(apple_price, tax)
print(total_price)
# backward
d_total_price = 1
d_apple_price, d_tax = mul_tax_layer.backward(d_total_price)
d_apple, d_apple_num = mul_apple_layer.backward(d_apple_price)
print(d_apple, d_apple_num, d_apple_price, d_tax, d_total_price)


# 2.2 110.00000000000001 1.1 200 1

# 加法层
class AddLayer:
    def __init__(self):
        # 加法层无需特意初始化
        pass

    def forward(self, x, y):
        out = x + y
        return out

    def backward(self, d_out):
        dx = d_out * 1
        dy = d_out * 1
        return dx, dy
