#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2023 Emanuele Ballarin <emanuele@ballarin.cc>
#  Released under the terms of the MIT License
#  (see: https://url.ballarin.cc/mitlicense)
#
# ------------------------------------------------------------------------------
import os
from typing import Optional
from typing import Tuple

from torch.utils.data import DataLoader
from torchvision.datasets import CIFAR10
from torchvision.datasets import CIFAR100
from torchvision.datasets import DatasetFolder
from torchvision.datasets import FashionMNIST
from torchvision.datasets import ImageFolder
from torchvision.datasets import MNIST
from torchvision.transforms import CenterCrop
from torchvision.transforms import Compose
from torchvision.transforms import RandomHorizontalFlip
from torchvision.transforms import RandomResizedCrop
from torchvision.transforms import Resize
from torchvision.transforms import ToTensor


data_root_literal: str = "../datasets/"
cuda_args_true: dict = {"num_workers": 8, "pin_memory": True}


def _dataloader_dispatcher(
    dataset: str,
    data_root: str = data_root_literal,
    batch_size_train: Optional[int] = None,
    batch_size_test: Optional[int] = None,
    cuda_accel: bool = False,
    dataset_kwargs: Optional[dict] = None,
    dataloader_kwargs: Optional[dict] = None,
) -> Tuple[DataLoader, DataLoader, DataLoader]:
    if dataset == "mnist":
        dataset_fx = MNIST
        if batch_size_train is None:
            batch_size_train: int = 256
        if batch_size_test is None:
            batch_size_test: int = 512

    elif dataset == "fashionmnist":
        dataset_fx = FashionMNIST
        if batch_size_train is None:
            batch_size_train: int = 256
        if batch_size_test is None:
            batch_size_test: int = 512

    elif dataset == "cifar10":
        dataset_fx = CIFAR10
        if batch_size_train is None:
            batch_size_train: int = 256
        if batch_size_test is None:
            batch_size_test: int = 512

    elif dataset == "cifar100":
        dataset_fx = CIFAR100
        if batch_size_train is None:
            batch_size_train: int = 256
        if batch_size_test is None:
            batch_size_test: int = 512

    else:
        raise ValueError("Dataset not supported... yet!")

    os.makedirs(name=data_root, exist_ok=True)

    transforms = Compose([ToTensor()])

    # Address dictionary mutability as default argument
    if dataset_kwargs is None:
        dataset_kwargs: dict = {}
    if dataloader_kwargs is None:
        dataloader_kwargs: dict = {}

    trainset = dataset_fx(
        root=data_root,
        train=True,
        transform=transforms,
        download=True,
        **dataset_kwargs,
    )
    testset = dataset_fx(
        root=data_root,
        train=False,
        transform=transforms,
        download=True,
        **dataset_kwargs,
    )

    cuda_args: dict = {}
    if cuda_accel:
        cuda_args: dict = cuda_args_true

    trainloader = DataLoader(
        dataset=trainset,
        batch_size=batch_size_train,
        shuffle=True,
        **cuda_args,
        **dataloader_kwargs,
    )
    testloader = DataLoader(
        dataset=testset,
        batch_size=batch_size_test,
        shuffle=False,
        **cuda_args,
        **dataloader_kwargs,
    )
    test_on_train_loader = DataLoader(
        dataset=trainset,
        batch_size=batch_size_test,
        shuffle=False,
        **cuda_args,
        **dataloader_kwargs,
    )

    return trainloader, testloader, test_on_train_loader


def mnist_dataloader_dispatcher(
    data_root: str = data_root_literal,
    batch_size_train: Optional[int] = None,
    batch_size_test: Optional[int] = None,
    cuda_accel: bool = False,
    dataset_kwargs: Optional[dict] = None,
    dataloader_kwargs: Optional[dict] = None,
) -> Tuple[DataLoader, DataLoader, DataLoader]:
    return _dataloader_dispatcher(
        dataset="mnist",
        data_root=data_root,
        batch_size_train=batch_size_train,
        batch_size_test=batch_size_test,
        cuda_accel=cuda_accel,
        dataset_kwargs=dataset_kwargs,
        dataloader_kwargs=dataloader_kwargs,
    )


