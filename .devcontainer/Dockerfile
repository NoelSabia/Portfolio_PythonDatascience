FROM mcr.microsoft.com/devcontainers/base:ubuntu

RUN apt-get update && apt-get install -y xz-utils

# Install gcc
RUN apt-get install gcc -y

# Install clang
RUN apt-get install clang -y

# Install git
RUN apt install git-all -y

# Install valgrind
RUN apt-get install git-core sudo build-essential cmake valgrind libcppunit-dev -y

#install ZSH
RUN apt install zsh -y

#install curl
RUN apt install curl -y
RUN apt-get install -y libreadline-dev

# Install python and all important extentions
RUN apt install python3-pip -y
RUN apt-get install python-dev-is-python3 -y
RUN apt install python3.10-venv -y
RUN python3 -m pip install --upgrade pip setuptools
RUN python3 -m pip install matplotlib
RUN python3 -m pip install pandas
RUN python3 -m pip install numpy
RUN python3 -m pip install pyarrow
RUN python3 -m pip install seaborn
RUN python3 -m pip install scikit-learn

# Specifies the shell that the Docker container uses
CMD [ "zsh" ]