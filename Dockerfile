FROM neungkl/keras

# install JupyterLab 
RUN pip3 install jupyterlab

# install Git
RUN apt-get update && apt-get install -y git

# install Python's libraries
RUN pip3 install cython
RUN pip3 install git+https://github.com/lukauskas/dtwco

CMD ["jupyter", "lab", "--allow-root"]