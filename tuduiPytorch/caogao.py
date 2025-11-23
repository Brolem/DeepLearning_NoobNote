import torch
from torch import nn

class TuDui(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 3)
        
    def forward(self, input):
        output = input + 1
        return output
    
tudui = TuDui()
x = torch.tensor(1.0)
output = tudui(x)
print(output)

writer = SummaryWriter("logs_seq")