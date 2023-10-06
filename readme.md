# AI server
### Config
Ref [example.yaml](./example.yaml), rename to config.yaml  

## Docker build image
```powershell
# docker build -t <tag> .
docker build -t aiserver .
```
ref [Dockerfile](./Dockerfile)  

## Run in docker
After build image  
```powershell
# docker run -d -p <port>:<prot> --gpus <gpus> --name <name> aiserver
docker run -d -p 50050:50050 --gpus all --name aiserver aiserver
```

## How to run
1. Config
2. Build docker image
3. Run in Docker

## RPC
[Check proto here](https://github.com/capdale/rpc-protocol)  

## File structure
```
ai-server
 ┣ funcmodel
 ┃ ┣ func
 ┃ ┣ model
 ┃ ┗ weight
 ┣ proto
 ┃ ┣ *.proto
 ┃ ┣ *.py
 ┃ ┣ *.pyi
 ┃ ┗ *.py
 ┣ service
 ┃ ┗ image_classifier.py
 ┣ .gitignore
 ┣ MakeProto.ps1
 ┣ readme.md
 ┣ requirements.txt
 ┗ server.py
 ```

 - /funcmodel: end-to-end ai model, [Check latest version](https://github.com/capdale/TEST-CNNmodel)
 - /proto: define .proto file and python grpc files, [Check proto here](https://github.com/capdale/rpc-protocol)
 - /service: group of service class
 - server.py: main server py