# SCONCE (Make Pytorch Development and Deployment Efficient)

This is a Pytorch Helper package aimed to aid the workflow of deep learning model development and deployment. 


1. This packages has boiler plate defintions that can ease the development of torch model development
2. Pruning Techniques are being imported from Tomoco Package
3. Model Quantization and Deployment features are in the development pipeline which will be available for use soon.
## Package install:

```python

pip install sconce

```


## Define Network and Config's:

```python
# Define your network

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 8, 3)
        self.bn1 = nn.BatchNorm2d(8)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(8, 16, 3)
        self.bn2 = nn.BatchNorm2d(16)
        self.fc1 = nn.Linear(16*6*6, 32)
        self.fc2 = nn.Linear(32, 10)

    def forward(self, x):
        x = self.pool(self.bn1(F.relu(self.conv1(x))))
        x = self.pool(self.bn2(F.relu(self.conv2(x))))
        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
    

# Make a Dict for Dataloader

image_size = 32
transforms = {
    "train": Compose([
        RandomCrop(image_size, padding=4),
        RandomHorizontalFlip(),
        ToTensor(),
    ]),
    "test": ToTensor(),
}
dataset = {}
for split in ["train", "test"]:
  dataset[split] = CIFAR10(
    root="data/cifar10",
    train=(split == "train"),
    download=True,
    transform=transforms[split],
  )
dataloader = {}
for split in ['train', 'test']:
  dataloader[split] = DataLoader(
    dataset[split],
    batch_size=512,
    shuffle=(split == 'train'),
    num_workers=0,
    pin_memory=True,
  )
```

## Config:
```python
# Define a cofig of the below parameters

from sconce import sconce, TrainPrune, config

config['model']= Net() # Model Definition
config['criterion'] = nn.CrossEntropyLoss() # Loss
config['optimizer'] = optim.Adam(config['model'].parameters(), lr=1e-4)
config['scheduler'] = optim.lr_scheduler.CosineAnnealingLR(config['optimizer'], T_max=200)
config['dataloader'] = dataloader
config['epochs'] = 1 #Number of time we iterate over the data


```

## Pipeline using Sconce usage:
```python

sconces = sconce()
TrainPrune()

```





### To-Do

- [x] Universal Channel-Wise Pruning
- [x] Update Tutorials
- [+] Fine Grained Purning (In-Progress)
- [ ] Quantisation
- [ ] Universal AutoML package
- [ ] Introduction of Sparsification in Pipeline
