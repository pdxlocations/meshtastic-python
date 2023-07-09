# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/mesh.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from meshtastic import channel_pb2 as meshtastic_dot_channel__pb2
from meshtastic import config_pb2 as meshtastic_dot_config__pb2
from meshtastic import module_config_pb2 as meshtastic_dot_module__config__pb2
from meshtastic import portnums_pb2 as meshtastic_dot_portnums__pb2
from meshtastic import telemetry_pb2 as meshtastic_dot_telemetry__pb2
from meshtastic import xmodem_pb2 as meshtastic_dot_xmodem__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15meshtastic/mesh.proto\x1a\x18meshtastic/channel.proto\x1a\x17meshtastic/config.proto\x1a\x1emeshtastic/module_config.proto\x1a\x19meshtastic/portnums.proto\x1a\x1ameshtastic/telemetry.proto\x1a\x17meshtastic/xmodem.proto\"\xb7\x05\n\x08Position\x12\x12\n\nlatitude_i\x18\x01 \x01(\x0f\x12\x13\n\x0blongitude_i\x18\x02 \x01(\x0f\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x05\x12\x0c\n\x04time\x18\x04 \x01(\x07\x12,\n\x0flocation_source\x18\x05 \x01(\x0e\x32\x13.Position.LocSource\x12,\n\x0f\x61ltitude_source\x18\x06 \x01(\x0e\x32\x13.Position.AltSource\x12\x11\n\ttimestamp\x18\x07 \x01(\x07\x12\x1f\n\x17timestamp_millis_adjust\x18\x08 \x01(\x05\x12\x14\n\x0c\x61ltitude_hae\x18\t \x01(\x11\x12#\n\x1b\x61ltitude_geoidal_separation\x18\n \x01(\x11\x12\x0c\n\x04PDOP\x18\x0b \x01(\r\x12\x0c\n\x04HDOP\x18\x0c \x01(\r\x12\x0c\n\x04VDOP\x18\r \x01(\r\x12\x14\n\x0cgps_accuracy\x18\x0e \x01(\r\x12\x14\n\x0cground_speed\x18\x0f \x01(\r\x12\x14\n\x0cground_track\x18\x10 \x01(\r\x12\x13\n\x0b\x66ix_quality\x18\x11 \x01(\r\x12\x10\n\x08\x66ix_type\x18\x12 \x01(\r\x12\x14\n\x0csats_in_view\x18\x13 \x01(\r\x12\x11\n\tsensor_id\x18\x14 \x01(\r\x12\x13\n\x0bnext_update\x18\x15 \x01(\r\x12\x12\n\nseq_number\x18\x16 \x01(\r\"N\n\tLocSource\x12\r\n\tLOC_UNSET\x10\x00\x12\x0e\n\nLOC_MANUAL\x10\x01\x12\x10\n\x0cLOC_INTERNAL\x10\x02\x12\x10\n\x0cLOC_EXTERNAL\x10\x03\"b\n\tAltSource\x12\r\n\tALT_UNSET\x10\x00\x12\x0e\n\nALT_MANUAL\x10\x01\x12\x10\n\x0c\x41LT_INTERNAL\x10\x02\x12\x10\n\x0c\x41LT_EXTERNAL\x10\x03\x12\x12\n\x0e\x41LT_BAROMETRIC\x10\x04\"\x85\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tlong_name\x18\x02 \x01(\t\x12\x12\n\nshort_name\x18\x03 \x01(\t\x12\x13\n\x07macaddr\x18\x04 \x01(\x0c\x42\x02\x18\x01\x12 \n\x08hw_model\x18\x05 \x01(\x0e\x32\x0e.HardwareModel\x12\x13\n\x0bis_licensed\x18\x06 \x01(\x08\"\x1f\n\x0eRouteDiscovery\x12\r\n\x05route\x18\x01 \x03(\x07\"\xdb\x02\n\x07Routing\x12(\n\rroute_request\x18\x01 \x01(\x0b\x32\x0f.RouteDiscoveryH\x00\x12&\n\x0broute_reply\x18\x02 \x01(\x0b\x32\x0f.RouteDiscoveryH\x00\x12&\n\x0c\x65rror_reason\x18\x03 \x01(\x0e\x32\x0e.Routing.ErrorH\x00\"\xca\x01\n\x05\x45rror\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08NO_ROUTE\x10\x01\x12\x0b\n\x07GOT_NAK\x10\x02\x12\x0b\n\x07TIMEOUT\x10\x03\x12\x10\n\x0cNO_INTERFACE\x10\x04\x12\x12\n\x0eMAX_RETRANSMIT\x10\x05\x12\x0e\n\nNO_CHANNEL\x10\x06\x12\r\n\tTOO_LARGE\x10\x07\x12\x0f\n\x0bNO_RESPONSE\x10\x08\x12\x14\n\x10\x44UTY_CYCLE_LIMIT\x10\t\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10 \x12\x12\n\x0eNOT_AUTHORIZED\x10!B\t\n\x07variant\"\x9c\x01\n\x04\x44\x61ta\x12\x19\n\x07portnum\x18\x01 \x01(\x0e\x32\x08.PortNum\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x15\n\rwant_response\x18\x03 \x01(\x08\x12\x0c\n\x04\x64\x65st\x18\x04 \x01(\x07\x12\x0e\n\x06source\x18\x05 \x01(\x07\x12\x12\n\nrequest_id\x18\x06 \x01(\x07\x12\x10\n\x08reply_id\x18\x07 \x01(\x07\x12\r\n\x05\x65moji\x18\x08 \x01(\x07\"\x93\x01\n\x08Waypoint\x12\n\n\x02id\x18\x01 \x01(\r\x12\x12\n\nlatitude_i\x18\x02 \x01(\x0f\x12\x13\n\x0blongitude_i\x18\x03 \x01(\x0f\x12\x0e\n\x06\x65xpire\x18\x04 \x01(\r\x12\x11\n\tlocked_to\x18\x05 \x01(\r\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x0c\n\x04icon\x18\x08 \x01(\x07\"l\n\x16MqttClientProxyMessage\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0e\n\x04\x64\x61ta\x18\x02 \x01(\x0cH\x00\x12\x0e\n\x04text\x18\x03 \x01(\tH\x00\x12\x10\n\x08retained\x18\x04 \x01(\x08\x42\x11\n\x0fpayload_variant\"\xcb\x03\n\nMeshPacket\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x07\x12\n\n\x02to\x18\x02 \x01(\x07\x12\x0f\n\x07\x63hannel\x18\x03 \x01(\r\x12\x18\n\x07\x64\x65\x63oded\x18\x04 \x01(\x0b\x32\x05.DataH\x00\x12\x13\n\tencrypted\x18\x05 \x01(\x0cH\x00\x12\n\n\x02id\x18\x06 \x01(\x07\x12\x0f\n\x07rx_time\x18\x07 \x01(\x07\x12\x0e\n\x06rx_snr\x18\x08 \x01(\x02\x12\x11\n\thop_limit\x18\t \x01(\r\x12\x10\n\x08want_ack\x18\n \x01(\x08\x12&\n\x08priority\x18\x0b \x01(\x0e\x32\x14.MeshPacket.Priority\x12\x0f\n\x07rx_rssi\x18\x0c \x01(\x05\x12$\n\x07\x64\x65layed\x18\r \x01(\x0e\x32\x13.MeshPacket.Delayed\"[\n\x08Priority\x12\t\n\x05UNSET\x10\x00\x12\x07\n\x03MIN\x10\x01\x12\x0e\n\nBACKGROUND\x10\n\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10@\x12\x0c\n\x08RELIABLE\x10\x46\x12\x07\n\x03\x41\x43K\x10x\x12\x07\n\x03MAX\x10\x7f\"B\n\x07\x44\x65layed\x12\x0c\n\x08NO_DELAY\x10\x00\x12\x15\n\x11\x44\x45LAYED_BROADCAST\x10\x01\x12\x12\n\x0e\x44\x45LAYED_DIRECT\x10\x02\x42\x11\n\x0fpayload_variant\"\xa3\x01\n\x08NodeInfo\x12\x0b\n\x03num\x18\x01 \x01(\r\x12\x13\n\x04user\x18\x02 \x01(\x0b\x32\x05.User\x12\x1b\n\x08position\x18\x03 \x01(\x0b\x32\t.Position\x12\x0b\n\x03snr\x18\x04 \x01(\x02\x12\x12\n\nlast_heard\x18\x05 \x01(\x07\x12&\n\x0e\x64\x65vice_metrics\x18\x06 \x01(\x0b\x32\x0e.DeviceMetrics\x12\x0f\n\x07\x63hannel\x18\x07 \x01(\r\"\xba\x03\n\nMyNodeInfo\x12\x13\n\x0bmy_node_num\x18\x01 \x01(\r\x12\x13\n\x07has_gps\x18\x02 \x01(\x08\x42\x02\x18\x01\x12\x18\n\x0cmax_channels\x18\x03 \x01(\rB\x02\x18\x01\x12\x1c\n\x10\x66irmware_version\x18\x04 \x01(\tB\x02\x18\x01\x12*\n\nerror_code\x18\x05 \x01(\x0e\x32\x12.CriticalErrorCodeB\x02\x18\x01\x12\x19\n\rerror_address\x18\x06 \x01(\rB\x02\x18\x01\x12\x17\n\x0b\x65rror_count\x18\x07 \x01(\rB\x02\x18\x01\x12\x14\n\x0creboot_count\x18\x08 \x01(\r\x12\x13\n\x07\x62itrate\x18\t \x01(\x02\x42\x02\x18\x01\x12 \n\x14message_timeout_msec\x18\n \x01(\rB\x02\x18\x01\x12\x17\n\x0fmin_app_version\x18\x0b \x01(\r\x12\x19\n\rair_period_tx\x18\x0c \x03(\rB\x02\x18\x01\x12\x19\n\rair_period_rx\x18\r \x03(\rB\x02\x18\x01\x12\x14\n\x08has_wifi\x18\x0e \x01(\x08\x42\x02\x18\x01\x12\x1f\n\x13\x63hannel_utilization\x18\x0f \x01(\x02\x42\x02\x18\x01\x12\x17\n\x0b\x61ir_util_tx\x18\x10 \x01(\x02\x42\x02\x18\x01\"\xb5\x01\n\tLogRecord\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\x07\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x1f\n\x05level\x18\x04 \x01(\x0e\x32\x10.LogRecord.Level\"X\n\x05Level\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08\x43RITICAL\x10\x32\x12\t\n\x05\x45RROR\x10(\x12\x0b\n\x07WARNING\x10\x1e\x12\x08\n\x04INFO\x10\x14\x12\t\n\x05\x44\x45\x42UG\x10\n\x12\t\n\x05TRACE\x10\x05\"P\n\x0bQueueStatus\x12\x0b\n\x03res\x18\x01 \x01(\x05\x12\x0c\n\x04\x66ree\x18\x02 \x01(\r\x12\x0e\n\x06maxlen\x18\x03 \x01(\r\x12\x16\n\x0emesh_packet_id\x18\x04 \x01(\r\"\xe2\x03\n\tFromRadio\x12\n\n\x02id\x18\x01 \x01(\r\x12\x1d\n\x06packet\x18\x02 \x01(\x0b\x32\x0b.MeshPacketH\x00\x12\x1e\n\x07my_info\x18\x03 \x01(\x0b\x32\x0b.MyNodeInfoH\x00\x12\x1e\n\tnode_info\x18\x04 \x01(\x0b\x32\t.NodeInfoH\x00\x12\x19\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\x07.ConfigH\x00\x12 \n\nlog_record\x18\x06 \x01(\x0b\x32\n.LogRecordH\x00\x12\x1c\n\x12\x63onfig_complete_id\x18\x07 \x01(\rH\x00\x12\x12\n\x08rebooted\x18\x08 \x01(\x08H\x00\x12%\n\x0cmoduleConfig\x18\t \x01(\x0b\x32\r.ModuleConfigH\x00\x12\x1b\n\x07\x63hannel\x18\n \x01(\x0b\x32\x08.ChannelH\x00\x12#\n\x0bqueueStatus\x18\x0b \x01(\x0b\x32\x0c.QueueStatusH\x00\x12\x1f\n\x0cxmodemPacket\x18\x0c \x01(\x0b\x32\x07.XModemH\x00\x12#\n\x08metadata\x18\r \x01(\x0b\x32\x0f.DeviceMetadataH\x00\x12\x39\n\x16mqttClientProxyMessage\x18\x0e \x01(\x0b\x32\x17.MqttClientProxyMessageH\x00\x42\x11\n\x0fpayload_variant\"\xc7\x01\n\x07ToRadio\x12\x1d\n\x06packet\x18\x01 \x01(\x0b\x32\x0b.MeshPacketH\x00\x12\x18\n\x0ewant_config_id\x18\x03 \x01(\rH\x00\x12\x14\n\ndisconnect\x18\x04 \x01(\x08H\x00\x12\x1f\n\x0cxmodemPacket\x18\x05 \x01(\x0b\x32\x07.XModemH\x00\x12\x39\n\x16mqttClientProxyMessage\x18\x06 \x01(\x0b\x32\x17.MqttClientProxyMessageH\x00\x42\x11\n\x0fpayload_variant\"5\n\nCompressed\x12\x19\n\x07portnum\x18\x01 \x01(\x0e\x32\x08.PortNum\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"V\n\x0cNeighborInfo\x12\x0f\n\x07node_id\x18\x01 \x01(\r\x12\x17\n\x0flast_sent_by_id\x18\x02 \x01(\r\x12\x1c\n\tneighbors\x18\x03 \x03(\x0b\x32\t.Neighbor\"(\n\x08Neighbor\x12\x0f\n\x07node_id\x18\x01 \x01(\r\x12\x0b\n\x03snr\x18\x02 \x01(\x02\"\x97\x02\n\x0e\x44\x65viceMetadata\x12\x18\n\x10\x66irmware_version\x18\x01 \x01(\t\x12\x1c\n\x14\x64\x65vice_state_version\x18\x02 \x01(\r\x12\x13\n\x0b\x63\x61nShutdown\x18\x03 \x01(\x08\x12\x0f\n\x07hasWifi\x18\x04 \x01(\x08\x12\x14\n\x0chasBluetooth\x18\x05 \x01(\x08\x12\x13\n\x0bhasEthernet\x18\x06 \x01(\x08\x12\'\n\x04role\x18\x07 \x01(\x0e\x32\x19.Config.DeviceConfig.Role\x12\x16\n\x0eposition_flags\x18\x08 \x01(\r\x12 \n\x08hw_model\x18\t \x01(\x0e\x32\x0e.HardwareModel\x12\x19\n\x11hasRemoteHardware\x18\n \x01(\x08*\xbe\x05\n\rHardwareModel\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08TLORA_V2\x10\x01\x12\x0c\n\x08TLORA_V1\x10\x02\x12\x12\n\x0eTLORA_V2_1_1P6\x10\x03\x12\t\n\x05TBEAM\x10\x04\x12\x0f\n\x0bHELTEC_V2_0\x10\x05\x12\x0e\n\nTBEAM_V0P7\x10\x06\x12\n\n\x06T_ECHO\x10\x07\x12\x10\n\x0cTLORA_V1_1P3\x10\x08\x12\x0b\n\x07RAK4631\x10\t\x12\x0f\n\x0bHELTEC_V2_1\x10\n\x12\r\n\tHELTEC_V1\x10\x0b\x12\x18\n\x14LILYGO_TBEAM_S3_CORE\x10\x0c\x12\x0c\n\x08RAK11200\x10\r\x12\x0b\n\x07NANO_G1\x10\x0e\x12\x12\n\x0eTLORA_V2_1_1P8\x10\x0f\x12\x0f\n\x0bTLORA_T3_S3\x10\x10\x12\x14\n\x10NANO_G1_EXPLORER\x10\x11\x12\x0e\n\nSTATION_G1\x10\x19\x12\x0c\n\x08RAK11310\x10\x1a\x12\x11\n\rLORA_RELAY_V1\x10 \x12\x0e\n\nNRF52840DK\x10!\x12\x07\n\x03PPR\x10\"\x12\x0f\n\x0bGENIEBLOCKS\x10#\x12\x11\n\rNRF52_UNKNOWN\x10$\x12\r\n\tPORTDUINO\x10%\x12\x0f\n\x0b\x41NDROID_SIM\x10&\x12\n\n\x06\x44IY_V1\x10\'\x12\x15\n\x11NRF52840_PCA10059\x10(\x12\n\n\x06\x44R_DEV\x10)\x12\x0b\n\x07M5STACK\x10*\x12\r\n\tHELTEC_V3\x10+\x12\x11\n\rHELTEC_WSL_V3\x10,\x12\x13\n\x0f\x42\x45TAFPV_2400_TX\x10-\x12\x17\n\x13\x42\x45TAFPV_900_NANO_TX\x10.\x12\x0c\n\x08RPI_PICO\x10/\x12\x1b\n\x17HELTEC_WIRELESS_TRACKER\x10\x30\x12\x19\n\x15HELTEC_WIRELESS_PAPER\x10\x31\x12\n\n\x06T_DECK\x10\x32\x12\x0e\n\nT_WATCH_S3\x10\x33\x12\x0f\n\nPRIVATE_HW\x10\xff\x01*,\n\tConstants\x12\x08\n\x04ZERO\x10\x00\x12\x15\n\x10\x44\x41TA_PAYLOAD_LEN\x10\xed\x01*\xee\x01\n\x11\x43riticalErrorCode\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0bTX_WATCHDOG\x10\x01\x12\x14\n\x10SLEEP_ENTER_WAIT\x10\x02\x12\x0c\n\x08NO_RADIO\x10\x03\x12\x0f\n\x0bUNSPECIFIED\x10\x04\x12\x15\n\x11UBLOX_UNIT_FAILED\x10\x05\x12\r\n\tNO_AXP192\x10\x06\x12\x19\n\x15INVALID_RADIO_SETTING\x10\x07\x12\x13\n\x0fTRANSMIT_FAILED\x10\x08\x12\x0c\n\x08\x42ROWNOUT\x10\t\x12\x12\n\x0eSX1262_FAILURE\x10\n\x12\x11\n\rRADIO_SPI_BUG\x10\x0b\x42_\n\x13\x63om.geeksville.meshB\nMeshProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_HARDWAREMODEL = DESCRIPTOR.enum_types_by_name['HardwareModel']
HardwareModel = enum_type_wrapper.EnumTypeWrapper(_HARDWAREMODEL)
_CONSTANTS = DESCRIPTOR.enum_types_by_name['Constants']
Constants = enum_type_wrapper.EnumTypeWrapper(_CONSTANTS)
_CRITICALERRORCODE = DESCRIPTOR.enum_types_by_name['CriticalErrorCode']
CriticalErrorCode = enum_type_wrapper.EnumTypeWrapper(_CRITICALERRORCODE)
UNSET = 0
TLORA_V2 = 1
TLORA_V1 = 2
TLORA_V2_1_1P6 = 3
TBEAM = 4
HELTEC_V2_0 = 5
TBEAM_V0P7 = 6
T_ECHO = 7
TLORA_V1_1P3 = 8
RAK4631 = 9
HELTEC_V2_1 = 10
HELTEC_V1 = 11
LILYGO_TBEAM_S3_CORE = 12
RAK11200 = 13
NANO_G1 = 14
TLORA_V2_1_1P8 = 15
TLORA_T3_S3 = 16
NANO_G1_EXPLORER = 17
STATION_G1 = 25
RAK11310 = 26
LORA_RELAY_V1 = 32
NRF52840DK = 33
PPR = 34
GENIEBLOCKS = 35
NRF52_UNKNOWN = 36
PORTDUINO = 37
ANDROID_SIM = 38
DIY_V1 = 39
NRF52840_PCA10059 = 40
DR_DEV = 41
M5STACK = 42
HELTEC_V3 = 43
HELTEC_WSL_V3 = 44
BETAFPV_2400_TX = 45
BETAFPV_900_NANO_TX = 46
RPI_PICO = 47
HELTEC_WIRELESS_TRACKER = 48
HELTEC_WIRELESS_PAPER = 49
T_DECK = 50
T_WATCH_S3 = 51
PRIVATE_HW = 255
ZERO = 0
DATA_PAYLOAD_LEN = 237
NONE = 0
TX_WATCHDOG = 1
SLEEP_ENTER_WAIT = 2
NO_RADIO = 3
UNSPECIFIED = 4
UBLOX_UNIT_FAILED = 5
NO_AXP192 = 6
INVALID_RADIO_SETTING = 7
TRANSMIT_FAILED = 8
BROWNOUT = 9
SX1262_FAILURE = 10
RADIO_SPI_BUG = 11


_POSITION = DESCRIPTOR.message_types_by_name['Position']
_USER = DESCRIPTOR.message_types_by_name['User']
_ROUTEDISCOVERY = DESCRIPTOR.message_types_by_name['RouteDiscovery']
_ROUTING = DESCRIPTOR.message_types_by_name['Routing']
_DATA = DESCRIPTOR.message_types_by_name['Data']
_WAYPOINT = DESCRIPTOR.message_types_by_name['Waypoint']
_MQTTCLIENTPROXYMESSAGE = DESCRIPTOR.message_types_by_name['MqttClientProxyMessage']
_MESHPACKET = DESCRIPTOR.message_types_by_name['MeshPacket']
_NODEINFO = DESCRIPTOR.message_types_by_name['NodeInfo']
_MYNODEINFO = DESCRIPTOR.message_types_by_name['MyNodeInfo']
_LOGRECORD = DESCRIPTOR.message_types_by_name['LogRecord']
_QUEUESTATUS = DESCRIPTOR.message_types_by_name['QueueStatus']
_FROMRADIO = DESCRIPTOR.message_types_by_name['FromRadio']
_TORADIO = DESCRIPTOR.message_types_by_name['ToRadio']
_COMPRESSED = DESCRIPTOR.message_types_by_name['Compressed']
_NEIGHBORINFO = DESCRIPTOR.message_types_by_name['NeighborInfo']
_NEIGHBOR = DESCRIPTOR.message_types_by_name['Neighbor']
_DEVICEMETADATA = DESCRIPTOR.message_types_by_name['DeviceMetadata']
_POSITION_LOCSOURCE = _POSITION.enum_types_by_name['LocSource']
_POSITION_ALTSOURCE = _POSITION.enum_types_by_name['AltSource']
_ROUTING_ERROR = _ROUTING.enum_types_by_name['Error']
_MESHPACKET_PRIORITY = _MESHPACKET.enum_types_by_name['Priority']
_MESHPACKET_DELAYED = _MESHPACKET.enum_types_by_name['Delayed']
_LOGRECORD_LEVEL = _LOGRECORD.enum_types_by_name['Level']
Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:Position)
  })
