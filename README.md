# AutoRA Bayesian Machine Scientist

`autora-theorist-bms` is a Python module built on AutoRA that can be used to discover equations that fit data.

Website: [https://autoresearch.github.io/autora/](https://autoresearch.github.io/autora/)

## User Guide

You will need:

- `python` 3.8 or greater: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Install BMS as part of the `autora` package:

```shell
pip install -U "autora[theorist-bms]" --pre
```

> It is recommended to use a `python` environment manager like `virtualenv`.

Check your installation by running:
```shell
python -c "from autora.theorist.bms import BMSRegressor; BMSRegressor()"
```

Guimera, R, Reichardt, I, Aguilar-Mogas, A, Massucci, FA, Miranda, M, Pallares, J, Sales-Pardo, M. A Bayesian machine scientist to aid in the solution of challenging scientific problems, Sci. Adv. 6 (5) , eaav6971 (2020).
