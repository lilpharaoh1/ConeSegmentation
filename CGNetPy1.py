import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
# import torchvision

class ContextGuidedBlock(nn.Module):
    def __init__(self, in_channels, out_channels, dilation=2, reduction=16, down=False,
                residual=True, stage2=False, norm_layer=nn.BatchNorm2d, **kwargs):
        super(ContextGuidedBlock, self).__init__()
        # inter_channels = out_channels // 2
        inter_channels = out_channels // 2 if not down else out_channels
        if down:
            self.conv = _ConvBNLeakyReLU(in_channels, inter_channels, 3, 2, 1, groups=1, norm_layer=norm_layer,  **kwargs)
            # self.reduce = nn.Conv2d(inter_channels * 2, out_channels, 1, bias=False)
        else:
            self.conv = _ConvBNLeakyReLU(in_channels, inter_channels, 1, 1, 0, groups=1, norm_layer=norm_layer, **kwargs)
            # self.reduce = nn.Identity()
        reduce_in_channels = inter_channels * 2
        self.reduce = nn.Conv2d(reduce_in_channels, out_channels, 1, groups=1, bias=False)
        # self.reduce = _ConvBNLeakyReLU(reduce_in_channels, out_channels, 1, groups=1, **kwargs)
        self.f_loc = _ChannelWiseConv(inter_channels, inter_channels, **kwargs)
        self.f_sur = _ChannelWiseConv(inter_channels, inter_channels, dilation, **kwargs)
        self.bnleakyrelu = _BNLeakyReLU(inter_channels * 2)
        self.leakyrelu = nn.LeakyReLU(0.1)
        self.relu = nn.ReLU(True)

        self.reduction_bnlr = _BNLeakyReLU(inter_channels)
        if out_channels == 128:
            image_size = (136, 182)
        else: 
            image_size = (68, 91)
        self.f_glo1 = _FGlo1(out_channels, reduction=reduction, **kwargs)
        self.down = down
        self.residual = residual

        self.gap = nn.AdaptiveAvgPool2d(1)
        self.postreduce = nn.Conv2d(out_channels, out_channels, 1, groups=1, bias=False)

    def forward(self, x):
        out = self.conv(x)
        loc = self.f_loc(out)
        sur = self.f_sur(out)
        loc = self.reduction_bnlr(loc)
        sur = self.reduction_bnlr(sur)

        joi_feat = torch.cat([loc, sur], dim=1)
        # joi_feat = 

        if self.down:
            joi_feat = self.reduce(joi_feat)

        out = self.f_glo1(joi_feat)
        if self.residual:
            out = out + x
    
        return out

class _ConcatInjection(nn.Module):
    def __init__(self, in_channels, norm_layer=nn.BatchNorm2d, **kwargs):
        super(_ConcatInjection, self).__init__()
        self.bn = norm_layer(in_channels)
        self.leakyrelu = nn.LeakyReLU(0.1)#in_channels)

    def forward(self, x1, x2):
        out = torch.cat([x1, x2], dim=1)
        out = self.bn(out)
        out = self.leakyrelu(out)
        return out

class _InputInjection(nn.Module):
    def __init__(self, ratio):
        super(_InputInjection, self).__init__()
        self.pool = nn.ModuleList()
        for i in range(0, ratio):
            self.pool.append(nn.AvgPool2d(3, 2, 1))

    def forward(self, x):
        for pool in self.pool:
            x = pool(x)
        return x

class _FGlo1(nn.Module):
    def __init__(self, in_channels, reduction=16, **kwargs):
        super(_FGlo1, self).__init__()
        self.gap = nn.AvgPool2d(kernel_size=(4,1), stride=(4, 1), padding=0)
        self.gap_after = nn.AvgPool2d(kernel_size=(4, 1), stride=(4, 1), padding=0)
        self.avgap = nn.AdaptiveAvgPool2d(1)
        mid_channels = in_channels // reduction
        self.fc1 = nn.Conv2d(in_channels, mid_channels, kernel_size=(1, 1), stride=1, groups=1)# bias=True)
        self.relu = nn.ReLU(True)
        self.fc2 = nn.Conv2d(mid_channels, in_channels, kernel_size=(1, 1), stride=1, groups=1)#, bias=True)
        self.hardtanh = nn.Hardtanh(min_val=0, max_val=6)#nn.Hardsigmoid()
        self.divisor = torch.tensor([[[0.1667]]], dtype=torch.float)

    def forward(self, x):
        n, c, _, _ = x.size()
        out = x
        # out = self.avgap(out)
        # out = self.rand
        # out = out.view(n, c)
        out = self.fc1(out)
        out = self.relu(out)
        out = self.fc2(out)
        # print(out.shape)
        out = self.hardtanh(out)#.view(n, c, 1, 1)
        # out = F.conv2d(out, self.divisor)
        # print(out)
        # out = torch.mul(out)#0.1667)
        # print(out.shape)
        # out = x * out
        return out
        # return x

