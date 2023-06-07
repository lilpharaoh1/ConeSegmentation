# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class SimpleNet(torch.nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.module_0 = py_nndct.nn.Input() #SimpleNet::input_0
        self.module_1 = py_nndct.nn.Conv2d(in_channels=1, out_channels=6, kernel_size=[5, 5], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #SimpleNet::SimpleNet/Conv2d[conv1]/20
        self.module_2 = py_nndct.nn.ReLU(inplace=False) #SimpleNet::SimpleNet/21
        self.module_3 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #SimpleNet::SimpleNet/input.2
        self.module_4 = py_nndct.nn.Conv2d(in_channels=6, out_channels=16, kernel_size=[5, 5], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #SimpleNet::SimpleNet/Conv2d[conv2]/37
        self.module_5 = py_nndct.nn.ReLU(inplace=False) #SimpleNet::SimpleNet/38
        self.module_6 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #SimpleNet::SimpleNet/44
        self.module_7 = py_nndct.nn.Module('flatten') #SimpleNet::SimpleNet/input.3
        self.module_8 = py_nndct.nn.Linear(in_features=256, out_features=120, bias=True) #SimpleNet::SimpleNet/Linear[fc1]/51
        self.module_9 = py_nndct.nn.ReLU(inplace=False) #SimpleNet::SimpleNet/input.4
        self.module_10 = py_nndct.nn.Linear(in_features=120, out_features=84, bias=True) #SimpleNet::SimpleNet/Linear[fc2]/56
        self.module_11 = py_nndct.nn.ReLU(inplace=False) #SimpleNet::SimpleNet/input
        self.module_12 = py_nndct.nn.Linear(in_features=84, out_features=10, bias=True) #SimpleNet::SimpleNet/Linear[fc3]/61

    def forward(self, *args):
        self.output_module_0 = self.module_0(input=args[0])
        self.output_module_1 = self.module_1(self.output_module_0)
        self.output_module_2 = self.module_2(self.output_module_1)
        self.output_module_3 = self.module_3(self.output_module_2)
        self.output_module_4 = self.module_4(self.output_module_3)
        self.output_module_5 = self.module_5(self.output_module_4)
        self.output_module_6 = self.module_6(self.output_module_5)
        self.output_module_7 = self.module_7(end_dim=3, input=self.output_module_6, start_dim=1)
        self.output_module_8 = self.module_8(self.output_module_7)
        self.output_module_9 = self.module_9(self.output_module_8)
        self.output_module_10 = self.module_10(self.output_module_9)
        self.output_module_11 = self.module_11(self.output_module_10)
        self.output_module_12 = self.module_12(self.output_module_11)
        return self.output_module_12
