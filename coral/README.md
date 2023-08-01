Coral
====
This repository contains tips of coral.

## Description
N/A

## Demo
N/A

## VS. 
N/A

## Features
N/A

## Requirement

### Hardware requirement

* Mac, M1, 2020

### Operating system requirements

* Mac OS X 10.4.1 Ventura

### Requirements for optional features

I use venv.

```
$ python3 -m venv coral
$ source coral/bin/activate
```

## Usage

  Object detection
* python detect_opencv.py --model models/ssd_mobilenet_v2_coco_quant_postprocess.tflite --labels models/labels.txt --threshold 0.6

## Install

```
$ pip3 install --upgrade pip
$ pip3 install imageio numpy pandas matplotlib japanize_matplotlib scikit-image lxml pillow Cython contextlib2 jupyter notebook scikit-learn seaborn tqdm
$ pip3 install opencv-python opencv-contrib-python
$ pip3 install tensorflow
$ python3 -m pip install --extra-index-url https://google-coral.github.io/py-repo/ pycoral~=2.0
```

## Contribution
N/A

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[Genta Matsukawa](https://github.com/MatsukawaGenta)