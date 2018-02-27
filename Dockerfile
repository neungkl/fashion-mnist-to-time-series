FROM neungkl/keras

RUN pip3 install jupyterlab

CMD ["jupyter", "lab", "--allow-root"]