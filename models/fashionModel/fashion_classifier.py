from torch import nn

input_size = 784
hidden_size = 10
output_size = 10


class FashioniModel(nn.Module):

    def __init__(self, input_size, hidden_size, output_size):

        super().__init__()

        self.layer_stack = nn.Sequential(
            nn.Flatten(),
            nn.Linear(input_size, hidden_size),
            nn.Linear(hidden_size, output_size),
        )

    def forward(self, x):
        return self.layer_stack(x)