_sym_db.RegisterMessage(Position)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:User)
  })
_sym_db.RegisterMessage(User)

RouteDiscovery = _reflection.GeneratedProtocolMessageType('RouteDiscovery', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEDISCOVERY,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:RouteDiscovery)
  })
_sym_db.RegisterMessage(RouteDiscovery)

Routing = _reflection.GeneratedProtocolMessageType('Routing', (_message.Message,), {
  'DESCRIPTOR' : _ROUTING,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:Routing)
  })
_sym_db.RegisterMessage(Routing)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:Data)
  })
_sym_db.RegisterMessage(Data)

Waypoint = _reflection.GeneratedProtocolMessageType('Waypoint', (_message.Message,), {
  'DESCRIPTOR' : _WAYPOINT,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:Waypoint)
  })
_sym_db.RegisterMessage(Waypoint)

MqttClientProxyMessage = _reflection.GeneratedProtocolMessageType('MqttClientProxyMessage', (_message.Message,), {
  'DESCRIPTOR' : _MQTTCLIENTPROXYMESSAGE,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:MqttClientProxyMessage)
  })
_sym_db.RegisterMessage(MqttClientProxyMessage)

MeshPacket = _reflection.GeneratedProtocolMessageType('MeshPacket', (_message.Message,), {
  'DESCRIPTOR' : _MESHPACKET,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:MeshPacket)
  })
