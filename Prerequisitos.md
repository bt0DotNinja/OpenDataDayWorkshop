# Prerequisitos

Las practicas estan diseñadas para ejecutarse en Python 3.6 en un [Notebook de Jupyter](http://jupyter.readthedocs.io/en/latest/content-quickstart.html)

# Jupyter Notebook

## Windows y Mac OS X

Para los sistemas operativos Windows y Mac recomendamos la distribucion de [Python Anaconda 3.6](https://www.anaconda.com/download/) que incluyen todos los paquetes requeridos en las practicas.

## GNU/Linux

Los requerimientos basicos son tener instalado python 3.

### Fedora 26 o superior

```bash
$ sudo dnf group install 'Python Science' 'Python Classroom'
```

### Ubuntu 17.04 o superior.

```$ sudo apt install jupyter-notebook jupyter-core python-ipykernel ```

### Debian, Ubuntu 16.04 o anteriores
```bash
$ sudo apt-get install python-pip
$ pip install --upgrade pip 
$ sudo pip install jupyter
```

###  ArchLinux

```bash
$ sudo pacman -Sy jupyter-notebook jupyter-nbconvert python-ipywidgets
```

## Test

