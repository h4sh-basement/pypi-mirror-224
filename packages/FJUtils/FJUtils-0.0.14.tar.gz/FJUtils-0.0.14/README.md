# FJUtils

a package for custom Jax Flax Functions and Utils
Welcome to FJUtils - A collection of useful functions and utilities for Flax and JAX!
Some Parts of code if from EasyLM <3

## Overview

FJUtils is a collection of functions and utilities that can help with various tasks when using Flax and JAX. It includes
checkpoint savers, partitioning tools, and other helpful functions.
The goal of FJUtils is to make your life easier when working with Flax and JAX. Whether you are training a new model,
fine-tuning an existing one, or just exploring the capabilities of these powerful frameworks, FJUtils has something to
offer.

## Features

Here are some of the features included in FJUtils:

Checkpoint saver: This tool provides an easy way to save and restore checkpoints during training. You can specify how
often to save checkpoints, where to store them, and more.

Partitioning tools: FJUtils includes several tools for partitioning data across multiple devices or nodes. These tools
can help you optimize the performance of your models on clusters or distributed systems.

Other utilities: FJUtils includes a variety of other helpful functions and utilities and more.

## Getting Started

To get started with FJUtils, simply install the package using pip:

```shell
pip install fjutils
```

Once installed, you can import the package and start using its functions and utilities. For example, here's how you can
use the checkpoint saver for loading models like :

```python
from fjutils import StreamingCheckpointer

ckpt = StreamingCheckpointer.load_trainstate_checkpoint('params::<path to model>')

```

or simply getting an optimizer for example adafactor with cosine scheduler :

```python
from jax import numpy as jnp
from fjutils.optimizers import get_adafactor_with_cosine_scheduler

optimizer, scheduler = get_adafactor_with_cosine_scheduler(
    steps=5000,
    learning_rate=5e-5,
    weight_decay=1e-1,
    min_dim_size_to_factor=128,
    decay_rate=0.8,
    decay_offset=0,
    multiply_by_parameter_scale=True,
    clipping_threshold=1.0,
    momentum=None,
    dtype_momentum=jnp.float32,
    weight_decay_rate=None,
    eps=1e-30,
    factored=True,
    weight_decay_mask=None,
)

```

or getting adamw with linear scheduler:

```python
from fjutils.optimizers import get_adamw_with_linear_scheduler

optimizer, scheduler = get_adamw_with_linear_scheduler(
    steps=5000,
    learning_rate_start=5e-5,
    learning_rate_end=1e-5,
    b1=0.9,
    b2=0.999,
    eps=1e-8,
    eps_root=0.0,
    weight_decay=1e-1,
    mu_dtype=None,
)

```

## Documentation

- TODO

## Contributing

FJUtils is an open-source project, and contributions are always welcome! If you have a feature request, bug report, or
just want to help out with development, please check out our GitHub repository and feel free to submit a pull request or
open an issue.

Thank you for using FJUtils, and happy training!

## Credits

- some of the jax utilities are from EasyLM by [Young-Geng](https://github.com/young-geng)
