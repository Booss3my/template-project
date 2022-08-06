
import torchvision
from torchvision import transforms
import torch
from torch.utils.data import Dataset
import mp
import ctypes
import numpy as np
import tqdm


class custom_image_dataset(Dataset):


    def __init__(self,resize_transforms=transforms.Compose([transforms.Resize(256),transforms.CenterCrop(224)]),type_='labeled',cache =False):

    # parameters:
        #### resize_transforms: resizing transforms
        #### type_: __getitem__ returns (image_tensor,label) or image_tensor
        #### cache: cache dataset to memory


        #self.table:  table containing paths and labels
        self.resize_transforms = resize_transforms #keep the dataset transformations for resize only (other transforms can be done in the dataloader or model with gpu potentially)
        self.type = type_

        ##### caching to save time on dataloading
        if cache:
            nb_samples = #len(data)* 224 *224 * 3   #num samples
            shared_array_base = mp.Array(ctypes.c_float, nb_samples)
            shared_array = np.ctypeslib.as_array(shared_array_base.get_obj())
            shared_array = shared_array.reshape#(len(data), 3, 224, 224)  #tensor shape to save
            self.shared_array = torch.from_numpy(shared_array)
            self.use_cache = False  #you can use load2mem or add $your_dataloader.dataset.set_use_cache(True) at the end of the first epoch

    def __getitem__(self, idx):
        path = #get image path

        if self.use_cache == False:
            out = torchvision.io.read_image(path, torchvision.io.ImageReadMode.RGB) / 255
            out = self.resize_transforms(out)
            self.shared_array[idx] = out
        else:
            out = self.shared_array[idx]

        if self.type == 'no_label':
            return out

        label = #get image label
        return out, label


    def set_use_cache(self, value):
        self.use_cache = value


    def load2mem(self):
        for i in tqdm(range(self.__len__()), desc="Loading..."):
            self.__getitem__(i)
        self.set_use_cache(True)


    def __len__(self):
        # len function