def fashionmnist_dataloader_dispatcher(
    data_root: str = data_root_literal,
    batch_size_train: Optional[int] = None,
    batch_size_test: Optional[int] = None,
    cuda_accel: bool = False,
    dataset_kwargs: Optional[dict] = None,
    dataloader_kwargs: Optional[dict] = None,
) -> Tuple[DataLoader, DataLoader, DataLoader]:
    return _dataloader_dispatcher(
        dataset="fashionmnist",
        data_root=data_root,
        batch_size_train=batch_size_train,
        batch_size_test=batch_size_test,
        cuda_accel=cuda_accel,
        dataset_kwargs=dataset_kwargs,
        dataloader_kwargs=dataloader_kwargs,
    )


def cifarten_dataloader_dispatcher(
    data_root: str = data_root_literal,
    batch_size_train: Optional[int] = None,
    batch_size_test: Optional[int] = None,
    cuda_accel: bool = False,
    dataset_kwargs: Optional[dict] = None,
    dataloader_kwargs: Optional[dict] = None,
) -> Tuple[DataLoader, DataLoader, DataLoader]:
    return _dataloader_dispatcher(
        dataset="cifar10",
        data_root=data_root,
        batch_size_train=batch_size_train,
        batch_size_test=batch_size_test,
        cuda_accel=cuda_accel,
        dataset_kwargs=dataset_kwargs,
        dataloader_kwargs=dataloader_kwargs,
    )


def cifarhundred_dataloader_dispatcher(
    data_root: str = data_root_literal,
    batch_size_train: Optional[int] = None,
    batch_size_test: Optional[int] = None,
    cuda_accel: bool = False,
    dataset_kwargs: Optional[dict] = None,
    dataloader_kwargs: Optional[dict] = None,
) -> Tuple[DataLoader, DataLoader, DataLoader]:
    return _dataloader_dispatcher(
        dataset="cifar100",
        data_root=data_root,
        batch_size_train=batch_size_train,
        batch_size_test=batch_size_test,
        cuda_accel=cuda_accel,
        dataset_kwargs=dataset_kwargs,
        dataloader_kwargs=dataloader_kwargs,
    )


def imagenette_dataloader_dispatcher(
    data_root: str = data_root_literal,
    batch_size_train: int = 64,
    batch_size_test: int = 128,
    cuda_accel: bool = False,
    dataset_kwargs: Optional[dict] = None,
    dataloader_kwargs: Optional[dict] = None,
) -> Tuple[DataLoader, DataLoader, DataLoader]:
    if dataset_kwargs is None:
        dataset_kwargs: dict = {}

    train_ds: DatasetFolder = ImageFolder(
        root=data_root + "imagenette2-320/train",
        transform=Compose(
            [
                RandomResizedCrop(224),
                RandomHorizontalFlip(),
                ToTensor(),
            ]
        ),
        **dataset_kwargs,
    )

    test_ds: DatasetFolder = ImageFolder(
        root=data_root + "imagenette2-320/val",
        transform=Compose(
            [
                Resize(256),
                CenterCrop(224),
                ToTensor(),
            ]
        ),
        **dataset_kwargs,
    )

    if dataloader_kwargs is None:
        dataloader_kwargs: dict = {}

    cuda_kwargs: dict = {}
    if cuda_accel:
        cuda_kwargs: dict = cuda_args_true

    train_dl: DataLoader = DataLoader(
        dataset=train_ds,
        batch_size=batch_size_train,
        shuffle=True,
        **cuda_kwargs,
        **dataloader_kwargs,
    )

    test_dl: DataLoader = DataLoader(
        dataset=test_ds,
        batch_size=batch_size_test,
        shuffle=False,
        **cuda_kwargs,
        **dataloader_kwargs,
    )

    tot_dl: DataLoader = DataLoader(
        dataset=train_ds,
        batch_size=batch_size_test,
        shuffle=False,
        **cuda_kwargs,
        **dataloader_kwargs,
    )

    return train_dl, test_dl, tot_dl
