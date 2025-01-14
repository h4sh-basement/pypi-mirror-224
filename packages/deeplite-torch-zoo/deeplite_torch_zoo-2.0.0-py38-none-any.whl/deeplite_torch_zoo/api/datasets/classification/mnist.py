import os
import sys
from os.path import expanduser

import torchvision
from torchvision import transforms

from deeplite_torch_zoo.api.datasets.utils import get_dataloader
from deeplite_torch_zoo.api.registries import DATASET_WRAPPER_REGISTRY
from deeplite_torch_zoo.utils import LOGGER


__all__ = ["get_mnist"]


@DATASET_WRAPPER_REGISTRY.register(dataset_name="mnist")
def get_mnist(
    data_root="",
    batch_size=128,
    num_workers=4,
    fp16=False,
    download=True,
    distributed=False,
    **kwargs,
):
    if kwargs:
        LOGGER.warning(
            f"Warning, {sys._getframe().f_code.co_name}: extra arguments {list(kwargs.keys())}!"
        )

    if data_root == "":
        data_root = os.path.join(expanduser("~"), ".deeplite-torch-zoo")

    train_dataset = torchvision.datasets.MNIST(
        root=data_root,
        train=True,
        download=download,
        transform=transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
        ),
    )

    test_dataset = torchvision.datasets.MNIST(
        root=data_root,
        train=False,
        download=download,
        transform=transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
        ),
    )

    train_loader = get_dataloader(
        train_dataset,
        batch_size=batch_size,
        num_workers=num_workers,
        fp16=fp16,
        distributed=distributed,
        shuffle=not distributed,
    )

    test_loader = get_dataloader(
        test_dataset,
        batch_size=batch_size,
        num_workers=num_workers,
        fp16=fp16,
        distributed=distributed,
        shuffle=False,
    )

    return {"train": train_loader, "test": test_loader}
