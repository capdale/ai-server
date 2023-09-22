import numpy as np
import torchvision.transforms as T
from torchvision.transforms.functional import to_pil_image
from torch import load, argmax, Tensor
from os import path
from io import BytesIO
from PIL import Image

from ..model.model import CNN
from .basemodel import ModelBox

class ImageClassify(ModelBox):
    """Image Classifier with cifar10-dataset

    Args:
        ModelBox (interface): interface, must implement method
    """
    def __init__(self, pt_path: str) -> None:
        """initialize end-to-end pipe
        load weight, make transform

        Args:
            pt_path (str): model weight file (.pt) path

        Raises:
            OSError: weight file doesn't exist
        """
        super().__init__()
        # for initialize performance, before load objects check file exists
        if not path.exists(pt_path):
            raise OSError("weight data path is not exist")
        self.transform = T.Compose([
            T.ToTensor(),
            T.Resize((32,32),antialias=True),
            T.Normalize((0.5, 0.5, 0.5), (0.25, 0.25, 0.25)),
        ])
        self.model = CNN(3, 10)
        self.model.load_state_dict(load(pt_path)["model_checkpoint"])

    # this method must be implemented (ModelBox)
    def input(self, byte_array: bytes) -> int:
        stream = BytesIO(byte_array)
        np_img = np.array(Image.open(stream))
        img = self.transform(np_img)
        target = self.model(img)
        key = int(argmax(target))
        return key
    
    # util method for developing
    def watch(self, byte_array: bytes):
        stream = BytesIO(byte_array)
        np_img = np.array(Image.open(stream))
        img: Tensor = self.transform(np_img)
        to_pil_image(img).show()