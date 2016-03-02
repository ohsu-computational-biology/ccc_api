
GOPATH := $(shell pwd)
export GOPATH
PATH := ${PATH}:$(shell pwd)/bin
export PATH

proxy:
	protoc --python_out ccc_client -I proto  --grpc_out=ccc_client --plugin=protoc-gen-grpc=`which grpc_python_plugin`  `./get_api_proto_files.sh`

swagger: FORCE
	protoc \
	  -I ./ \
		-I $(GOPATH)/src/github.com/gengo/grpc-gateway/third_party/googleapis/ \
 		--swagger_out=logtostderr=true:swagger \
 		`./get_api_proto_files.sh`

install_tools:
	echo $(GOPATH)
	go get -u github.com/gengo/grpc-gateway/protoc-gen-swagger
	go get -u github.com/golang/protobuf/protoc-gen-go

FORCE: 