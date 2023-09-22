## RPC
```powershell
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. --pyi_out=. ./proto/image.proto
```
Or use [./MakeProto.ps1](./MakeProto.ps1)  
```powershell
./Makeproto.ps1 image
```
Automatically use ./proto/{filename}.proto  

## Protocol
### Image
[image.proto](./proto/image.proto)  

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
 - /proto: define .proto file and python grpc files, [Check latest version](https://github.com/capdale/rpc-protocol)
 - /service: group of service class
 - server.py: main server py