#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#  Copyright (c) 2020-2023 Emanuele Ballarin <emanuele@ballarin.cc>
#  Released under the terms of the MIT License
#  (see: https://url.ballarin.cc/mitlicense)
#
# ------------------------------------------------------------------------------
#
# SPDX-License-Identifier: MIT
#
# ------------------------------------------------------------------------------
from .cutmixup import FastCollateMixup
from .cutmixup import Mixup
from .datasets import cifarhundred_dataloader_dispatcher
from .datasets import cifarten_dataloader_dispatcher
from .datasets import fashionmnist_dataloader_dispatcher
from .datasets import imagenette_dataloader_dispatcher
from .datasets import mnist_dataloader_dispatcher

# ------------------------------------------------------------------------------

del cutmixup
del datasets
