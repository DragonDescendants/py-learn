import torch as t

# 设置默认的tensor类型
t.set_default_tensor_type("torch.FloatTensor")
a = t.tensor([3, 6, 9], dtype=t.float64)
b = t.arange(0, 12)
print(a.dtype, b.dtype) #torch.float64 torch.int64
c = b.type_as(a)  # 把tensor b的类型转换成a的,创建新的tensor c
print(a.dtype, b.dtype, c.dtype) #torch.float64 torch.int64 torch.float64


# Tensor 还有 new方法,该用法与 t.Tensor 一样，会调用
# tensor 对应类型的构造函数，生成与当 tensor 类型一致的 tensor
d = a.new(2,4)
print(d.dtype,d.shape) #torch.float64 torch.Size([2, 4])