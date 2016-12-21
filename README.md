# Tensorflow Lab
Experimenting with Tensorflow.



# Installation
This project is built for Tensorflow CPU only version running on Python 3.5 on Mac. 
Create and enter a virtual enviroment and install the required
packages.  Note that you should use `venv` with Python 3 to avoid a
lot of problems. Don't use `virtualenv`.

    python3 -m venv-tfpy3
    . venv-tfpy3/bin/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt 

Read more in [Matplotlib FAQ](http://matplotlib.org/faq/virtualenv_faq.html#short-version).

## Troubleshooting

### SciPy
SciPy needs the latest `pip` and `wheel`, otherwise `pip` will fail while installing the scipy package.
Remedy with:

    python -m pip install --upgrade pip

More information on [SciPy installation page](https://www.scipy.org/install.html).


### Tensorflow
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
