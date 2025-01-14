# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: routing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ..model import model_pb2 as model__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rrouting.proto\x12\x02v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x19google/protobuf/any.proto\x1a\x0bmodel.proto\"\x96\x03\n\x07Routing\x12-\n\x07service\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tnamespace\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1b\n\x08inbounds\x18\x03 \x03(\x0b\x32\t.v1.Route\x12\x1c\n\toutbounds\x18\x04 \x03(\x0b\x32\t.v1.Route\x12+\n\x05\x63time\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05mtime\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08revision\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x42\n\rservice_token\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\rservice_token\x12\x1c\n\x05rules\x18\x15 \x03(\x0b\x32\r.v1.RouteRuleJ\x04\x08\t\x10\x15\"\xad\x01\n\x05Route\x12\x1b\n\x07sources\x18\x01 \x03(\x0b\x32\n.v1.Source\x12%\n\x0c\x64\x65stinations\x18\x02 \x03(\x0b\x32\x0f.v1.Destination\x12-\n\nextendInfo\x18\x03 \x03(\x0b\x32\x19.v1.Route.ExtendInfoEntry\x1a\x31\n\x0f\x45xtendInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xd6\x01\n\x06Source\x12-\n\x07service\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tnamespace\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x08metadata\x18\x03 \x03(\x0b\x32\x18.v1.Source.MetadataEntry\x1a@\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.v1.MatchString:\x02\x38\x01\"\xc7\x03\n\x0b\x44\x65stination\x12-\n\x07service\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tnamespace\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x08metadata\x18\x03 \x03(\x0b\x32\x1d.v1.Destination.MetadataEntry\x12.\n\x08priority\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12,\n\x06weight\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12.\n\x08transfer\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x07isolate\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x04name\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a@\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.v1.MatchString:\x02\x38\x01\"\x8d\x03\n\tRouteRule\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12\x0e\n\x06\x65nable\x18\x04 \x01(\x08\x12\x39\n\x0erouting_policy\x18\x05 \x01(\x0e\x32\x11.v1.RoutingPolicyR\x0erouting_policy\x12<\n\x0erouting_config\x18\x06 \x01(\x0b\x32\x14.google.protobuf.AnyR\x0erouting_config\x12\x10\n\x08revision\x18\x07 \x01(\t\x12\r\n\x05\x63time\x18\x08 \x01(\t\x12\r\n\x05mtime\x18\t \x01(\t\x12\r\n\x05\x65time\x18\n \x01(\t\x12\x10\n\x08priority\x18\x0b \x01(\r\x12\x13\n\x0b\x64\x65scription\x18\x0c \x01(\t\x12\x31\n\nextendInfo\x18\x14 \x03(\x0b\x32\x1d.v1.RouteRule.ExtendInfoEntry\x1a\x31\n\x0f\x45xtendInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe5\x01\n\x10MetadataFailover\x12:\n\x0e\x66\x61ilover_range\x18\x01 \x01(\x0e\x32\".v1.MetadataFailover.FailoverRange\x12\x30\n\x06labels\x18\x02 \x03(\x0b\x32 .v1.MetadataFailover.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"4\n\rFailoverRange\x12\x07\n\x03\x41LL\x10\x00\x12\n\n\x06OTHERS\x10\x01\x12\x0e\n\nOTHER_KEYS\x10\x02\"\xc9\x01\n\x15MetadataRoutingConfig\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x35\n\x06labels\x18\x03 \x03(\x0b\x32%.v1.MetadataRoutingConfig.LabelsEntry\x12&\n\x08\x66\x61ilover\x18\x04 \x01(\x0b\x32\x14.v1.MetadataFailover\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x86\x01\n\x11RuleRoutingConfig\x12\"\n\x07sources\x18\x01 \x03(\x0b\x32\x11.v1.SourceService\x12*\n\x0c\x64\x65stinations\x18\x02 \x03(\x0b\x32\x14.v1.DestinationGroup\x12!\n\x05rules\x18\x03 \x03(\x0b\x32\x12.v1.SubRuleRouting\"n\n\x0eSubRuleRouting\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\"\n\x07sources\x18\x02 \x03(\x0b\x32\x11.v1.SourceService\x12*\n\x0c\x64\x65stinations\x18\x03 \x03(\x0b\x32\x14.v1.DestinationGroup\"W\n\rSourceService\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\"\n\targuments\x18\x03 \x03(\x0b\x32\x0f.v1.SourceMatch\"\xfb\x01\n\x10\x44\x65stinationGroup\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x30\n\x06labels\x18\x03 \x03(\x0b\x32 .v1.DestinationGroup.LabelsEntry\x12\x10\n\x08priority\x18\x04 \x01(\r\x12\x0e\n\x06weight\x18\x05 \x01(\r\x12\x10\n\x08transfer\x18\x06 \x01(\t\x12\x0f\n\x07isolate\x18\x07 \x01(\x08\x12\x0c\n\x04name\x18\x08 \x01(\t\x1a>\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.v1.MatchString:\x02\x38\x01\"\xba\x01\n\x0bSourceMatch\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.v1.SourceMatch.Type\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x1e\n\x05value\x18\x03 \x01(\x0b\x32\x0f.v1.MatchString\"Z\n\x04Type\x12\n\n\x06\x43USTOM\x10\x00\x12\n\n\x06METHOD\x10\x01\x12\n\n\x06HEADER\x10\x02\x12\t\n\x05QUERY\x10\x03\x12\r\n\tCALLER_IP\x10\x04\x12\x08\n\x04PATH\x10\x05\x12\n\n\x06\x43OOKIE\x10\x06*3\n\rRoutingPolicy\x12\x0e\n\nRulePolicy\x10\x00\x12\x12\n\x0eMetadataPolicy\x10\x01\x42\x8d\x01\n7com.tencent.polaris.specification.api.v1.traffic.manageB\x0cRoutingProtoZDgithub.com/polarismesh/specification/source/go/api/v1/traffic_manageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'routing_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n7com.tencent.polaris.specification.api.v1.traffic.manageB\014RoutingProtoZDgithub.com/polarismesh/specification/source/go/api/v1/traffic_manage'
  _ROUTE_EXTENDINFOENTRY._options = None
  _ROUTE_EXTENDINFOENTRY._serialized_options = b'8\001'
  _SOURCE_METADATAENTRY._options = None
  _SOURCE_METADATAENTRY._serialized_options = b'8\001'
  _DESTINATION_METADATAENTRY._options = None
  _DESTINATION_METADATAENTRY._serialized_options = b'8\001'
  _ROUTERULE_EXTENDINFOENTRY._options = None
  _ROUTERULE_EXTENDINFOENTRY._serialized_options = b'8\001'
  _METADATAFAILOVER_LABELSENTRY._options = None
  _METADATAFAILOVER_LABELSENTRY._serialized_options = b'8\001'
  _METADATAROUTINGCONFIG_LABELSENTRY._options = None
  _METADATAROUTINGCONFIG_LABELSENTRY._serialized_options = b'8\001'
  _DESTINATIONGROUP_LABELSENTRY._options = None
  _DESTINATIONGROUP_LABELSENTRY._serialized_options = b'8\001'
  _globals['_ROUTINGPOLICY']._serialized_start=2970
  _globals['_ROUTINGPOLICY']._serialized_end=3021
  _globals['_ROUTING']._serialized_start=94
  _globals['_ROUTING']._serialized_end=500
  _globals['_ROUTE']._serialized_start=503
  _globals['_ROUTE']._serialized_end=676
  _globals['_ROUTE_EXTENDINFOENTRY']._serialized_start=627
  _globals['_ROUTE_EXTENDINFOENTRY']._serialized_end=676
  _globals['_SOURCE']._serialized_start=679
  _globals['_SOURCE']._serialized_end=893
  _globals['_SOURCE_METADATAENTRY']._serialized_start=829
  _globals['_SOURCE_METADATAENTRY']._serialized_end=893
  _globals['_DESTINATION']._serialized_start=896
  _globals['_DESTINATION']._serialized_end=1351
  _globals['_DESTINATION_METADATAENTRY']._serialized_start=829
  _globals['_DESTINATION_METADATAENTRY']._serialized_end=893
  _globals['_ROUTERULE']._serialized_start=1354
  _globals['_ROUTERULE']._serialized_end=1751
  _globals['_ROUTERULE_EXTENDINFOENTRY']._serialized_start=627
  _globals['_ROUTERULE_EXTENDINFOENTRY']._serialized_end=676
  _globals['_METADATAFAILOVER']._serialized_start=1754
  _globals['_METADATAFAILOVER']._serialized_end=1983
  _globals['_METADATAFAILOVER_LABELSENTRY']._serialized_start=1884
  _globals['_METADATAFAILOVER_LABELSENTRY']._serialized_end=1929
  _globals['_METADATAFAILOVER_FAILOVERRANGE']._serialized_start=1931
  _globals['_METADATAFAILOVER_FAILOVERRANGE']._serialized_end=1983
  _globals['_METADATAROUTINGCONFIG']._serialized_start=1986
  _globals['_METADATAROUTINGCONFIG']._serialized_end=2187
  _globals['_METADATAROUTINGCONFIG_LABELSENTRY']._serialized_start=1884
  _globals['_METADATAROUTINGCONFIG_LABELSENTRY']._serialized_end=1929
  _globals['_RULEROUTINGCONFIG']._serialized_start=2190
  _globals['_RULEROUTINGCONFIG']._serialized_end=2324
  _globals['_SUBRULEROUTING']._serialized_start=2326
  _globals['_SUBRULEROUTING']._serialized_end=2436
  _globals['_SOURCESERVICE']._serialized_start=2438
  _globals['_SOURCESERVICE']._serialized_end=2525
  _globals['_DESTINATIONGROUP']._serialized_start=2528
  _globals['_DESTINATIONGROUP']._serialized_end=2779
  _globals['_DESTINATIONGROUP_LABELSENTRY']._serialized_start=2717
  _globals['_DESTINATIONGROUP_LABELSENTRY']._serialized_end=2779
  _globals['_SOURCEMATCH']._serialized_start=2782
  _globals['_SOURCEMATCH']._serialized_end=2968
  _globals['_SOURCEMATCH_TYPE']._serialized_start=2878
  _globals['_SOURCEMATCH_TYPE']._serialized_end=2968
# @@protoc_insertion_point(module_scope)
