# Tensorflow Lab
Experimenting with Tensorflow.



# Installation
This project is built for Tensorflow CPU only version running on Python 3.5 on Mac. 

## Troubleshooting
If Tensorflow does not install from the requirements.txt file, try this

    # first activate virtualenv
    . venv-tfpy3/bin/activate
    # then install
    export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.12.0-py3-none-any.whl
    pip3 install --upgrade $TF_BINARY_URL

Refer to the TF [installation page](https://www.tensorflow.org/get_started/os_setup#pip_installation) 
for further information.

## Test the installation
Run the `helloworld.py` script (the Tensorflow Getting Started example):

    . venv-tfpy3/bin/activate
    python3 helloworld.py