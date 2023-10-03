# AI server
### Config
Ref [example.yaml](./example.yaml), rename to config.yaml  

## How to run
Ref [example.yaml](./example.yaml), rename to config.yaml  
```powershell
docker build -t aiserver .
```

## Docker build image
```powershell
docker build -t aiserver .
```

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