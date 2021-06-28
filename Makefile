all: unixfs_pb2.py

unixfs_pb2.py: unixfs.proto
	protoc --python_out=. $<
