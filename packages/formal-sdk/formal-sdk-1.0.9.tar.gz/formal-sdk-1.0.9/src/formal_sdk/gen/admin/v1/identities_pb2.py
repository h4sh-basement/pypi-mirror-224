# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin/v1/identities.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .types.v1 import external_id_pb2 as admin_dot_v1_dot_types_dot_v1_dot_external__id__pb2
from .types.v1 import group_pb2 as admin_dot_v1_dot_types_dot_v1_dot_group__pb2
from .types.v1 import user_pb2 as admin_dot_v1_dot_types_dot_v1_dot_user__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61\x64min/v1/identities.proto\x12\x08\x61\x64min.v1\x1a#admin/v1/types/v1/external_id.proto\x1a\x1d\x61\x64min/v1/types/v1/group.proto\x1a\x1c\x61\x64min/v1/types/v1/user.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"Y\n\x10GetGroupsRequest\x12\x14\n\x05limit\x18\x01 \x01(\x05R\x05limit\x12\x16\n\x06\x63ursor\x18\x02 \x01(\tR\x06\x63ursor\x12\x17\n\x07go_back\x18\x03 \x01(\x08R\x06goBack\"J\n\x12\x43reateGroupRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"%\n\x13GetGroupByIdRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"$\n\x12\x44\x65leteGroupRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"Z\n\x12UpdateGroupRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\"D\n\x17LinkUsersToGroupRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x19\n\x08user_ids\x18\x02 \x03(\tR\x07userIds\"H\n\x1bUnlinkUsersFromGroupRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x19\n\x08user_ids\x18\x02 \x03(\tR\x07userIds\"E\n\x13\x43reateGroupResponse\x12.\n\x05group\x18\x01 \x01(\x0b\x32\x18.admin.v1.types.v1.GroupR\x05group\"F\n\x14GetGroupByIdResponse\x12.\n\x05group\x18\x01 \x01(\x0b\x32\x18.admin.v1.types.v1.GroupR\x05group\"E\n\x13\x44\x65leteGroupResponse\x12.\n\x05group\x18\x01 \x01(\x0b\x32\x18.admin.v1.types.v1.GroupR\x05group\"E\n\x13UpdateGroupResponse\x12.\n\x05group\x18\x01 \x01(\x0b\x32\x18.admin.v1.types.v1.GroupR\x05group\"\x8e\x01\n\x11GetGroupsResponse\x12\x30\n\x06groups\x18\x01 \x03(\x0b\x32\x18.admin.v1.types.v1.GroupR\x06groups\x12,\n\x12last_evaluated_key\x18\x02 \x01(\tR\x10lastEvaluatedKey\x12\x19\n\x08has_more\x18\x03 \x01(\x08R\x07hasMore\"P\n\x18LinkUsersToGroupResponse\x12\x19\n\x08user_ids\x18\x01 \x03(\tR\x07userIds\x12\x19\n\x08group_id\x18\x02 \x01(\tR\x07groupId\"T\n\x1cUnlinkUsersFromGroupResponse\x12\x19\n\x08user_ids\x18\x01 \x03(\tR\x07userIds\x12\x19\n\x08group_id\x18\x02 \x01(\tR\x07groupId\"M\n\x15UserLinkGroupResponse\x12\x19\n\x08user_ids\x18\x01 \x03(\tR\x07userIds\x12\x19\n\x08group_id\x18\x02 \x01(\tR\x07groupId\"X\n\x0fGetUsersRequest\x12\x14\n\x05limit\x18\x01 \x01(\tR\x05limit\x12\x16\n\x06\x63ursor\x18\x02 \x01(\tR\x06\x63ursor\x12\x17\n\x07go_back\x18\x03 \x01(\x08R\x06goBack\"\x8a\x01\n\x10GetUsersResponse\x12-\n\x05users\x18\x01 \x03(\x0b\x32\x17.admin.v1.types.v1.UserR\x05users\x12,\n\x12last_evaluated_key\x18\x02 \x01(\tR\x10lastEvaluatedKey\x12\x19\n\x08has_more\x18\x03 \x01(\x08R\x07hasMore\"\xb8\x02\n\x11\x43reateUserRequest\x12\x1d\n\nfirst_name\x18\x01 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x02 \x01(\tR\x08lastName\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\x12\x19\n\x08\x61pp_type\x18\x04 \x01(\tR\x07\x61ppType\x12\x15\n\x06\x61pp_id\x18\x05 \x01(\tR\x05\x61ppId\x12\x12\n\x04name\x18\x06 \x01(\tR\x04name\x12\x14\n\x05\x65mail\x18\x07 \x01(\tR\x05\x65mail\x12\x14\n\x05\x61\x64min\x18\x08 \x01(\x08R\x05\x61\x64min\x12\x10\n\x03idp\x18\t \x01(\tR\x03idp\x12\x16\n\x06status\x18\n \x01(\tR\x06status\x12\x37\n\texpire_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x08\x65xpireAt\"^\n\x12\x43reateUserResponse\x12+\n\x04user\x18\x01 \x01(\x0b\x32\x17.admin.v1.types.v1.UserR\x04user\x12\x1b\n\ttenant_id\x18\x02 \x01(\tR\x08tenantId\"$\n\x12GetUserByIdRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"B\n\x13GetUserByIdResponse\x12+\n\x04user\x18\x01 \x01(\x0b\x32\x17.admin.v1.types.v1.UserR\x04user\"#\n\x11\x44\x65leteUserRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x14\n\x12\x44\x65leteUserResponse\"\x89\x01\n\x11UpdateUserRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1d\n\nfirst_name\x18\x03 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x04 \x01(\tR\x08lastName\x12\x14\n\x05\x65mail\x18\x05 \x01(\tR\x05\x65mail\"\x14\n\x12UpdateUserResponse\"0\n\x1eGetMachineUserAuthTokenRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"S\n\x1fGetMachineUserAuthTokenResponse\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\x12\x1a\n\x08username\x18\x02 \x01(\tR\x08username\"4\n\"RefreshMachineUserAuthTokenRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"W\n#RefreshMachineUserAuthTokenResponse\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\x12\x1a\n\x08username\x18\x02 \x01(\tR\x08username\"+\n\x19GetUserExternalIdsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"^\n\x1aGetUserExternalIdsResponse\x12@\n\x0c\x65xternal_ids\x18\x01 \x03(\x0b\x32\x1d.admin.v1.types.v1.ExternalIdR\x0b\x65xternalIds\"\x8f\x01\n\x1aMapUserToExternalIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1f\n\x0b\x65xternal_id\x18\x02 \x01(\tR\nexternalId\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x15\n\x06\x61pp_id\x18\x04 \x01(\tR\x05\x61ppId\"\x1d\n\x1bMapUserToExternalIdResponse\"?\n\x1e\x44\x65leteExternalIdMappingRequest\x12\x1d\n\nmapping_id\x18\x01 \x01(\tR\tmappingId\"!\n\x1f\x44\x65leteExternalIdMappingResponse2\x98\x07\n\x0bUserService\x12\x41\n\x08GetUsers\x12\x19.admin.v1.GetUsersRequest\x1a\x1a.admin.v1.GetUsersResponse\x12G\n\nCreateUser\x12\x1b.admin.v1.CreateUserRequest\x1a\x1c.admin.v1.CreateUserResponse\x12J\n\x0bGetUserById\x12\x1c.admin.v1.GetUserByIdRequest\x1a\x1d.admin.v1.GetUserByIdResponse\x12G\n\nDeleteUser\x12\x1b.admin.v1.DeleteUserRequest\x1a\x1c.admin.v1.DeleteUserResponse\x12G\n\nUpdateUser\x12\x1b.admin.v1.UpdateUserRequest\x1a\x1c.admin.v1.UpdateUserResponse\x12n\n\x17GetMachineUserAuthToken\x12(.admin.v1.GetMachineUserAuthTokenRequest\x1a).admin.v1.GetMachineUserAuthTokenResponse\x12z\n\x1bRefreshMachineUserAuthToken\x12,.admin.v1.RefreshMachineUserAuthTokenRequest\x1a-.admin.v1.RefreshMachineUserAuthTokenResponse\x12_\n\x12GetUserExternalIds\x12#.admin.v1.GetUserExternalIdsRequest\x1a$.admin.v1.GetUserExternalIdsResponse\x12\x62\n\x13MapUserToExternalId\x12$.admin.v1.MapUserToExternalIdRequest\x1a%.admin.v1.MapUserToExternalIdResponse\x12n\n\x17\x44\x65leteExternalIdMapping\x12(.admin.v1.DeleteExternalIdMappingRequest\x1a).admin.v1.DeleteExternalIdMappingResponse2\xc9\x04\n\x0cGroupService\x12J\n\x0b\x43reateGroup\x12\x1c.admin.v1.CreateGroupRequest\x1a\x1d.admin.v1.CreateGroupResponse\x12\x44\n\tGetGroups\x12\x1a.admin.v1.GetGroupsRequest\x1a\x1b.admin.v1.GetGroupsResponse\x12M\n\x0cGetGroupById\x12\x1d.admin.v1.GetGroupByIdRequest\x1a\x1e.admin.v1.GetGroupByIdResponse\x12J\n\x0bUpdateGroup\x12\x1c.admin.v1.UpdateGroupRequest\x1a\x1d.admin.v1.UpdateGroupResponse\x12Y\n\x10LinkUsersToGroup\x12!.admin.v1.LinkUsersToGroupRequest\x1a\".admin.v1.LinkUsersToGroupResponse\x12\x65\n\x14UnlinkUsersFromGroup\x12%.admin.v1.UnlinkUsersFromGroupRequest\x1a&.admin.v1.UnlinkUsersFromGroupResponse\x12J\n\x0b\x44\x65leteGroup\x12\x1c.admin.v1.DeleteGroupRequest\x1a\x1d.admin.v1.DeleteGroupResponseB\xaa\x01\n\x0c\x63om.admin.v1B\x0fIdentitiesProtoP\x01ZHgithub.com/formalco/control-plane/backend/admin-api/gen/admin/v1;adminv1\xa2\x02\x03\x41XX\xaa\x02\x08\x41\x64min.V1\xca\x02\x08\x41\x64min\\V1\xe2\x02\x14\x41\x64min\\V1\\GPBMetadata\xea\x02\tAdmin::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'admin.v1.identities_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\014com.admin.v1B\017IdentitiesProtoP\001ZHgithub.com/formalco/control-plane/backend/admin-api/gen/admin/v1;adminv1\242\002\003AXX\252\002\010Admin.V1\312\002\010Admin\\V1\342\002\024Admin\\V1\\GPBMetadata\352\002\tAdmin::V1'
  _globals['_GETGROUPSREQUEST']._serialized_start=170
  _globals['_GETGROUPSREQUEST']._serialized_end=259
  _globals['_CREATEGROUPREQUEST']._serialized_start=261
  _globals['_CREATEGROUPREQUEST']._serialized_end=335
  _globals['_GETGROUPBYIDREQUEST']._serialized_start=337
  _globals['_GETGROUPBYIDREQUEST']._serialized_end=374
  _globals['_DELETEGROUPREQUEST']._serialized_start=376
  _globals['_DELETEGROUPREQUEST']._serialized_end=412
  _globals['_UPDATEGROUPREQUEST']._serialized_start=414
  _globals['_UPDATEGROUPREQUEST']._serialized_end=504
  _globals['_LINKUSERSTOGROUPREQUEST']._serialized_start=506
  _globals['_LINKUSERSTOGROUPREQUEST']._serialized_end=574
  _globals['_UNLINKUSERSFROMGROUPREQUEST']._serialized_start=576
  _globals['_UNLINKUSERSFROMGROUPREQUEST']._serialized_end=648
  _globals['_CREATEGROUPRESPONSE']._serialized_start=650
  _globals['_CREATEGROUPRESPONSE']._serialized_end=719
  _globals['_GETGROUPBYIDRESPONSE']._serialized_start=721
  _globals['_GETGROUPBYIDRESPONSE']._serialized_end=791
  _globals['_DELETEGROUPRESPONSE']._serialized_start=793
  _globals['_DELETEGROUPRESPONSE']._serialized_end=862
  _globals['_UPDATEGROUPRESPONSE']._serialized_start=864
  _globals['_UPDATEGROUPRESPONSE']._serialized_end=933
  _globals['_GETGROUPSRESPONSE']._serialized_start=936
  _globals['_GETGROUPSRESPONSE']._serialized_end=1078
  _globals['_LINKUSERSTOGROUPRESPONSE']._serialized_start=1080
  _globals['_LINKUSERSTOGROUPRESPONSE']._serialized_end=1160
  _globals['_UNLINKUSERSFROMGROUPRESPONSE']._serialized_start=1162
  _globals['_UNLINKUSERSFROMGROUPRESPONSE']._serialized_end=1246
  _globals['_USERLINKGROUPRESPONSE']._serialized_start=1248
  _globals['_USERLINKGROUPRESPONSE']._serialized_end=1325
  _globals['_GETUSERSREQUEST']._serialized_start=1327
  _globals['_GETUSERSREQUEST']._serialized_end=1415
  _globals['_GETUSERSRESPONSE']._serialized_start=1418
  _globals['_GETUSERSRESPONSE']._serialized_end=1556
  _globals['_CREATEUSERREQUEST']._serialized_start=1559
  _globals['_CREATEUSERREQUEST']._serialized_end=1871
  _globals['_CREATEUSERRESPONSE']._serialized_start=1873
  _globals['_CREATEUSERRESPONSE']._serialized_end=1967
  _globals['_GETUSERBYIDREQUEST']._serialized_start=1969
  _globals['_GETUSERBYIDREQUEST']._serialized_end=2005
  _globals['_GETUSERBYIDRESPONSE']._serialized_start=2007
  _globals['_GETUSERBYIDRESPONSE']._serialized_end=2073
  _globals['_DELETEUSERREQUEST']._serialized_start=2075
  _globals['_DELETEUSERREQUEST']._serialized_end=2110
  _globals['_DELETEUSERRESPONSE']._serialized_start=2112
  _globals['_DELETEUSERRESPONSE']._serialized_end=2132
  _globals['_UPDATEUSERREQUEST']._serialized_start=2135
  _globals['_UPDATEUSERREQUEST']._serialized_end=2272
  _globals['_UPDATEUSERRESPONSE']._serialized_start=2274
  _globals['_UPDATEUSERRESPONSE']._serialized_end=2294
  _globals['_GETMACHINEUSERAUTHTOKENREQUEST']._serialized_start=2296
  _globals['_GETMACHINEUSERAUTHTOKENREQUEST']._serialized_end=2344
  _globals['_GETMACHINEUSERAUTHTOKENRESPONSE']._serialized_start=2346
  _globals['_GETMACHINEUSERAUTHTOKENRESPONSE']._serialized_end=2429
  _globals['_REFRESHMACHINEUSERAUTHTOKENREQUEST']._serialized_start=2431
  _globals['_REFRESHMACHINEUSERAUTHTOKENREQUEST']._serialized_end=2483
  _globals['_REFRESHMACHINEUSERAUTHTOKENRESPONSE']._serialized_start=2485
  _globals['_REFRESHMACHINEUSERAUTHTOKENRESPONSE']._serialized_end=2572
  _globals['_GETUSEREXTERNALIDSREQUEST']._serialized_start=2574
  _globals['_GETUSEREXTERNALIDSREQUEST']._serialized_end=2617
  _globals['_GETUSEREXTERNALIDSRESPONSE']._serialized_start=2619
  _globals['_GETUSEREXTERNALIDSRESPONSE']._serialized_end=2713
  _globals['_MAPUSERTOEXTERNALIDREQUEST']._serialized_start=2716
  _globals['_MAPUSERTOEXTERNALIDREQUEST']._serialized_end=2859
  _globals['_MAPUSERTOEXTERNALIDRESPONSE']._serialized_start=2861
  _globals['_MAPUSERTOEXTERNALIDRESPONSE']._serialized_end=2890
  _globals['_DELETEEXTERNALIDMAPPINGREQUEST']._serialized_start=2892
  _globals['_DELETEEXTERNALIDMAPPINGREQUEST']._serialized_end=2955
  _globals['_DELETEEXTERNALIDMAPPINGRESPONSE']._serialized_start=2957
  _globals['_DELETEEXTERNALIDMAPPINGRESPONSE']._serialized_end=2990
  _globals['_USERSERVICE']._serialized_start=2993
  _globals['_USERSERVICE']._serialized_end=3913
  _globals['_GROUPSERVICE']._serialized_start=3916
  _globals['_GROUPSERVICE']._serialized_end=4501
# @@protoc_insertion_point(module_scope)
