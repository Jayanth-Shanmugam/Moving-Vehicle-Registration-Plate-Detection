import torch
import cv2 as cv
import pandas as pd
from PIL import Image

model = torch.hub.load('.', 'custom', path = 'best.pt', source = 'local', force_reload = True)

test_image = cv.imread('test_image.jpg')
test_image_rgb = cv.cvtColor(test_image, cv.COLOR_BGR2RGB)

results = model(test_image_rgb)
print(results)

#print(annotations)

#results.show()


