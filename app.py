import numpy as np
from fastapi import FastAPI, Response, status
from .models.fashionModel import fashion_classifier
import torch

# initialize the app
app = FastAPI()

# initialize the model
model = fashion_classifier.FashioniModel(
    input_size=fashion_classifier.input_size,  # noqa: E501
    hidden_size=fashion_classifier.hidden_size,
    output_size=fashion_classifier.output_size,
)

# load the model weights
model.load_state_dict(torch.load(f="models/fashionModel/fashionModel_params.pth"))


# the api endpoint for prediction
@app.get("/predict/{pixel_values}", status_code=status.HTTP_200_OK)
async def main(pixel_values: str, response: Response):
    pixel_values = np.array([float(p.strip()) for p in pixel_values.split(",")])
    pixel_values = torch.tensor(pixel_values, dtype=torch.float32)
    if len(pixel_values) != 784:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Invalid input, expected 784 pixel values"}
    pixel_values = pixel_values.view(1, 784)
    model.eval()
    with torch.inference_mode():
        output = model(pixel_values)
        predicted = torch.argmax(output)
        prob = output[0][predicted]
    return {"predicted": predicted.item(), "probability": prob.item()}
