import torch
# import torchvision
from pytorch_nndct.apis import torch_quantizer, dump_xmodel#, Inspector

from models.CGNet.CGNetPyVitis import CGNet, CGNetEnd
from models.ENet.ENet import ENet, ENetEnd
#from SimpleNet.simple_net import SimpleNet
from cone_dataset import CustomDataset, build_dataset
from display_masks import display_pred_masks
from evaluate import evaluate

# inspector = Inspector("DPUCZDX8G_ISA0_B4096")

dataset = CustomDataset()

model = CGNet().cpu()
model_end = CGNetEnd().cpu()
# model = ENet().cpu()
# model_end = ENetEnd().cpu()
# model = SimpleNet().cpu()
# state_dict = torch.load('weights/CGNetWeights_wrong_conv_4')
state_dict = torch.load('weights/CGNetWeights_conv_2')
# state_dict = torch.load('weights/CGNetWeights_avmax')
model.load_state_dict(state_dict)
# input = torch.rand([1, 3, 544, 728])
input = torch.rand([1, 3, 1088, 1456])
# input, _ = dataset[0]
# input = input.unsqueeze(0)
# print(input.shape)
#input = torch.rand([1, 3, 924, 1236])

# input = torch.rand([1, 1, 28, 28])

# inspector.inspect(model, (input,), device=torch.device('cpu'))
print("model created...")

img, mask = dataset[5]

out = model(img.unsqueeze(0))
out = model_end(out)

# # out = model_end(out)
# # print(out)
display_pred_masks(model, model_end, img, mask[0], output_name='normal_output.png')
print(out)
print(out.shape)
print("model runs normally...")

# # train_loader, test_loader = build_dataset(test_split=0.02)
loss_fn = torch.nn.BCELoss().to(torch.device('cpu'))

calib_dataset = torch.zeros([10, 3, 1088, 1456])
for i in range(10):
    img, mask = dataset[i]
    calib_dataset[i] = img

print("calib dataset created...")

print("calibration starting...")
quantizer = torch_quantizer('calib', model, calib_dataset, device=torch.device('cpu'))#, quant_config_file='./quant_config.json')
quant = quantizer.quant_model

# finetune = True

# quant_mode = 'calib'

# if finetune == True:
#       ft_loader, _ = build_dataset(test_split=0.98)
#       if quant_mode == 'calib':
#         quantizer.fast_finetune(evaluate, (quant, model_end, loss_fn))
#       elif quant_mode == 'test':
#         quantizer.load_ft_param()

eval_loss = evaluate(quant, model_end, loss_fn, e=1, test_split=0.15, eval=True)
# quant.eval()
# quant(img.unsqueeze(0))
# # # quant(torch.rand([1, 1, 28, 28]))
# # # torch.save(quant.state_dict(), "quantize_result/quant.pth")
# # # out = model_end(out)
# # # img, mask = dataset[0]
img, mask = dataset[5]
display_pred_masks(quant, model_end, img, mask[0], output_name='calib_output_epoch1_test4.png')

quantizer.export_quant_config()

# for i in range(3000):
#     if i % 50 == 0 and i != 0:
#         print(i)
#         output_name = 'calib_images/calib_output' + str(i) + '.png'
#         img, mask = dataset[1]
#         display_pred_masks(quant, quant_head, img, mask[0], output_name=output_name)
#     img, _ = dataset[i % 1000]
#     out = quant(img.unsqueeze(0))
#     out = quant_head(out)
    # print(i % 1000)

# quantizer.load_ft_param()

print("model calibrated...")

quantizer = torch_quantizer('test', model, img.unsqueeze(0), device=torch.device('cpu'),)# quant_config_file='./quant_config.json')
# # # # quantizer = torch_quantizer('test', model, torch.rand([1, 1, 28, 28]), device=torch.device('cpu'),)# quant_config_file='./quant_config.json')
quant = quantizer.quant_model
# # # img, mask = dataset[0]

# # quant(img.unsqueeze(0))

# # quantizer.load_ft_param()

eval_loss = evaluate(quant, model_end, loss_fn, e=1, test_split=0.15, eval=True)
print("Evaluation Loss : ", eval_loss)

display_pred_masks(quant, model_end, img, mask[0], output_name='test_output_epoch1_test4.png')
# print("exporting to xmodel...")
quantizer.export_xmodel(deploy_check=False)
# # # # quantizer.export_onnx_model()

