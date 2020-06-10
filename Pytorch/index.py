# 14 January 2020
import torch

output = torch.tensor([[0.1, 1.2]])
print(torch.sigmoid(output))
print(torch.argmax(torch.sigmoid(output)))