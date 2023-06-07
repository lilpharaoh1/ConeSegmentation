# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class CGNetEnd(torch.nn.Module):
    def __init__(self):
        super(CGNetEnd, self).__init__()
        self.module_0 = py_nndct.nn.Input() #CGNetEnd::input_0
        self.module_1 = py_nndct.nn.Interpolate() #CGNetEnd::CGNetEnd/3
        self.module_2 = py_nndct.nn.Sigmoid() #CGNetEnd::CGNetEnd/4

    def forward(self, *args):
        self.output_module_0 = self.module_0(input=args[0])
        self.output_module_1 = self.module_1(input=self.output_module_0, size=[1088,1456], scale_factor=None, mode='bilinear', align_corners=True)
        self.output_module_2 = self.module_2(self.output_module_1)
        return self.output_module_2
