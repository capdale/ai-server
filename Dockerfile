FROM ubuntu:latest

LABEL author="devhoodit"

RUN apt-get update && apt-get install wget -y
RUN wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh -O /Miniforge3-Linux-x86_64.sh && /bin/bash /Miniforge3-Linux-x86_64.sh -b -p /opt/conda
ENV PATH="/opt/conda/bin:$PATH"

RUN conda init --all
RUN conda create -n server python=3.10 -y && echo "source activate server" > ~/.bashrc
ENV PATH=/opt/conda/envs/server/bin:$PATH
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

WORKDIR /server

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "/bin/bash", "-c", "python3 server.py" ]