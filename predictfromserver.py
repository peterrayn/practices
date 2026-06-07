import torch
import torch.nn as nn
from torchvision import models,transforms


model =models.resnet18(pretrained=True)
model.fc=nn.Linear(model.fc.in_features,10)
try:
    model.load_state_dict(torch.load("./model.ckpt")['state_dict'])
except Exception as e:
    print("fail to load",e)
    exit(0)

transform=transforms.Compose([transforms.Resize((224,224)),transforms.ToTensor()])


def predict(img):

    img=[transform(i) for i in img]
    img=torch.stack(img)
    model.eval()
    pred=model(img)
    pred=torch.argmax(pred,dim=1)
    reflet_types=["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]
    return [reflet_types[p] for p in pred]
