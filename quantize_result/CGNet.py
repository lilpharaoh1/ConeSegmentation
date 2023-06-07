# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class CGNet(torch.nn.Module):
    def __init__(self):
        super(CGNet, self).__init__()
        self.module_0 = py_nndct.nn.Input() #CGNet::input_0
        self.module_1 = py_nndct.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=[2, 1], stride=[2, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/Conv2d[stage_0_conv_0]/input.3
        self.module_2 = py_nndct.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=[1, 2], stride=[1, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/Conv2d[stage_0_conv_1]/input.5
        self.module_3 = py_nndct.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/_ConvBNLeakyReLU[stage1_0]/Conv2d[conv]/input.7
        self.module_4 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/_ConvBNLeakyReLU[stage1_0]/LeakyReLU[leakyrelu]/input.11
        self.module_5 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/_ConvBNLeakyReLU[stage1_1]/Conv2d[conv]/input.13
        self.module_6 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/_ConvBNLeakyReLU[stage1_1]/LeakyReLU[leakyrelu]/input.17
        self.module_7 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/_ConvBNLeakyReLU[stage1_2]/Conv2d[conv]/input.19
        self.module_8 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/_ConvBNLeakyReLU[stage1_2]/LeakyReLU[leakyrelu]/13392
        self.module_9 = py_nndct.nn.AvgPool2d(kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], ceil_mode=False, count_include_pad=True) #CGNet::CGNet/_InputInjection[sample1]/AvgPool2d[pool]/ModuleList[0]/13405
        self.module_10 = py_nndct.nn.AvgPool2d(kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], ceil_mode=False, count_include_pad=True) #CGNet::CGNet/_InputInjection[sample2]/AvgPool2d[pool]/ModuleList[0]/13418
        self.module_11 = py_nndct.nn.AvgPool2d(kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], ceil_mode=False, count_include_pad=True) #CGNet::CGNet/_InputInjection[sample2]/AvgPool2d[pool]/ModuleList[1]/13431
        self.module_12 = py_nndct.nn.Cat() #CGNet::CGNet/input.23
        self.module_13 = py_nndct.nn.BatchNorm(num_features=35, eps=0.0, momentum=0.1) #CGNet::CGNet/_BNLeakyReLU[bn_leakyrelu1]/BatchNorm2d[bn]/input.25
        self.module_14 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/_BNLeakyReLU[bn_leakyrelu1]/ReLU[leakyrelu]/input.27
        self.module_15 = py_nndct.nn.Conv2d(in_channels=35, out_channels=64, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_0]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.29
        self.module_16 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage2_0]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.33
        self.module_17 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_0]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.35
        self.module_18 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[2, 2], dilation=[2, 2], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_0]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.39
        self.module_19 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage2_0]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/13513
        self.module_20 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage2_0]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/13519
        self.module_21 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage2_0]/input.43
        self.module_22 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=False) #CGNet::CGNet/ContextGuidedBlock[stage2_0]/Conv2d[reduce]/input.45
        self.module_23 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_0]/_FGlo1[f_glo1]/Conv2d[fc1]/input.47
        self.module_24 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage2_0]/_FGlo1[f_glo1]/ReLU[relu]/input.49
        self.module_25 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_0]/_FGlo1[f_glo1]/Conv2d[fc2]/input.51
        self.module_26 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage2_0]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/input.53
        self.module_27 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_1]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.55
        self.module_28 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage2_1]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.59
        self.module_29 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_1]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.61
        self.module_30 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[2, 2], dilation=[2, 2], groups=32, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_1]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.65
        self.module_31 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage2_1]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/13669
        self.module_32 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage2_1]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/13675
        self.module_33 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage2_1]/input.69
        self.module_34 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_1]/_FGlo1[f_glo1]/Conv2d[fc1]/input.71
        self.module_35 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage2_1]/_FGlo1[f_glo1]/ReLU[relu]/input.73
        self.module_36 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_1]/_FGlo1[f_glo1]/Conv2d[fc2]/input.75
        self.module_37 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage2_1]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/13732
        self.module_38 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage2_1]/input.77
        self.module_39 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_2]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.79
        self.module_40 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage2_2]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.83
        self.module_41 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_2]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.85
        self.module_42 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[2, 2], dilation=[2, 2], groups=32, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_2]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.89
        self.module_43 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage2_2]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/13807
        self.module_44 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage2_2]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/13813
        self.module_45 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage2_2]/input.93
        self.module_46 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_2]/_FGlo1[f_glo1]/Conv2d[fc1]/input.95
        self.module_47 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage2_2]/_FGlo1[f_glo1]/ReLU[relu]/input.97
        self.module_48 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_2]/_FGlo1[f_glo1]/Conv2d[fc2]/input.99
        self.module_49 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage2_2]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/13870
        self.module_50 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage2_2]/input.101
        self.module_51 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_3]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.103
        self.module_52 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage2_3]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.107
        self.module_53 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_3]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.109
        self.module_54 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[2, 2], dilation=[2, 2], groups=32, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_3]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.113
        self.module_55 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage2_3]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/13945
        self.module_56 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage2_3]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/13951
        self.module_57 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage2_3]/input.117
        self.module_58 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_3]/_FGlo1[f_glo1]/Conv2d[fc1]/input.119
        self.module_59 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage2_3]/_FGlo1[f_glo1]/ReLU[relu]/input.121
        self.module_60 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage2_3]/_FGlo1[f_glo1]/Conv2d[fc2]/input.123
        self.module_61 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage2_3]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/14008
        self.module_62 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage2_3]/14010
        self.module_63 = py_nndct.nn.Cat() #CGNet::CGNet/input.125
        self.module_64 = py_nndct.nn.BatchNorm(num_features=131, eps=0.0, momentum=0.1) #CGNet::CGNet/_BNLeakyReLU[bn_leakyrelu2]/BatchNorm2d[bn]/input.127
        self.module_65 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/_BNLeakyReLU[bn_leakyrelu2]/ReLU[leakyrelu]/input.129
        self.module_66 = py_nndct.nn.Conv2d(in_channels=131, out_channels=128, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_0]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.131
        self.module_67 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_0]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.135
        self.module_68 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=128, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_0]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.137
        self.module_69 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=128, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_0]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.141
        self.module_70 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_0]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14092
        self.module_71 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_0]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14098
        self.module_72 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_0]/input.145
        self.module_73 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=False) #CGNet::CGNet/ContextGuidedBlock[stage3_0]/Conv2d[reduce]/input.147
        self.module_74 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_0]/_FGlo1[f_glo1]/Conv2d[fc1]/input.149
        self.module_75 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_0]/_FGlo1[f_glo1]/ReLU[relu]/input.151
        self.module_76 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_0]/_FGlo1[f_glo1]/Conv2d[fc2]/input.153
        self.module_77 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_0]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/input.155
        self.module_78 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_1]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.157
        self.module_79 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_1]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.161
        self.module_80 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_1]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.163
        self.module_81 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_1]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.167
        self.module_82 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_1]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14248
        self.module_83 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_1]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14254
        self.module_84 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_1]/input.171
        self.module_85 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_1]/_FGlo1[f_glo1]/Conv2d[fc1]/input.173
        self.module_86 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_1]/_FGlo1[f_glo1]/ReLU[relu]/input.175
        self.module_87 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_1]/_FGlo1[f_glo1]/Conv2d[fc2]/input.177
        self.module_88 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_1]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/14311
        self.module_89 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_1]/input.179
        self.module_90 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_2]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.181
        self.module_91 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_2]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.185
        self.module_92 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_2]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.187
        self.module_93 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_2]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.191
        self.module_94 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_2]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14386
        self.module_95 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_2]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14392
        self.module_96 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_2]/input.195
        self.module_97 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_2]/_FGlo1[f_glo1]/Conv2d[fc1]/input.197
        self.module_98 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_2]/_FGlo1[f_glo1]/ReLU[relu]/input.199
        self.module_99 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_2]/_FGlo1[f_glo1]/Conv2d[fc2]/input.201
        self.module_100 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_2]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/14449
        self.module_101 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_2]/input.203
        self.module_102 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_3]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.205
        self.module_103 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_3]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.209
        self.module_104 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_3]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.211
        self.module_105 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_3]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.215
        self.module_106 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_3]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14524
        self.module_107 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_3]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14530
        self.module_108 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_3]/input.219
        self.module_109 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_3]/_FGlo1[f_glo1]/Conv2d[fc1]/input.221
        self.module_110 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_3]/_FGlo1[f_glo1]/ReLU[relu]/input.223
        self.module_111 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_3]/_FGlo1[f_glo1]/Conv2d[fc2]/input.225
        self.module_112 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_3]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/14587
        self.module_113 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_3]/input.227
        self.module_114 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_4]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.229
        self.module_115 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_4]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.233
        self.module_116 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_4]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.235
        self.module_117 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_4]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.239
        self.module_118 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_4]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14662
        self.module_119 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_4]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14668
        self.module_120 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_4]/input.243
        self.module_121 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_4]/_FGlo1[f_glo1]/Conv2d[fc1]/input.245
        self.module_122 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_4]/_FGlo1[f_glo1]/ReLU[relu]/input.247
        self.module_123 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_4]/_FGlo1[f_glo1]/Conv2d[fc2]/input.249
        self.module_124 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_4]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/14725
        self.module_125 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_4]/input.251
        self.module_126 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_5]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.253
        self.module_127 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_5]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.257
        self.module_128 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_5]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.259
        self.module_129 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_5]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.263
        self.module_130 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_5]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14800
        self.module_131 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_5]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14806
        self.module_132 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_5]/input.267
        self.module_133 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_5]/_FGlo1[f_glo1]/Conv2d[fc1]/input.269
        self.module_134 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_5]/_FGlo1[f_glo1]/ReLU[relu]/input.271
        self.module_135 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_5]/_FGlo1[f_glo1]/Conv2d[fc2]/input.273
        self.module_136 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_5]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/14863
        self.module_137 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_5]/input.275
        self.module_138 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_6]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.277
        self.module_139 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_6]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.281
        self.module_140 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_6]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.283
        self.module_141 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_6]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.287
        self.module_142 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_6]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14938
        self.module_143 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_6]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/14944
        self.module_144 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_6]/input.291
        self.module_145 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_6]/_FGlo1[f_glo1]/Conv2d[fc1]/input.293
        self.module_146 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_6]/_FGlo1[f_glo1]/ReLU[relu]/input.295
        self.module_147 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_6]/_FGlo1[f_glo1]/Conv2d[fc2]/input.297
        self.module_148 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_6]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/15001
        self.module_149 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_6]/input.299
        self.module_150 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_7]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.301
        self.module_151 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_7]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.305
        self.module_152 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_7]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.307
        self.module_153 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_7]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.311
        self.module_154 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_7]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15076
        self.module_155 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_7]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15082
        self.module_156 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_7]/input.315
        self.module_157 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_7]/_FGlo1[f_glo1]/Conv2d[fc1]/input.317
        self.module_158 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_7]/_FGlo1[f_glo1]/ReLU[relu]/input.319
        self.module_159 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_7]/_FGlo1[f_glo1]/Conv2d[fc2]/input.321
        self.module_160 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_7]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/15139
        self.module_161 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_7]/input.323
        self.module_162 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_8]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.325
        self.module_163 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_8]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.329
        self.module_164 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_8]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.331
        self.module_165 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_8]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.335
        self.module_166 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_8]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15214
        self.module_167 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_8]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15220
        self.module_168 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_8]/input.339
        self.module_169 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_8]/_FGlo1[f_glo1]/Conv2d[fc1]/input.341
        self.module_170 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_8]/_FGlo1[f_glo1]/ReLU[relu]/input.343
        self.module_171 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_8]/_FGlo1[f_glo1]/Conv2d[fc2]/input.345
        self.module_172 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_8]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/15277
        self.module_173 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_8]/input.347
        self.module_174 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_9]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.349
        self.module_175 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_9]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.353
        self.module_176 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_9]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.355
        self.module_177 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_9]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.359
        self.module_178 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_9]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15352
        self.module_179 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_9]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15358
        self.module_180 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_9]/input.363
        self.module_181 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_9]/_FGlo1[f_glo1]/Conv2d[fc1]/input.365
        self.module_182 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_9]/_FGlo1[f_glo1]/ReLU[relu]/input.367
        self.module_183 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_9]/_FGlo1[f_glo1]/Conv2d[fc2]/input.369
        self.module_184 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_9]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/15415
        self.module_185 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_9]/input.371
        self.module_186 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_10]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.373
        self.module_187 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_10]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.377
        self.module_188 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_10]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.379
        self.module_189 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_10]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.383
        self.module_190 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_10]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15490
        self.module_191 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_10]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15496
        self.module_192 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_10]/input.387
        self.module_193 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_10]/_FGlo1[f_glo1]/Conv2d[fc1]/input.389
        self.module_194 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_10]/_FGlo1[f_glo1]/ReLU[relu]/input.391
        self.module_195 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_10]/_FGlo1[f_glo1]/Conv2d[fc2]/input.393
        self.module_196 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_10]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/15553
        self.module_197 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_10]/input.395
        self.module_198 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_11]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.397
        self.module_199 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_11]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.401
        self.module_200 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_11]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.403
        self.module_201 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_11]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.407
        self.module_202 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_11]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15628
        self.module_203 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_11]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15634
        self.module_204 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_11]/input.411
        self.module_205 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_11]/_FGlo1[f_glo1]/Conv2d[fc1]/input.413
        self.module_206 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_11]/_FGlo1[f_glo1]/ReLU[relu]/input.415
        self.module_207 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_11]/_FGlo1[f_glo1]/Conv2d[fc2]/input.417
        self.module_208 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_11]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/15691
        self.module_209 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_11]/input.419
        self.module_210 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_12]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.421
        self.module_211 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_12]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.425
        self.module_212 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_12]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.427
        self.module_213 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_12]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.431
        self.module_214 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_12]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15766
        self.module_215 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_12]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15772
        self.module_216 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_12]/input.435
        self.module_217 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_12]/_FGlo1[f_glo1]/Conv2d[fc1]/input.437
        self.module_218 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_12]/_FGlo1[f_glo1]/ReLU[relu]/input.439
        self.module_219 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_12]/_FGlo1[f_glo1]/Conv2d[fc2]/input.441
        self.module_220 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_12]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/15829
        self.module_221 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_12]/input.443
        self.module_222 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_13]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.445
        self.module_223 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_13]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.449
        self.module_224 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_13]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.451
        self.module_225 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_13]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.455
        self.module_226 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_13]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15904
        self.module_227 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_13]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/15910
        self.module_228 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_13]/input.459
        self.module_229 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_13]/_FGlo1[f_glo1]/Conv2d[fc1]/input.461
        self.module_230 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_13]/_FGlo1[f_glo1]/ReLU[relu]/input.463
        self.module_231 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_13]/_FGlo1[f_glo1]/Conv2d[fc2]/input.465
        self.module_232 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_13]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/15967
        self.module_233 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_13]/input.467
        self.module_234 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_14]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.469
        self.module_235 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_14]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.473
        self.module_236 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_14]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.475
        self.module_237 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_14]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.479
        self.module_238 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_14]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/16042
        self.module_239 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_14]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/16048
        self.module_240 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_14]/input.483
        self.module_241 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_14]/_FGlo1[f_glo1]/Conv2d[fc1]/input.485
        self.module_242 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_14]/_FGlo1[f_glo1]/ReLU[relu]/input.487
        self.module_243 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_14]/_FGlo1[f_glo1]/Conv2d[fc2]/input.489
        self.module_244 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_14]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/16105
        self.module_245 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_14]/input.491
        self.module_246 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_15]/_ConvBNLeakyReLU[conv]/Conv2d[conv]/input.493
        self.module_247 = py_nndct.nn.LeakyReLU(negative_slope=0.1, inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_15]/_ConvBNLeakyReLU[conv]/LeakyReLU[leakyrelu]/input.497
        self.module_248 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_15]/_ChannelWiseConv[f_loc]/Conv2d[conv]/input.499
        self.module_249 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[4, 4], dilation=[4, 4], groups=64, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_15]/_ChannelWiseConv[f_sur]/Conv2d[conv]/input.503
        self.module_250 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_15]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/16180
        self.module_251 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_15]/_BNLeakyReLU[reduction_bnlr]/ReLU[leakyrelu]/16186
        self.module_252 = py_nndct.nn.Cat() #CGNet::CGNet/ContextGuidedBlock[stage3_15]/input.507
        self.module_253 = py_nndct.nn.Conv2d(in_channels=128, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_15]/_FGlo1[f_glo1]/Conv2d[fc1]/input.509
        self.module_254 = py_nndct.nn.ReLU(inplace=True) #CGNet::CGNet/ContextGuidedBlock[stage3_15]/_FGlo1[f_glo1]/ReLU[relu]/input.511
        self.module_255 = py_nndct.nn.Conv2d(in_channels=8, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/ContextGuidedBlock[stage3_15]/_FGlo1[f_glo1]/Conv2d[fc2]/input.513
        self.module_256 = py_nndct.nn.Module('relu6',inplace=False) #CGNet::CGNet/ContextGuidedBlock[stage3_15]/_FGlo1[f_glo1]/Hardtanh[hardtanh]/16243
        self.module_257 = py_nndct.nn.Add() #CGNet::CGNet/ContextGuidedBlock[stage3_15]/16245
        self.module_258 = py_nndct.nn.Cat() #CGNet::CGNet/input.515
        self.module_259 = py_nndct.nn.Conv2d(in_channels=256, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #CGNet::CGNet/Sequential[head]/Conv2d[1]/16270

    def forward(self, *args):
        output_module_0 = self.module_0(input=args[0])
        output_module_0 = self.module_1(output_module_0)
        output_module_0 = self.module_2(output_module_0)
        output_module_3 = self.module_3(output_module_0)
        output_module_3 = self.module_4(output_module_3)
        output_module_3 = self.module_5(output_module_3)
        output_module_3 = self.module_6(output_module_3)
        output_module_3 = self.module_7(output_module_3)
        output_module_3 = self.module_8(output_module_3)
        output_module_9 = self.module_9(output_module_0)
        output_module_10 = self.module_10(output_module_0)
        output_module_10 = self.module_11(output_module_10)
        output_module_3 = self.module_12(dim=1, tensors=[output_module_3,output_module_9])
        output_module_3 = self.module_13(output_module_3)
        output_module_3 = self.module_14(output_module_3)
        output_module_3 = self.module_15(output_module_3)
        output_module_3 = self.module_16(output_module_3)
        output_module_17 = self.module_17(output_module_3)
        output_module_18 = self.module_18(output_module_3)
        output_module_17 = self.module_19(output_module_17)
        output_module_18 = self.module_20(output_module_18)
        output_module_17 = self.module_21(dim=1, tensors=[output_module_17,output_module_18])
        output_module_17 = self.module_22(output_module_17)
        output_module_17 = self.module_23(output_module_17)
        output_module_17 = self.module_24(output_module_17)
        output_module_17 = self.module_25(output_module_17)
        output_module_17 = self.module_26(output_module_17)
        output_module_27 = self.module_27(output_module_17)
        output_module_27 = self.module_28(output_module_27)
        output_module_29 = self.module_29(output_module_27)
        output_module_30 = self.module_30(output_module_27)
        output_module_29 = self.module_31(output_module_29)
        output_module_30 = self.module_32(output_module_30)
        output_module_29 = self.module_33(dim=1, tensors=[output_module_29,output_module_30])
        output_module_29 = self.module_34(output_module_29)
        output_module_29 = self.module_35(output_module_29)
        output_module_29 = self.module_36(output_module_29)
        output_module_29 = self.module_37(output_module_29)
        output_module_29 = self.module_38(input=output_module_29, other=output_module_17, alpha=1)
        output_module_39 = self.module_39(output_module_29)
        output_module_39 = self.module_40(output_module_39)
        output_module_41 = self.module_41(output_module_39)
        output_module_42 = self.module_42(output_module_39)
        output_module_41 = self.module_43(output_module_41)
        output_module_42 = self.module_44(output_module_42)
        output_module_41 = self.module_45(dim=1, tensors=[output_module_41,output_module_42])
        output_module_41 = self.module_46(output_module_41)
        output_module_41 = self.module_47(output_module_41)
        output_module_41 = self.module_48(output_module_41)
        output_module_41 = self.module_49(output_module_41)
        output_module_41 = self.module_50(input=output_module_41, other=output_module_29, alpha=1)
        output_module_51 = self.module_51(output_module_41)
        output_module_51 = self.module_52(output_module_51)
        output_module_53 = self.module_53(output_module_51)
        output_module_54 = self.module_54(output_module_51)
        output_module_53 = self.module_55(output_module_53)
        output_module_54 = self.module_56(output_module_54)
        output_module_53 = self.module_57(dim=1, tensors=[output_module_53,output_module_54])
        output_module_53 = self.module_58(output_module_53)
        output_module_53 = self.module_59(output_module_53)
        output_module_53 = self.module_60(output_module_53)
        output_module_53 = self.module_61(output_module_53)
        output_module_53 = self.module_62(input=output_module_53, other=output_module_41, alpha=1)
        output_module_53 = self.module_63(dim=1, tensors=[output_module_53,output_module_17,output_module_10])
        output_module_53 = self.module_64(output_module_53)
        output_module_53 = self.module_65(output_module_53)
        output_module_53 = self.module_66(output_module_53)
        output_module_53 = self.module_67(output_module_53)
        output_module_68 = self.module_68(output_module_53)
        output_module_69 = self.module_69(output_module_53)
        output_module_68 = self.module_70(output_module_68)
        output_module_69 = self.module_71(output_module_69)
        output_module_68 = self.module_72(dim=1, tensors=[output_module_68,output_module_69])
        output_module_68 = self.module_73(output_module_68)
        output_module_68 = self.module_74(output_module_68)
        output_module_68 = self.module_75(output_module_68)
        output_module_68 = self.module_76(output_module_68)
        output_module_68 = self.module_77(output_module_68)
        output_module_78 = self.module_78(output_module_68)
        output_module_78 = self.module_79(output_module_78)
        output_module_80 = self.module_80(output_module_78)
        output_module_81 = self.module_81(output_module_78)
        output_module_80 = self.module_82(output_module_80)
        output_module_81 = self.module_83(output_module_81)
        output_module_80 = self.module_84(dim=1, tensors=[output_module_80,output_module_81])
        output_module_80 = self.module_85(output_module_80)
        output_module_80 = self.module_86(output_module_80)
        output_module_80 = self.module_87(output_module_80)
        output_module_80 = self.module_88(output_module_80)
        output_module_80 = self.module_89(input=output_module_80, other=output_module_68, alpha=1)
        output_module_90 = self.module_90(output_module_80)
        output_module_90 = self.module_91(output_module_90)
        output_module_92 = self.module_92(output_module_90)
        output_module_93 = self.module_93(output_module_90)
        output_module_92 = self.module_94(output_module_92)
        output_module_93 = self.module_95(output_module_93)
        output_module_92 = self.module_96(dim=1, tensors=[output_module_92,output_module_93])
        output_module_92 = self.module_97(output_module_92)
        output_module_92 = self.module_98(output_module_92)
        output_module_92 = self.module_99(output_module_92)
        output_module_92 = self.module_100(output_module_92)
        output_module_92 = self.module_101(input=output_module_92, other=output_module_80, alpha=1)
        output_module_102 = self.module_102(output_module_92)
        output_module_102 = self.module_103(output_module_102)
        output_module_104 = self.module_104(output_module_102)
        output_module_105 = self.module_105(output_module_102)
        output_module_104 = self.module_106(output_module_104)
        output_module_105 = self.module_107(output_module_105)
        output_module_104 = self.module_108(dim=1, tensors=[output_module_104,output_module_105])
        output_module_104 = self.module_109(output_module_104)
        output_module_104 = self.module_110(output_module_104)
        output_module_104 = self.module_111(output_module_104)
        output_module_104 = self.module_112(output_module_104)
        output_module_104 = self.module_113(input=output_module_104, other=output_module_92, alpha=1)
        output_module_114 = self.module_114(output_module_104)
        output_module_114 = self.module_115(output_module_114)
        output_module_116 = self.module_116(output_module_114)
        output_module_117 = self.module_117(output_module_114)
        output_module_116 = self.module_118(output_module_116)
        output_module_117 = self.module_119(output_module_117)
        output_module_116 = self.module_120(dim=1, tensors=[output_module_116,output_module_117])
        output_module_116 = self.module_121(output_module_116)
        output_module_116 = self.module_122(output_module_116)
        output_module_116 = self.module_123(output_module_116)
        output_module_116 = self.module_124(output_module_116)
        output_module_116 = self.module_125(input=output_module_116, other=output_module_104, alpha=1)
        output_module_126 = self.module_126(output_module_116)
        output_module_126 = self.module_127(output_module_126)
        output_module_128 = self.module_128(output_module_126)
        output_module_129 = self.module_129(output_module_126)
        output_module_128 = self.module_130(output_module_128)
        output_module_129 = self.module_131(output_module_129)
        output_module_128 = self.module_132(dim=1, tensors=[output_module_128,output_module_129])
        output_module_128 = self.module_133(output_module_128)
        output_module_128 = self.module_134(output_module_128)
        output_module_128 = self.module_135(output_module_128)
        output_module_128 = self.module_136(output_module_128)
        output_module_128 = self.module_137(input=output_module_128, other=output_module_116, alpha=1)
        output_module_138 = self.module_138(output_module_128)
        output_module_138 = self.module_139(output_module_138)
        output_module_140 = self.module_140(output_module_138)
        output_module_141 = self.module_141(output_module_138)
        output_module_140 = self.module_142(output_module_140)
        output_module_141 = self.module_143(output_module_141)
        output_module_140 = self.module_144(dim=1, tensors=[output_module_140,output_module_141])
        output_module_140 = self.module_145(output_module_140)
        output_module_140 = self.module_146(output_module_140)
        output_module_140 = self.module_147(output_module_140)
        output_module_140 = self.module_148(output_module_140)
        output_module_140 = self.module_149(input=output_module_140, other=output_module_128, alpha=1)
        output_module_150 = self.module_150(output_module_140)
        output_module_150 = self.module_151(output_module_150)
        output_module_152 = self.module_152(output_module_150)
        output_module_153 = self.module_153(output_module_150)
        output_module_152 = self.module_154(output_module_152)
        output_module_153 = self.module_155(output_module_153)
        output_module_152 = self.module_156(dim=1, tensors=[output_module_152,output_module_153])
        output_module_152 = self.module_157(output_module_152)
        output_module_152 = self.module_158(output_module_152)
        output_module_152 = self.module_159(output_module_152)
        output_module_152 = self.module_160(output_module_152)
        output_module_152 = self.module_161(input=output_module_152, other=output_module_140, alpha=1)
        output_module_162 = self.module_162(output_module_152)
        output_module_162 = self.module_163(output_module_162)
        output_module_164 = self.module_164(output_module_162)
        output_module_165 = self.module_165(output_module_162)
        output_module_164 = self.module_166(output_module_164)
        output_module_165 = self.module_167(output_module_165)
        output_module_164 = self.module_168(dim=1, tensors=[output_module_164,output_module_165])
        output_module_164 = self.module_169(output_module_164)
        output_module_164 = self.module_170(output_module_164)
        output_module_164 = self.module_171(output_module_164)
        output_module_164 = self.module_172(output_module_164)
        output_module_164 = self.module_173(input=output_module_164, other=output_module_152, alpha=1)
        output_module_174 = self.module_174(output_module_164)
        output_module_174 = self.module_175(output_module_174)
        output_module_176 = self.module_176(output_module_174)
        output_module_177 = self.module_177(output_module_174)
        output_module_176 = self.module_178(output_module_176)
        output_module_177 = self.module_179(output_module_177)
        output_module_176 = self.module_180(dim=1, tensors=[output_module_176,output_module_177])
        output_module_176 = self.module_181(output_module_176)
        output_module_176 = self.module_182(output_module_176)
        output_module_176 = self.module_183(output_module_176)
        output_module_176 = self.module_184(output_module_176)
        output_module_176 = self.module_185(input=output_module_176, other=output_module_164, alpha=1)
        output_module_186 = self.module_186(output_module_176)
        output_module_186 = self.module_187(output_module_186)
        output_module_188 = self.module_188(output_module_186)
        output_module_189 = self.module_189(output_module_186)
        output_module_188 = self.module_190(output_module_188)
        output_module_189 = self.module_191(output_module_189)
        output_module_188 = self.module_192(dim=1, tensors=[output_module_188,output_module_189])
        output_module_188 = self.module_193(output_module_188)
        output_module_188 = self.module_194(output_module_188)
        output_module_188 = self.module_195(output_module_188)
        output_module_188 = self.module_196(output_module_188)
        output_module_188 = self.module_197(input=output_module_188, other=output_module_176, alpha=1)
        output_module_198 = self.module_198(output_module_188)
        output_module_198 = self.module_199(output_module_198)
        output_module_200 = self.module_200(output_module_198)
        output_module_201 = self.module_201(output_module_198)
        output_module_200 = self.module_202(output_module_200)
        output_module_201 = self.module_203(output_module_201)
        output_module_200 = self.module_204(dim=1, tensors=[output_module_200,output_module_201])
        output_module_200 = self.module_205(output_module_200)
        output_module_200 = self.module_206(output_module_200)
        output_module_200 = self.module_207(output_module_200)
        output_module_200 = self.module_208(output_module_200)
        output_module_200 = self.module_209(input=output_module_200, other=output_module_188, alpha=1)
        output_module_210 = self.module_210(output_module_200)
        output_module_210 = self.module_211(output_module_210)
        output_module_212 = self.module_212(output_module_210)
        output_module_213 = self.module_213(output_module_210)
        output_module_212 = self.module_214(output_module_212)
        output_module_213 = self.module_215(output_module_213)
        output_module_212 = self.module_216(dim=1, tensors=[output_module_212,output_module_213])
        output_module_212 = self.module_217(output_module_212)
        output_module_212 = self.module_218(output_module_212)
        output_module_212 = self.module_219(output_module_212)
        output_module_212 = self.module_220(output_module_212)
        output_module_212 = self.module_221(input=output_module_212, other=output_module_200, alpha=1)
        output_module_222 = self.module_222(output_module_212)
        output_module_222 = self.module_223(output_module_222)
        output_module_224 = self.module_224(output_module_222)
        output_module_225 = self.module_225(output_module_222)
        output_module_224 = self.module_226(output_module_224)
        output_module_225 = self.module_227(output_module_225)
        output_module_224 = self.module_228(dim=1, tensors=[output_module_224,output_module_225])
        output_module_224 = self.module_229(output_module_224)
        output_module_224 = self.module_230(output_module_224)
        output_module_224 = self.module_231(output_module_224)
        output_module_224 = self.module_232(output_module_224)
        output_module_224 = self.module_233(input=output_module_224, other=output_module_212, alpha=1)
        output_module_234 = self.module_234(output_module_224)
        output_module_234 = self.module_235(output_module_234)
        output_module_236 = self.module_236(output_module_234)
        output_module_237 = self.module_237(output_module_234)
        output_module_236 = self.module_238(output_module_236)
        output_module_237 = self.module_239(output_module_237)
        output_module_236 = self.module_240(dim=1, tensors=[output_module_236,output_module_237])
        output_module_236 = self.module_241(output_module_236)
        output_module_236 = self.module_242(output_module_236)
        output_module_236 = self.module_243(output_module_236)
        output_module_236 = self.module_244(output_module_236)
        output_module_236 = self.module_245(input=output_module_236, other=output_module_224, alpha=1)
        output_module_246 = self.module_246(output_module_236)
        output_module_246 = self.module_247(output_module_246)
        output_module_248 = self.module_248(output_module_246)
        output_module_249 = self.module_249(output_module_246)
        output_module_248 = self.module_250(output_module_248)
        output_module_249 = self.module_251(output_module_249)
        output_module_248 = self.module_252(dim=1, tensors=[output_module_248,output_module_249])
        output_module_248 = self.module_253(output_module_248)
        output_module_248 = self.module_254(output_module_248)
        output_module_248 = self.module_255(output_module_248)
        output_module_248 = self.module_256(output_module_248)
        output_module_248 = self.module_257(input=output_module_248, other=output_module_236, alpha=1)
        output_module_258 = self.module_258(dim=1, tensors=[output_module_68,output_module_248])
        output_module_258 = self.module_259(output_module_258)
        return output_module_258