class _ChannelWiseConv(nn.Module):
    def __init__(self, in_channels, out_channels, dilation=1, **kwargs):
        super(_ChannelWiseConv, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, 3, 1, dilation, dilation, groups=in_channels, bias=False)

    def forward(self, x):
        x = self.conv(x)
        return x

class _ConvBNLeakyReLU(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0,
                 dilation=1, groups=1, norm_layer=nn.BatchNorm2d, bit_width=3, **kwargs):
        super(_ConvBNLeakyReLU, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias=False)
        self.bn = norm_layer(out_channels)
        self.leakyrelu = nn.LeakyReLU(0.1)#out_channels)

    def forward(self, x):
        x = self.conv(x)
        # x = self.bn(x)
        # x = self.leakyrelu(x)
        return x

class _ChannelWiseConv(nn.Module):
    def __init__(self, in_channels, out_channels, dilation=1, **kwargs):
        super(_ChannelWiseConv, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, 3, 1, dilation, dilation, groups=in_channels, bias=False)

    def forward(self, x):
        x = self.conv(x)
        return x

class _ConvBNLeakyReLU(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0,
                 dilation=1, groups=1, norm_layer=nn.BatchNorm2d, bit_width=3, **kwargs):
        super(_ConvBNLeakyReLU, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias=False)
        self.bn = norm_layer(out_channels)
        self.leakyrelu = nn.LeakyReLU(0.1)#out_channels)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.leakyrelu(x)
        return x

class _BNLeakyReLU(nn.Module):
    def __init__(self, out_channels, norm_layer=nn.BatchNorm2d, **kwargs):
        super(_BNLeakyReLU, self).__init__()
        self.bn = norm_layer(out_channels)
        self.leakyrelu = nn.ReLU(True)#nn.LeakyReLU(0.1)#out_channels)

    def forward(self, x):
        x = self.bn(x)
        x = self.leakyrelu(x) # TODO : FIX THIS
        # x = nn.functional.leaky_relu(x, 0.1)
        return x