_sym_db.RegisterMessage(MeshPacket)

NodeInfo = _reflection.GeneratedProtocolMessageType('NodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _NODEINFO,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:NodeInfo)
  })
_sym_db.RegisterMessage(NodeInfo)

MyNodeInfo = _reflection.GeneratedProtocolMessageType('MyNodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _MYNODEINFO,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:MyNodeInfo)
  })
_sym_db.RegisterMessage(MyNodeInfo)

LogRecord = _reflection.GeneratedProtocolMessageType('LogRecord', (_message.Message,), {
  'DESCRIPTOR' : _LOGRECORD,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:LogRecord)
  })
_sym_db.RegisterMessage(LogRecord)

QueueStatus = _reflection.GeneratedProtocolMessageType('QueueStatus', (_message.Message,), {
  'DESCRIPTOR' : _QUEUESTATUS,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:QueueStatus)
  })
_sym_db.RegisterMessage(QueueStatus)

FromRadio = _reflection.GeneratedProtocolMessageType('FromRadio', (_message.Message,), {
  'DESCRIPTOR' : _FROMRADIO,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:FromRadio)
  })
_sym_db.RegisterMessage(FromRadio)

ToRadio = _reflection.GeneratedProtocolMessageType('ToRadio', (_message.Message,), {
  'DESCRIPTOR' : _TORADIO,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:ToRadio)
  })
