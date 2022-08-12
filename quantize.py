import torch
import torchvision
from pytorch_nndct.apis import torch_quantizer, dump_xmodel, Inspector

from ConeSegmentation.CGNetPy1 import CGNet
from simple_net import SimpleNet

inspector = Inspector("DPUCZDX8G_ISA0_B4096")

# model = CGNet().cpu()
model = SimpleNet().cpu()
#model.load_state_dict(torch.load("ConeSegmentation/weights_tuned/CGNetWeights_deployable"))
# input = torch.rand([1, 3, 544, 728])
# input = torch.rand([1, 3, 1088, 1456])
#input = torch.rand([1, 3, 924, 1236])

input = torch.rand([1, 1, 28, 28])

inspector.inspect(model, (input,), device=torch.device('cpu'))
print("model inspected...")

quantizer = torch_quantizer('calib', model, input, device=torch.device('cpu'), quant_config_file='./quant_config.json')
quant = quantizer.quant_model
quant(input)
print("calib model quantised...")
quantizer.export_quant_config()
print("model calibrated...")

quantizer = torch_quantizer('test', model, input, device=torch.device('cpu'), quant_config_file='./quant_config.json')
quant = quantizer.quant_model
quant(input)
print("exporting to xmodel...")
quantizer.export_xmodel()
quantizer.export_onnx_model()

