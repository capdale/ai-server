### RPC
```powershell
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. --pyi_out=. ./proto/image.proto
```
Or use [./MakeProto.ps1](./MakeProto.ps1)
```powershell
./Makeproto.ps1 image
```
Automatically use ./proto/{filename}.proto

### File structure
```
ai-server
 ┣ proto
 ┃ ┃ ┣ image_pb2.cpython-311.pyc
 ┃ ┃ ┗ image_pb2_grpc.cpython-311.pyc
 ┃ ┣ image.proto
 ┃ ┣ image_pb2.py
 ┃ ┣ image_pb2.pyi
 ┃ ┗ image_pb2_grpc.py
 ┣ service
 ┃ ┗ image_classifier.py
 ┣ .gitignore
 ┣ MakeProto.ps1
 ┣ readme.md
 ┣ requirements.txt
 ┗ server.py
 ```

 - /proto: define .proto file and python grpc files
 - /service: group of service class
 - server.py: main server py