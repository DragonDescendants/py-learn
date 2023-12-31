import torch as t
# 获取元素
a = t.randn(3,4)
# 切片语法 start:stop:step [start,stop)
print('a:',a,'\n', # 输出整个tensor
      'a[0]:',a[0],'\n' #输出tensor的第0行
      'a[:,0]',a[:,0],'\n' #输出tensor的第0列
      'a[0][2]',a[0][2],a[0,2],'\n' #输出第0行第2列的元素
      'a[1][-1]',a[1][-1],a[1,-1],'\n' #输出第1行倒数第1个的元素
      'a[:2]',a[:2],'\n' # 输出前两行
      'a[:2,0:2]',a[:2,0:2],'\n' #输出前两行的0,1列
      'a[0:1,:2] or a[0,:2]',a[0:1,:2],a[0,:2],'\n' #两者输出的形状不同(2维,1维)
      'a>1',a>1,'\n' #判断其中的元素是否>1,得到ByteTensor
      'a[a>1]',a[a>1],'\n' #选出所有>1的元素,组成新的tensor
        #...
      )

'''
a: tensor([[ 0.7872, -0.5912, -1.2341,  0.2248],
        [ 0.4981,  0.9411,  0.3265, -1.0761],
        [-0.0748,  1.0530,  0.0282, -0.9017]])
 a[0]: tensor([ 0.7872, -0.5912, -1.2341,  0.2248])
a[:,0] tensor([ 0.7872,  0.4981, -0.0748])
a[0][2] tensor(-1.2341) tensor(-1.2341)
a[1][-1] tensor(-1.0761) tensor(-1.0761)
a[:2] tensor([[ 0.7872, -0.5912, -1.2341,  0.2248],
        [ 0.4981,  0.9411,  0.3265, -1.0761]])
a[:2,0:2] tensor([[ 0.7872, -0.5912],
        [ 0.4981,  0.9411]])
a[0:1,:2] or a[0,:2] tensor([[ 0.7872, -0.5912]]) 
tensor([ 0.7872, -0.5912])
a>1 tensor([[False, False, False, False],
        [False, False, False, False],
        [False,  True, False, False]])
a[a>1] tensor([1.0530])
'''