class CGNet(nn.Module):
    r"""CGNet
    Parameters
    ----------
    nclass : int
        Number of categories for the training dataset.
    norm_layer : object
        Normalization layer used in backbone network (default: :class:`nn.BatchNorm`;
        for Synchronized Cross-GPU BachNormalization).
    aux : bool
        Auxiliary loss.
    Reference:
        Tianyi Wu, et al. "CGNet: A Light-weight Context Guided Network for Semantic Segmentation."
        arXiv preprint arXiv:1811.08201 (2018).
    """

    def __init__(self, nclass=1, dropout_rate=0.2, backbone='', aux=False, jpu=False, pretrained_base=True, M=3, N=21, **kwargs):
        super(CGNet, self).__init__()
        #stage 0 
        self.stage0_0 = nn.AvgPool2d(kernel_size=(2,2), stride=2, padding=0)
        self.stage0_1 = nn.MaxPool2d(kernel_size=(2,2), stride=2, padding=0)

        self.stage_0_conv_0 = nn.Conv2d(3, 3, kernel_size=(2, 1), stride=(2, 1), padding=0)
        self.stage_0_conv_1 = nn.Conv2d(3, 3, kernel_size=(1, 2), stride=(1, 2), padding=0)

        # stage 1
        self.stage1_0 = _ConvBNLeakyReLU(3, 32, 3, 2, 1, **kwargs)
        self.stage1_1 = _ConvBNLeakyReLU(32, 32, 3, 1, 1, **kwargs)
        self.stage1_2 = _ConvBNLeakyReLU(32, 32, 3, 1, 1, **kwargs)

        self.sample1 = _InputInjection(1)
        self.sample2 = _InputInjection(2)
        self.bn_leakyrelu1 = _BNLeakyReLU(32 + 3, **kwargs)

        # stage 2
        self.stage2_0 = ContextGuidedBlock(32 + 3, 64, dilation=2, reduction=8, down=True, residual=False, stage2=True, **kwargs)
        self.stage2_1 = ContextGuidedBlock(64, 64, dilation=2, reduction=8, **kwargs)
        self.stage2_2 = ContextGuidedBlock(64, 64, dilation=2, reduction=8, **kwargs)
        self.stage2_3 = ContextGuidedBlock(64, 64, dilation=2, reduction=8, **kwargs)
        #self.stage2 = nn.ModuleList()
        #for i in range(0, M - 1):
        #    self.stage2.append(ContextGuidedBlock(64, 64, dilation=2, reduction=8, **kwargs))
        self.bn_leakyrelu2 = _BNLeakyReLU(128 + 3, **kwargs)

        # stage 3
        self.stage3_0 = ContextGuidedBlock(128 + 3, 128, dilation=4, reduction=16, down=True, residual=False, **kwargs)
        self.stage3_1 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_2 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_3 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_4 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_5 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_6 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_7 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_8 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_9 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_10 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_11 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_12 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_13 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_14 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        self.stage3_15 = ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs)
        #self.stage3 = nn.ModuleList()
        #for i in range(0, N - 1):
        #    self.stage3.append(ContextGuidedBlock(128, 128, dilation=4, reduction=16, **kwargs))
        self.bn_leakyrelu3 = _BNLeakyReLU(256, **kwargs)

        self.head = nn.Sequential(
            nn.Dropout2d(dropout_rate, False),
            nn.Conv2d(256, nclass, 1))

        self.__setattr__('exclusive', ['stage1_0', 'stage1_1', 'stage1_2', 'sample1', 'sample2',
                                       'bn_leakyrelu1', 'stage2_0', 'stage2', 'bn_leakyrelu2', 'stage3_0',
                                       'stage3', 'bn_leakyrelu3', 'head'])

        #print("CGNet initialised")

    def forward(self, x):
        # stage0
        size = x.size()[2:]
        #print(x.shape)
        # x = self.stage0_0(x)
        # x = self.stage0_1(x)
        x = self.stage_0_conv_0(x)
        x = self.stage_0_conv_1(x)
        #print(x.shape)        
        # stage1
        out0 = self.stage1_0(x)
        out0 = self.stage1_1(out0)
        out0 = self.stage1_2(out0)
                
        inp1 = self.sample1(x)
        inp2 = self.sample2(x)

        # stage 2
        out0_cat = self.bn_leakyrelu1(torch.cat([out0, inp1], dim=1))
        out1_0 = self.stage2_0(out0_cat)
        out1 = out1_0
        out1 = self.stage2_1(out1)
        out1 = self.stage2_2(out1)
        out1 = self.stage2_3(out1)
        # out1 = self.stage2(out1)
        # #for layer in self.stage2:
        #     #out1 = layer(out1)
        #     #break
        out1_cat = self.bn_leakyrelu2(torch.cat([out1, out1_0, inp2], dim=1))

        # # stage 3
        out2_0 = self.stage3_0(out1_cat)
        out2 = out2_0
        out2 = self.stage3_1(out2)
        out2 = self.stage3_2(out2)
        out2 = self.stage3_3(out2)
        out2 = self.stage3_4(out2)
        out2 = self.stage3_5(out2)
        out2 = self.stage3_6(out2)
        out2 = self.stage3_7(out2)
        out2 = self.stage3_8(out2)
        out2 = self.stage3_9(out2)
        out2 = self.stage3_10(out2)
        out2 = self.stage3_11(out2)
        out2 = self.stage3_12(out2)
        out2 = self.stage3_13(out2)
        out2 = self.stage3_14(out2)
        out2 = self.stage3_15(out2)
        # # for layer in self.stage3:
        # #   out2 = layer(out2)
        out2_cat = self.bn_leakyrelu3(torch.cat([out2_0, out2], dim=1))

        out = self.head(out2_cat)
        
        #out = F.interpolate(out, size, mode='bilinear', align_corners=False)
        #out = torch.sigmoid(out)
        #print(out)

        return out