_sym_db.RegisterMessage(ToRadio)

Compressed = _reflection.GeneratedProtocolMessageType('Compressed', (_message.Message,), {
  'DESCRIPTOR' : _COMPRESSED,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:Compressed)
  })
_sym_db.RegisterMessage(Compressed)

NeighborInfo = _reflection.GeneratedProtocolMessageType('NeighborInfo', (_message.Message,), {
  'DESCRIPTOR' : _NEIGHBORINFO,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:NeighborInfo)
  })
_sym_db.RegisterMessage(NeighborInfo)

Neighbor = _reflection.GeneratedProtocolMessageType('Neighbor', (_message.Message,), {
  'DESCRIPTOR' : _NEIGHBOR,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:Neighbor)
  })
_sym_db.RegisterMessage(Neighbor)

DeviceMetadata = _reflection.GeneratedProtocolMessageType('DeviceMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEMETADATA,
  '__module__' : 'meshtastic.mesh_pb2'
  # @@protoc_insertion_point(class_scope:DeviceMetadata)
  })
_sym_db.RegisterMessage(DeviceMetadata)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\nMeshProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _USER.fields_by_name['macaddr']._options = None
  _USER.fields_by_name['macaddr']._serialized_options = b'\030\001'
  _MYNODEINFO.fields_by_name['has_gps']._options = None
  _MYNODEINFO.fields_by_name['has_gps']._serialized_options = b'\030\001'
  _MYNODEINFO.fields_by_name['max_channels']._options = None
  _MYNODEINFO.fields_by_name['max_channels']._serialized_options = b'\030\001'
  _MYNODEINFO.fields_by_name['firmware_version']._options = None
  _MYNODEINFO.fields_by_name['firmware_version']._serialized_options = b'\030\001'
  _MYNODEINFO.fields_by_name['error_code']._options = None
  _MYNODEINFO.fields_by_name['error_code']._serialized_options = b'\030\001'
  _MYNODEINFO.fields_by_name['error_address']._options = None
  _MYNODEINFO.fields_by_name['error_address']._serialized_options = b'\030\001'
  _MYNODEINFO.fields_by_name['error_count']._options = None
  _MYNODEINFO.fields_by_name['error_count']._serialized_options = b'\030\001'
  _MYNODEINFO.fields_by_name['bitrate']._options = None
  _MYNODEINFO.fields_by_name['bitrate']._serialized_options = b'\030\001'
  _MYNODEINFO.fields_by_name['message_timeout_msec']._options = None
  _MYNODEINFO.fields_by_name['message_timeout_msec']._serialized_options = b'\030\001'
  _MYNODEINFO.fields_by_name['air_period_tx']._options = None
  _MYNODEINFO.fields_by_name['air_period_tx']._serialized_options = b'\030\001'
  _MYNODEINFO.fields_by_name['air_period_rx']._options = None
  _MYNODEINFO.fields_by_name['air_period_rx']._serialized_options = b'\030\001'
  _MYNODEINFO.fields_by_name['has_wifi']._options = None
  _MYNODEINFO.fields_by_name['has_wifi']._serialized_options = b'\030\001'
  _MYNODEINFO.fields_by_name['channel_utilization']._options = None
  _MYNODEINFO.fields_by_name['channel_utilization']._serialized_options = b'\030\001'
  _MYNODEINFO.fields_by_name['air_util_tx']._options = None
  _MYNODEINFO.fields_by_name['air_util_tx']._serialized_options = b'\030\001'
  _HARDWAREMODEL._serialized_start=4318
  _HARDWAREMODEL._serialized_end=5020
  _CONSTANTS._serialized_start=5022
  _CONSTANTS._serialized_end=5066
  _CRITICALERRORCODE._serialized_start=5069
  _CRITICALERRORCODE._serialized_end=5307
  _POSITION._serialized_start=189
  _POSITION._serialized_end=884
  _POSITION_LOCSOURCE._serialized_start=706
  _POSITION_LOCSOURCE._serialized_end=784
  _POSITION_ALTSOURCE._serialized_start=786
  _POSITION_ALTSOURCE._serialized_end=884
  _USER._serialized_start=887
  _USER._serialized_end=1020
  _ROUTEDISCOVERY._serialized_start=1022
  _ROUTEDISCOVERY._serialized_end=1053
  _ROUTING._serialized_start=1056
  _ROUTING._serialized_end=1403
  _ROUTING_ERROR._serialized_start=1190
  _ROUTING_ERROR._serialized_end=1392
  _DATA._serialized_start=1406
  _DATA._serialized_end=1562
  _WAYPOINT._serialized_start=1565
  _WAYPOINT._serialized_end=1712
  _MQTTCLIENTPROXYMESSAGE._serialized_start=1714
  _MQTTCLIENTPROXYMESSAGE._serialized_end=1822
  _MESHPACKET._serialized_start=1825
  _MESHPACKET._serialized_end=2284
  _MESHPACKET_PRIORITY._serialized_start=2106
  _MESHPACKET_PRIORITY._serialized_end=2197
  _MESHPACKET_DELAYED._serialized_start=2199
  _MESHPACKET_DELAYED._serialized_end=2265
  _NODEINFO._serialized_start=2287
  _NODEINFO._serialized_end=2450
  _MYNODEINFO._serialized_start=2453
  _MYNODEINFO._serialized_end=2895
  _LOGRECORD._serialized_start=2898
  _LOGRECORD._serialized_end=3079
  _LOGRECORD_LEVEL._serialized_start=2991
  _LOGRECORD_LEVEL._serialized_end=3079
  _QUEUESTATUS._serialized_start=3081
  _QUEUESTATUS._serialized_end=3161
  _FROMRADIO._serialized_start=3164
  _FROMRADIO._serialized_end=3646
  _TORADIO._serialized_start=3649
  _TORADIO._serialized_end=3848
  _COMPRESSED._serialized_start=3850
  _COMPRESSED._serialized_end=3903
  _NEIGHBORINFO._serialized_start=3905
  _NEIGHBORINFO._serialized_end=3991
  _NEIGHBOR._serialized_start=3993
  _NEIGHBOR._serialized_end=4033
  _DEVICEMETADATA._serialized_start=4036
  _DEVICEMETADATA._serialized_end=4315
# @@protoc_insertion_point(module_scope)
