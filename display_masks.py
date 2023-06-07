import torch
import matplotlib.pyplot as plt
import numpy as np

def display_pred_masks(model, model_end, image, label, output_name='output.png'):
    num_rows = 1

    num_columns = 3
    fig, axes = plt.subplots(num_rows, num_columns, figsize=(num_columns * 4, num_rows * 4))
    axes = axes.reshape(-1, num_columns)
    plt.tight_layout()
    
#     tensor_image = torch.tensor(image).double()
#     tensor_image = tensor_image.reshape(1, *tensor_image.shape)
#     output = model(tensor_image.double())
    
    image = torch.tensor(image).unsqueeze(0)
    output = model(image)
    output = model_end(output)
        
    axes[0, 0].imshow(image.squeeze().permute(1,2,0))
    axes[0, 0].set_xlabel("Image")
    axes[0, 0].axes.set_xticks([])
    axes[0, 0].axes.set_yticks([])
    axes[0, 1].imshow(label.squeeze())
    axes[0, 1].set_xlabel("Mask")
    axes[0, 1].axes.set_xticks([])
    axes[0, 1].axes.set_yticks([])
        
    base_array = np.zeros_like(output.detach().numpy())
    base_array[output > 0.5] = 1
    
    axes[0, 2].imshow(base_array.squeeze())
    axes[0, 2].set_xlabel("Pred Mask")
    axes[0, 2].axes.set_xticks([])
    axes[0, 2].axes.set_yticks([])

    plt.show()
    plt.savefig(output_name)