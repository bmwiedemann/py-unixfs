#!/usr/bin/python3
import sys
import unixfs_pb2

node = unixfs_pb2.PBNode()
link = unixfs_pb2.PBLink()
link.Hash = b"\001U\022 \2129\322\253\323\231\232\267<4\333$v\204\234\335\363\003\3168\2335\202hP\371\247\000X\233J\220"
link.Tsize = 262144
#link.Name = ""
node.Links.extend([link,link])
dataparsed = unixfs_pb2.Data()
dataparsed.Type = unixfs_pb2.Data.DataType.File
dataparsed.blocksizes.extend([262144,262144])
dataparsed.filesize = 262144*2
#dataparsed.hashType = 0
#dataparsed.fanout = 0
node.Data = dataparsed.SerializeToString()
nodebytes = node.SerializeToString()
sys.stdout.buffer.write(nodebytes)

