### RPC
```powershell
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. --pyi_out=. ./proto/image.proto
```