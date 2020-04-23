# git proto

## prerequisite
https://grpc.io/docs/quickstart/python/
https://grpc.io/docs/quickstart/go/



## convert proto to python file


```
python -m grpc_tools.protoc -Iproto  --python_out=proto --grpc_python_out=proto  proto/git.proto
```

실행 경로 위치는 git.proto 파일보다 한단계 상위폴더 여야 함 …. (clone한 디렉토리의 경로 ... \git-proto>   )
프로토 파일을 python 파일로 변환법  … 클라이언트 용...
-Iproto 처음 인자는 .proto 파일이 들어있는 폴더명….
--python_out=proto --grpc_python_out=proto 두번째 세번째 인자는 파일 생성 위치 …
proto/git.proto 네번째 인자는 변환할 프로토파일 위치 … (복수개 가능)


## convert proto to go file

```
protoc --go_out=plugins=grpc:proto  proto/git.proto
```
파일이 있는 위치에서 가능 …

첫번째 인자 파일 나올 위치인데  grpc용으로 컴파일하는 거라 grpc 플러그인 명시 해줘야 함 ….
두번째 인자는 컴파일할 파일위치 


## ETC
```
C:\Users\hosuk\go\src\proto>python -m grpc_tools.protoc --proto_path=../proto  --python_out=. --grpc_python_out=.  git.proto
protoc --go_out=plugins=grpc:.  ./git.proto
```
