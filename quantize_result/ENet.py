# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class ENet(torch.nn.Module):
    def __init__(self):
        super(ENet, self).__init__()
        self.module_0 = py_nndct.nn.Input() #ENet::input_0
        self.module_1 = py_nndct.nn.Conv2d(in_channels=3, out_channels=13, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=False) #ENet::ENet/InitialBlock[initial]/Conv2d[conv]/536
        self.module_2 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #ENet::ENet/InitialBlock[initial]/MaxPool2d[maxpool]/542
        self.module_3 = py_nndct.nn.Cat() #ENet::ENet/InitialBlock[initial]/input.2
        self.module_4 = py_nndct.nn.Module('batch_norm',num_features=16, eps=0.0, momentum=0.1) #ENet::ENet/InitialBlock[initial]/BatchNorm2d[bn]/input.3
        self.module_5 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/InitialBlock[initial]/LeakyReLU[act]/input.6
        self.module_6 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #ENet::ENet/Bottleneck[bottleneck1_0]/MaxPool2d[maxpool]/input.4
        self.module_7 = py_nndct.nn.Conv2d(in_channels=16, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_0]/Sequential[conv_down]/Conv2d[0]/input.5
        self.module_9 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_0]/Sequential[conv1]/Conv2d[0]/input.7
        self.module_11 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_0]/Sequential[conv1]/LeakyReLU[2]/input.9
        self.module_12 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_0]/Sequential[conv2]/Conv2d[0]/input.10
        self.module_14 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_0]/Sequential[conv2]/LeakyReLU[2]/input.12
        self.module_15 = py_nndct.nn.Conv2d(in_channels=16, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_0]/Sequential[conv3]/Conv2d[0]/input.13
        self.module_18 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck1_0]/input.15
        self.module_19 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_0]/LeakyReLU[act]/input.16
        self.module_20 = py_nndct.nn.Conv2d(in_channels=64, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_1]/Sequential[conv1]/Conv2d[0]/input.17
        self.module_22 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_1]/Sequential[conv1]/LeakyReLU[2]/input.19
        self.module_23 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_1]/Sequential[conv2]/Conv2d[0]/input.20
        self.module_25 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_1]/Sequential[conv2]/LeakyReLU[2]/input.22
        self.module_26 = py_nndct.nn.Conv2d(in_channels=16, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_1]/Sequential[conv3]/Conv2d[0]/input.23
        self.module_29 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck1_1]/input.25
        self.module_30 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_1]/LeakyReLU[act]/input.26
        self.module_31 = py_nndct.nn.Conv2d(in_channels=64, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_2]/Sequential[conv1]/Conv2d[0]/input.27
        self.module_33 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_2]/Sequential[conv1]/LeakyReLU[2]/input.29
        self.module_34 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_2]/Sequential[conv2]/Conv2d[0]/input.30
        self.module_36 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_2]/Sequential[conv2]/LeakyReLU[2]/input.32
        self.module_37 = py_nndct.nn.Conv2d(in_channels=16, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_2]/Sequential[conv3]/Conv2d[0]/input.33
        self.module_40 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck1_2]/input.35
        self.module_41 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_2]/LeakyReLU[act]/input.36
        self.module_42 = py_nndct.nn.Conv2d(in_channels=64, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_3]/Sequential[conv1]/Conv2d[0]/input.37
        self.module_44 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_3]/Sequential[conv1]/LeakyReLU[2]/input.39
        self.module_45 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_3]/Sequential[conv2]/Conv2d[0]/input.40
        self.module_47 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_3]/Sequential[conv2]/LeakyReLU[2]/input.42
        self.module_48 = py_nndct.nn.Conv2d(in_channels=16, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_3]/Sequential[conv3]/Conv2d[0]/input.43
        self.module_51 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck1_3]/input.45
        self.module_52 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_3]/LeakyReLU[act]/input.46
        self.module_53 = py_nndct.nn.Conv2d(in_channels=64, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_4]/Sequential[conv1]/Conv2d[0]/input.47
        self.module_55 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_4]/Sequential[conv1]/LeakyReLU[2]/input.49
        self.module_56 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_4]/Sequential[conv2]/Conv2d[0]/input.50
        self.module_58 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_4]/Sequential[conv2]/LeakyReLU[2]/input.52
        self.module_59 = py_nndct.nn.Conv2d(in_channels=16, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck1_4]/Sequential[conv3]/Conv2d[0]/input.53
        self.module_62 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck1_4]/input.55
        self.module_63 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck1_4]/LeakyReLU[act]/input.58
        self.module_64 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #ENet::ENet/Bottleneck[bottleneck2_0]/MaxPool2d[maxpool]/input.56
        self.module_65 = py_nndct.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_0]/Sequential[conv_down]/Conv2d[0]/input.57
        self.module_67 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_0]/Sequential[conv1]/Conv2d[0]/input.59
        self.module_69 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_0]/Sequential[conv1]/LeakyReLU[2]/input.61
        self.module_70 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_0]/Sequential[conv2]/Conv2d[0]/input.62
        self.module_72 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_0]/Sequential[conv2]/LeakyReLU[2]/input.64
        self.module_73 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_0]/Sequential[conv3]/Conv2d[0]/input.65
        self.module_76 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck2_0]/input.67
        self.module_77 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_0]/LeakyReLU[act]/input.68
        self.module_78 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_1]/Sequential[conv1]/Conv2d[0]/input.69
        self.module_80 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_1]/Sequential[conv1]/LeakyReLU[2]/input.71
        self.module_81 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_1]/Sequential[conv2]/Conv2d[0]/input.72
        self.module_83 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_1]/Sequential[conv2]/LeakyReLU[2]/input.74
        self.module_84 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_1]/Sequential[conv3]/Conv2d[0]/input.75
        self.module_87 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck2_1]/input.77
        self.module_88 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_1]/LeakyReLU[act]/input.78
        self.module_89 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_2]/Sequential[conv1]/Conv2d[0]/input.79
        self.module_91 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_2]/Sequential[conv1]/LeakyReLU[2]/input.81
        self.module_92 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[2, 2], dilation=[2, 2], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_2]/Sequential[conv2]/Conv2d[0]/input.82
        self.module_94 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_2]/Sequential[conv2]/LeakyReLU[2]/input.84
        self.module_95 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_2]/Sequential[conv3]/Conv2d[0]/input.85
        self.module_98 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck2_2]/input.87
        self.module_99 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_2]/LeakyReLU[act]/input.88
        self.module_100 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_3]/Sequential[conv1]/Conv2d[0]/input.89
        self.module_102 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_3]/Sequential[conv1]/LeakyReLU[2]/input.91
        self.module_103 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[5, 1], stride=[1, 1], padding=[2, 0], dilation=[1, 1], groups=1, bias=False) #ENet::ENet/Bottleneck[bottleneck2_3]/Sequential[conv2]/Conv2d[0]/input.92
        self.module_104 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 5], stride=[1, 1], padding=[0, 2], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_3]/Sequential[conv2]/Conv2d[1]/input.93
        self.module_106 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_3]/Sequential[conv2]/LeakyReLU[3]/input.95
        self.module_107 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_3]/Sequential[conv3]/Conv2d[0]/input.96
        self.module_110 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck2_3]/input.98
        self.module_111 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_3]/LeakyReLU[act]/input.99
        self.module_112 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_4]/Sequential[conv1]/Conv2d[0]/input.100
        self.module_114 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_4]/Sequential[conv1]/LeakyReLU[2]/input.102
        self.module_115 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_4]/Sequential[conv2]/Conv2d[0]/input.103
        self.module_117 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_4]/Sequential[conv2]/LeakyReLU[2]/input.105
        self.module_118 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_4]/Sequential[conv3]/Conv2d[0]/input.106
        self.module_121 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck2_4]/input.108
        self.module_122 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_4]/LeakyReLU[act]/input.109
        self.module_123 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_5]/Sequential[conv1]/Conv2d[0]/input.110
        self.module_125 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_5]/Sequential[conv1]/LeakyReLU[2]/input.112
        self.module_126 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_5]/Sequential[conv2]/Conv2d[0]/input.113
        self.module_128 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_5]/Sequential[conv2]/LeakyReLU[2]/input.115
        self.module_129 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_5]/Sequential[conv3]/Conv2d[0]/input.116
        self.module_132 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck2_5]/input.118
        self.module_133 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_5]/LeakyReLU[act]/input.119
        self.module_134 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_6]/Sequential[conv1]/Conv2d[0]/input.120
        self.module_136 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_6]/Sequential[conv1]/LeakyReLU[2]/input.122
        self.module_137 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[8, 8], dilation=[8, 8], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_6]/Sequential[conv2]/Conv2d[0]/input.123
        self.module_139 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_6]/Sequential[conv2]/LeakyReLU[2]/input.125
        self.module_140 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_6]/Sequential[conv3]/Conv2d[0]/input.126
        self.module_143 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck2_6]/input.128
        self.module_144 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_6]/LeakyReLU[act]/input.129
        self.module_145 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_7]/Sequential[conv1]/Conv2d[0]/input.130
        self.module_147 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_7]/Sequential[conv1]/LeakyReLU[2]/input.132
        self.module_148 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[5, 1], stride=[1, 1], padding=[2, 0], dilation=[1, 1], groups=1, bias=False) #ENet::ENet/Bottleneck[bottleneck2_7]/Sequential[conv2]/Conv2d[0]/input.133
        self.module_149 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 5], stride=[1, 1], padding=[0, 2], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_7]/Sequential[conv2]/Conv2d[1]/input.134
        self.module_151 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_7]/Sequential[conv2]/LeakyReLU[3]/input.136
        self.module_152 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_7]/Sequential[conv3]/Conv2d[0]/input.137
        self.module_155 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck2_7]/input.139
        self.module_156 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_7]/LeakyReLU[act]/input.140
        self.module_157 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_8]/Sequential[conv1]/Conv2d[0]/input.141
        self.module_159 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_8]/Sequential[conv1]/LeakyReLU[2]/input.143
        self.module_160 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[16, 16], dilation=[16, 16], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_8]/Sequential[conv2]/Conv2d[0]/input.144
        self.module_162 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_8]/Sequential[conv2]/LeakyReLU[2]/input.146
        self.module_163 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck2_8]/Sequential[conv3]/Conv2d[0]/input.147
        self.module_166 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck2_8]/input.149
        self.module_167 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck2_8]/LeakyReLU[act]/input.150
        self.module_168 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_1]/Sequential[conv1]/Conv2d[0]/input.151
        self.module_170 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_1]/Sequential[conv1]/LeakyReLU[2]/input.153
        self.module_171 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_1]/Sequential[conv2]/Conv2d[0]/input.154
        self.module_173 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_1]/Sequential[conv2]/LeakyReLU[2]/input.156
        self.module_174 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_1]/Sequential[conv3]/Conv2d[0]/input.157
        self.module_177 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck3_1]/input.159
        self.module_178 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_1]/LeakyReLU[act]/input.160
        self.module_179 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_2]/Sequential[conv1]/Conv2d[0]/input.161
        self.module_181 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_2]/Sequential[conv1]/LeakyReLU[2]/input.163
        self.module_182 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[2, 2], dilation=[2, 2], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_2]/Sequential[conv2]/Conv2d[0]/input.164
        self.module_184 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_2]/Sequential[conv2]/LeakyReLU[2]/input.166
        self.module_185 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_2]/Sequential[conv3]/Conv2d[0]/input.167
        self.module_188 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck3_2]/input.169
        self.module_189 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_2]/LeakyReLU[act]/input.170
        self.module_190 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_3]/Sequential[conv1]/Conv2d[0]/input.171
        self.module_192 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_3]/Sequential[conv1]/LeakyReLU[2]/input.173
        self.module_193 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[5, 1], stride=[1, 1], padding=[2, 0], dilation=[1, 1], groups=1, bias=False) #ENet::ENet/Bottleneck[bottleneck3_3]/Sequential[conv2]/Conv2d[0]/input.174
        self.module_194 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 5], stride=[1, 1], padding=[0, 2], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_3]/Sequential[conv2]/Conv2d[1]/input.175
        self.module_196 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_3]/Sequential[conv2]/LeakyReLU[3]/input.177
        self.module_197 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_3]/Sequential[conv3]/Conv2d[0]/input.178
        self.module_200 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck3_3]/input.180
        self.module_201 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_3]/LeakyReLU[act]/input.181
        self.module_202 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_4]/Sequential[conv1]/Conv2d[0]/input.182
        self.module_204 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_4]/Sequential[conv1]/LeakyReLU[2]/input.184
        self.module_205 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_4]/Sequential[conv2]/Conv2d[0]/input.185
        self.module_207 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_4]/Sequential[conv2]/LeakyReLU[2]/input.187
        self.module_208 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_4]/Sequential[conv3]/Conv2d[0]/input.188
        self.module_211 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck3_4]/input.190
        self.module_212 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_4]/LeakyReLU[act]/input.191
        self.module_213 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_6]/Sequential[conv1]/Conv2d[0]/input.192
        self.module_215 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_6]/Sequential[conv1]/LeakyReLU[2]/input.194
        self.module_216 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[8, 8], dilation=[8, 8], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_6]/Sequential[conv2]/Conv2d[0]/input.195
        self.module_218 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_6]/Sequential[conv2]/LeakyReLU[2]/input.197
        self.module_219 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_6]/Sequential[conv3]/Conv2d[0]/input.198
        self.module_222 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck3_6]/input.200
        self.module_223 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_6]/LeakyReLU[act]/input.201
        self.module_224 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_7]/Sequential[conv1]/Conv2d[0]/input.202
        self.module_226 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_7]/Sequential[conv1]/LeakyReLU[2]/input.204
        self.module_227 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[5, 1], stride=[1, 1], padding=[2, 0], dilation=[1, 1], groups=1, bias=False) #ENet::ENet/Bottleneck[bottleneck3_7]/Sequential[conv2]/Conv2d[0]/input.205
        self.module_228 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 5], stride=[1, 1], padding=[0, 2], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_7]/Sequential[conv2]/Conv2d[1]/input.206
        self.module_230 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_7]/Sequential[conv2]/LeakyReLU[3]/input.208
        self.module_231 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_7]/Sequential[conv3]/Conv2d[0]/input.209
        self.module_234 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck3_7]/input.211
        self.module_235 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_7]/LeakyReLU[act]/input.212
        self.module_236 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_8]/Sequential[conv1]/Conv2d[0]/input.213
        self.module_238 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_8]/Sequential[conv1]/LeakyReLU[2]/input.215
        self.module_239 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[16, 16], dilation=[16, 16], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_8]/Sequential[conv2]/Conv2d[0]/input.216
        self.module_241 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_8]/Sequential[conv2]/LeakyReLU[2]/input.218
        self.module_242 = py_nndct.nn.Conv2d(in_channels=32, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck3_8]/Sequential[conv3]/Conv2d[0]/input.219
        self.module_245 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck3_8]/input.221
        self.module_246 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck3_8]/LeakyReLU[act]/input.222
        self.module_247 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/UpsamplingBottleneck[bottleneck4_0]/Sequential[conv]/Conv2d[0]/input.223
        self.module_249 = py_nndct.nn.ConvTranspose2d(in_channels=64, out_channels=64, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #ENet::ENet/UpsamplingBottleneck[bottleneck4_0]/ConvTranspose2d[upsampling]/1905
        self.module_250 = py_nndct.nn.Conv2d(in_channels=128, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/UpsamplingBottleneck[bottleneck4_0]/Sequential[block]/Conv2d[0]/input.224
        self.module_252 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/UpsamplingBottleneck[bottleneck4_0]/Sequential[block]/LeakyReLU[2]/1923
        self.module_253 = py_nndct.nn.ConvTranspose2d(in_channels=16, out_channels=16, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #ENet::ENet/UpsamplingBottleneck[bottleneck4_0]/Sequential[block]/ConvTranspose2d[3]/input.226
        self.module_255 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/UpsamplingBottleneck[bottleneck4_0]/Sequential[block]/LeakyReLU[5]/input.228
        self.module_256 = py_nndct.nn.Conv2d(in_channels=16, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/UpsamplingBottleneck[bottleneck4_0]/Sequential[block]/Conv2d[6]/input.229
        self.module_259 = py_nndct.nn.Add() #ENet::ENet/UpsamplingBottleneck[bottleneck4_0]/input.231
        self.module_260 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/UpsamplingBottleneck[bottleneck4_0]/LeakyReLU[act]/input.232
        self.module_261 = py_nndct.nn.Conv2d(in_channels=64, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck4_1]/Sequential[conv1]/Conv2d[0]/input.233
        self.module_263 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck4_1]/Sequential[conv1]/LeakyReLU[2]/input.235
        self.module_264 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck4_1]/Sequential[conv2]/Conv2d[0]/input.236
        self.module_266 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck4_1]/Sequential[conv2]/LeakyReLU[2]/input.238
        self.module_267 = py_nndct.nn.Conv2d(in_channels=16, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck4_1]/Sequential[conv3]/Conv2d[0]/input.239
        self.module_270 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck4_1]/input.241
        self.module_271 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck4_1]/LeakyReLU[act]/input.242
        self.module_272 = py_nndct.nn.Conv2d(in_channels=64, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck4_2]/Sequential[conv1]/Conv2d[0]/input.243
        self.module_274 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck4_2]/Sequential[conv1]/LeakyReLU[2]/input.245
        self.module_275 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck4_2]/Sequential[conv2]/Conv2d[0]/input.246
        self.module_277 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck4_2]/Sequential[conv2]/LeakyReLU[2]/input.248
        self.module_278 = py_nndct.nn.Conv2d(in_channels=16, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck4_2]/Sequential[conv3]/Conv2d[0]/input.249
        self.module_281 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck4_2]/input.251
        self.module_282 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck4_2]/LeakyReLU[act]/input.252
        self.module_283 = py_nndct.nn.Conv2d(in_channels=64, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/UpsamplingBottleneck[bottleneck5_0]/Sequential[conv]/Conv2d[0]/input.253
        self.module_285 = py_nndct.nn.ConvTranspose2d(in_channels=16, out_channels=16, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #ENet::ENet/UpsamplingBottleneck[bottleneck5_0]/ConvTranspose2d[upsampling]/2108
        self.module_286 = py_nndct.nn.Conv2d(in_channels=64, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/UpsamplingBottleneck[bottleneck5_0]/Sequential[block]/Conv2d[0]/input.254
        self.module_288 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/UpsamplingBottleneck[bottleneck5_0]/Sequential[block]/LeakyReLU[2]/2126
        self.module_289 = py_nndct.nn.ConvTranspose2d(in_channels=4, out_channels=4, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #ENet::ENet/UpsamplingBottleneck[bottleneck5_0]/Sequential[block]/ConvTranspose2d[3]/input.256
        self.module_291 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/UpsamplingBottleneck[bottleneck5_0]/Sequential[block]/LeakyReLU[5]/input.258
        self.module_292 = py_nndct.nn.Conv2d(in_channels=4, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/UpsamplingBottleneck[bottleneck5_0]/Sequential[block]/Conv2d[6]/input.259
        self.module_295 = py_nndct.nn.Add() #ENet::ENet/UpsamplingBottleneck[bottleneck5_0]/input.261
        self.module_296 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/UpsamplingBottleneck[bottleneck5_0]/LeakyReLU[act]/input.262
        self.module_297 = py_nndct.nn.Conv2d(in_channels=16, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck5_1]/Sequential[conv1]/Conv2d[0]/input.263
        self.module_299 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck5_1]/Sequential[conv1]/LeakyReLU[2]/input.265
        self.module_300 = py_nndct.nn.Conv2d(in_channels=4, out_channels=4, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck5_1]/Sequential[conv2]/Conv2d[0]/input.266
        self.module_302 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck5_1]/Sequential[conv2]/LeakyReLU[2]/input.268
        self.module_303 = py_nndct.nn.Conv2d(in_channels=4, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #ENet::ENet/Bottleneck[bottleneck5_1]/Sequential[conv3]/Conv2d[0]/input.269
        self.module_306 = py_nndct.nn.Add() #ENet::ENet/Bottleneck[bottleneck5_1]/input
        self.module_307 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #ENet::ENet/Bottleneck[bottleneck5_1]/LeakyReLU[act]/2226
        self.module_308 = py_nndct.nn.ConvTranspose2d(in_channels=16, out_channels=1, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], output_padding=[0, 0], groups=1, bias=False, dilation=[1, 1]) #ENet::ENet/ConvTranspose2d[fullconv]/2237

    def forward(self, *args):
        self.output_module_0 = self.module_0(input=args[0])
        self.output_module_1 = self.module_1(self.output_module_0)
        self.output_module_2 = self.module_2(self.output_module_0)
        self.output_module_3 = self.module_3(tensors=[self.output_module_1,self.output_module_2], dim=1)
        self.output_module_4 = self.module_4(self.output_module_3)
        self.output_module_5 = self.module_5(self.output_module_4)
        self.output_module_6 = self.module_6(self.output_module_5)
        self.output_module_7 = self.module_7(self.output_module_6)
        self.output_module_9 = self.module_9(self.output_module_5)
        self.output_module_11 = self.module_11(self.output_module_9)
        self.output_module_12 = self.module_12(self.output_module_11)
        self.output_module_14 = self.module_14(self.output_module_12)
        self.output_module_15 = self.module_15(self.output_module_14)
        self.output_module_18 = self.module_18(alpha=1, other=self.output_module_7, input=self.output_module_15)
        self.output_module_19 = self.module_19(self.output_module_18)
        self.output_module_20 = self.module_20(self.output_module_19)
        self.output_module_22 = self.module_22(self.output_module_20)
        self.output_module_23 = self.module_23(self.output_module_22)
        self.output_module_25 = self.module_25(self.output_module_23)
        self.output_module_26 = self.module_26(self.output_module_25)
        self.output_module_29 = self.module_29(alpha=1, other=self.output_module_19, input=self.output_module_26)
        self.output_module_30 = self.module_30(self.output_module_29)
        self.output_module_31 = self.module_31(self.output_module_30)
        self.output_module_33 = self.module_33(self.output_module_31)
        self.output_module_34 = self.module_34(self.output_module_33)
        self.output_module_36 = self.module_36(self.output_module_34)
        self.output_module_37 = self.module_37(self.output_module_36)
        self.output_module_40 = self.module_40(alpha=1, other=self.output_module_30, input=self.output_module_37)
        self.output_module_41 = self.module_41(self.output_module_40)
        self.output_module_42 = self.module_42(self.output_module_41)
        self.output_module_44 = self.module_44(self.output_module_42)
        self.output_module_45 = self.module_45(self.output_module_44)
        self.output_module_47 = self.module_47(self.output_module_45)
        self.output_module_48 = self.module_48(self.output_module_47)
        self.output_module_51 = self.module_51(alpha=1, other=self.output_module_41, input=self.output_module_48)
        self.output_module_52 = self.module_52(self.output_module_51)
        self.output_module_53 = self.module_53(self.output_module_52)
        self.output_module_55 = self.module_55(self.output_module_53)
        self.output_module_56 = self.module_56(self.output_module_55)
        self.output_module_58 = self.module_58(self.output_module_56)
        self.output_module_59 = self.module_59(self.output_module_58)
        self.output_module_62 = self.module_62(alpha=1, other=self.output_module_52, input=self.output_module_59)
        self.output_module_63 = self.module_63(self.output_module_62)
        self.output_module_64 = self.module_64(self.output_module_63)
        self.output_module_65 = self.module_65(self.output_module_64)
        self.output_module_67 = self.module_67(self.output_module_63)
        self.output_module_69 = self.module_69(self.output_module_67)
        self.output_module_70 = self.module_70(self.output_module_69)
        self.output_module_72 = self.module_72(self.output_module_70)
        self.output_module_73 = self.module_73(self.output_module_72)
        self.output_module_76 = self.module_76(alpha=1, other=self.output_module_65, input=self.output_module_73)
        self.output_module_77 = self.module_77(self.output_module_76)
        self.output_module_78 = self.module_78(self.output_module_77)
        self.output_module_80 = self.module_80(self.output_module_78)
        self.output_module_81 = self.module_81(self.output_module_80)
        self.output_module_83 = self.module_83(self.output_module_81)
        self.output_module_84 = self.module_84(self.output_module_83)
        self.output_module_87 = self.module_87(alpha=1, other=self.output_module_77, input=self.output_module_84)
        self.output_module_88 = self.module_88(self.output_module_87)
        self.output_module_89 = self.module_89(self.output_module_88)
        self.output_module_91 = self.module_91(self.output_module_89)
        self.output_module_92 = self.module_92(self.output_module_91)
        self.output_module_94 = self.module_94(self.output_module_92)
        self.output_module_95 = self.module_95(self.output_module_94)
        self.output_module_98 = self.module_98(alpha=1, other=self.output_module_88, input=self.output_module_95)
        self.output_module_99 = self.module_99(self.output_module_98)
        self.output_module_100 = self.module_100(self.output_module_99)
        self.output_module_102 = self.module_102(self.output_module_100)
        self.output_module_103 = self.module_103(self.output_module_102)
        self.output_module_104 = self.module_104(self.output_module_103)
        self.output_module_106 = self.module_106(self.output_module_104)
        self.output_module_107 = self.module_107(self.output_module_106)
        self.output_module_110 = self.module_110(alpha=1, other=self.output_module_99, input=self.output_module_107)
        self.output_module_111 = self.module_111(self.output_module_110)
        self.output_module_112 = self.module_112(self.output_module_111)
        self.output_module_114 = self.module_114(self.output_module_112)
        self.output_module_115 = self.module_115(self.output_module_114)
        self.output_module_117 = self.module_117(self.output_module_115)
        self.output_module_118 = self.module_118(self.output_module_117)
        self.output_module_121 = self.module_121(alpha=1, other=self.output_module_111, input=self.output_module_118)
        self.output_module_122 = self.module_122(self.output_module_121)
        self.output_module_123 = self.module_123(self.output_module_122)
        self.output_module_125 = self.module_125(self.output_module_123)
        self.output_module_126 = self.module_126(self.output_module_125)
        self.output_module_128 = self.module_128(self.output_module_126)
        self.output_module_129 = self.module_129(self.output_module_128)
        self.output_module_132 = self.module_132(alpha=1, other=self.output_module_122, input=self.output_module_129)
        self.output_module_133 = self.module_133(self.output_module_132)
        self.output_module_134 = self.module_134(self.output_module_133)
        self.output_module_136 = self.module_136(self.output_module_134)
        self.output_module_137 = self.module_137(self.output_module_136)
        self.output_module_139 = self.module_139(self.output_module_137)
        self.output_module_140 = self.module_140(self.output_module_139)
        self.output_module_143 = self.module_143(alpha=1, other=self.output_module_133, input=self.output_module_140)
        self.output_module_144 = self.module_144(self.output_module_143)
        self.output_module_145 = self.module_145(self.output_module_144)
        self.output_module_147 = self.module_147(self.output_module_145)
        self.output_module_148 = self.module_148(self.output_module_147)
        self.output_module_149 = self.module_149(self.output_module_148)
        self.output_module_151 = self.module_151(self.output_module_149)
        self.output_module_152 = self.module_152(self.output_module_151)
        self.output_module_155 = self.module_155(alpha=1, other=self.output_module_144, input=self.output_module_152)
        self.output_module_156 = self.module_156(self.output_module_155)
        self.output_module_157 = self.module_157(self.output_module_156)
        self.output_module_159 = self.module_159(self.output_module_157)
        self.output_module_160 = self.module_160(self.output_module_159)
        self.output_module_162 = self.module_162(self.output_module_160)
        self.output_module_163 = self.module_163(self.output_module_162)
        self.output_module_166 = self.module_166(alpha=1, other=self.output_module_156, input=self.output_module_163)
        self.output_module_167 = self.module_167(self.output_module_166)
        self.output_module_168 = self.module_168(self.output_module_167)
        self.output_module_170 = self.module_170(self.output_module_168)
        self.output_module_171 = self.module_171(self.output_module_170)
        self.output_module_173 = self.module_173(self.output_module_171)
        self.output_module_174 = self.module_174(self.output_module_173)
        self.output_module_177 = self.module_177(alpha=1, other=self.output_module_167, input=self.output_module_174)
        self.output_module_178 = self.module_178(self.output_module_177)
        self.output_module_179 = self.module_179(self.output_module_178)
        self.output_module_181 = self.module_181(self.output_module_179)
        self.output_module_182 = self.module_182(self.output_module_181)
        self.output_module_184 = self.module_184(self.output_module_182)
        self.output_module_185 = self.module_185(self.output_module_184)
        self.output_module_188 = self.module_188(alpha=1, other=self.output_module_178, input=self.output_module_185)
        self.output_module_189 = self.module_189(self.output_module_188)
        self.output_module_190 = self.module_190(self.output_module_189)
        self.output_module_192 = self.module_192(self.output_module_190)
        self.output_module_193 = self.module_193(self.output_module_192)
        self.output_module_194 = self.module_194(self.output_module_193)
        self.output_module_196 = self.module_196(self.output_module_194)
        self.output_module_197 = self.module_197(self.output_module_196)
        self.output_module_200 = self.module_200(alpha=1, other=self.output_module_189, input=self.output_module_197)
        self.output_module_201 = self.module_201(self.output_module_200)
        self.output_module_202 = self.module_202(self.output_module_201)
        self.output_module_204 = self.module_204(self.output_module_202)
        self.output_module_205 = self.module_205(self.output_module_204)
        self.output_module_207 = self.module_207(self.output_module_205)
        self.output_module_208 = self.module_208(self.output_module_207)
        self.output_module_211 = self.module_211(alpha=1, other=self.output_module_201, input=self.output_module_208)
        self.output_module_212 = self.module_212(self.output_module_211)
        self.output_module_213 = self.module_213(self.output_module_212)
        self.output_module_215 = self.module_215(self.output_module_213)
        self.output_module_216 = self.module_216(self.output_module_215)
        self.output_module_218 = self.module_218(self.output_module_216)
        self.output_module_219 = self.module_219(self.output_module_218)
        self.output_module_222 = self.module_222(alpha=1, other=self.output_module_212, input=self.output_module_219)
        self.output_module_223 = self.module_223(self.output_module_222)
        self.output_module_224 = self.module_224(self.output_module_223)
        self.output_module_226 = self.module_226(self.output_module_224)
        self.output_module_227 = self.module_227(self.output_module_226)
        self.output_module_228 = self.module_228(self.output_module_227)
        self.output_module_230 = self.module_230(self.output_module_228)
        self.output_module_231 = self.module_231(self.output_module_230)
        self.output_module_234 = self.module_234(alpha=1, other=self.output_module_223, input=self.output_module_231)
        self.output_module_235 = self.module_235(self.output_module_234)
        self.output_module_236 = self.module_236(self.output_module_235)
        self.output_module_238 = self.module_238(self.output_module_236)
        self.output_module_239 = self.module_239(self.output_module_238)
        self.output_module_241 = self.module_241(self.output_module_239)
        self.output_module_242 = self.module_242(self.output_module_241)
        self.output_module_245 = self.module_245(alpha=1, other=self.output_module_235, input=self.output_module_242)
        self.output_module_246 = self.module_246(self.output_module_245)
        self.output_module_247 = self.module_247(self.output_module_246)
        self.output_module_249 = self.module_249(self.output_module_247)
        self.output_module_250 = self.module_250(self.output_module_246)
        self.output_module_252 = self.module_252(self.output_module_250)
        self.output_module_253 = self.module_253(self.output_module_252)
        self.output_module_255 = self.module_255(self.output_module_253)
        self.output_module_256 = self.module_256(self.output_module_255)
        self.output_module_259 = self.module_259(alpha=1, other=self.output_module_256, input=self.output_module_249)
        self.output_module_260 = self.module_260(self.output_module_259)
        self.output_module_261 = self.module_261(self.output_module_260)
        self.output_module_263 = self.module_263(self.output_module_261)
        self.output_module_264 = self.module_264(self.output_module_263)
        self.output_module_266 = self.module_266(self.output_module_264)
        self.output_module_267 = self.module_267(self.output_module_266)
        self.output_module_270 = self.module_270(alpha=1, other=self.output_module_260, input=self.output_module_267)
        self.output_module_271 = self.module_271(self.output_module_270)
        self.output_module_272 = self.module_272(self.output_module_271)
        self.output_module_274 = self.module_274(self.output_module_272)
        self.output_module_275 = self.module_275(self.output_module_274)
        self.output_module_277 = self.module_277(self.output_module_275)
        self.output_module_278 = self.module_278(self.output_module_277)
        self.output_module_281 = self.module_281(alpha=1, other=self.output_module_271, input=self.output_module_278)
        self.output_module_282 = self.module_282(self.output_module_281)
        self.output_module_283 = self.module_283(self.output_module_282)
        self.output_module_285 = self.module_285(self.output_module_283)
        self.output_module_286 = self.module_286(self.output_module_282)
        self.output_module_288 = self.module_288(self.output_module_286)
        self.output_module_289 = self.module_289(self.output_module_288)
        self.output_module_291 = self.module_291(self.output_module_289)
        self.output_module_292 = self.module_292(self.output_module_291)
        self.output_module_295 = self.module_295(alpha=1, other=self.output_module_292, input=self.output_module_285)
        self.output_module_296 = self.module_296(self.output_module_295)
        self.output_module_297 = self.module_297(self.output_module_296)
        self.output_module_299 = self.module_299(self.output_module_297)
        self.output_module_300 = self.module_300(self.output_module_299)
        self.output_module_302 = self.module_302(self.output_module_300)
        self.output_module_303 = self.module_303(self.output_module_302)
        self.output_module_306 = self.module_306(alpha=1, other=self.output_module_296, input=self.output_module_303)
        self.output_module_307 = self.module_307(self.output_module_306)
        self.output_module_308 = self.module_308(self.output_module_307)
        return self.output_module_308
