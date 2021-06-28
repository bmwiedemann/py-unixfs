#!/usr/bin/python3
import unixfs_pb2

data = ""
#with open("test/bafybeihwooctskg5ke3ymjutqdbsutdtj74g7l734ieiprxsiw77mmyvoq", "rb") as f:
with open("test/bafybeig5axbv7uxiwv63kn6qvegw5vbz2tlgv4nhz4crv6g3f3rat7ttsi", "rb") as f:
#with open("test/file256k.data", "rb") as f:
    data = f.read(4096)

nodeparsed = unixfs_pb2.PBNode()
nodeparsed.ParseFromString(data)
dataparsed = unixfs_pb2.Data()
dataparsed.ParseFromString(nodeparsed.Data)

print("links="+str(nodeparsed.Links))

print("type="+str(dataparsed.Type))
print("size="+str(dataparsed.filesize))
print("blocksizse="+str(dataparsed.blocksizes))
print("hashType="+str(dataparsed.hashType))
print("fanout="+str(dataparsed.fanout))
#print(dataparsed.SerializeToString())

