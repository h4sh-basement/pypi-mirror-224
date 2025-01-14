# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: strmprivacy/api/entities/v1alpha/entities_v1alpha.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from strmprivacy.api.entities.v1 import entities_v1_pb2 as strmprivacy_dot_api_dot_entities_dot_v1_dot_entities__v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7strmprivacy/api/entities/v1alpha/entities_v1alpha.proto\x12 strmprivacy.api.entities.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\x1a-strmprivacy/api/entities/v1/entities_v1.proto\"\xc2\x02\n\x0bProjectPlan\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12#\n\x05title\x18\x02 \x01(\tB\r\xfa\x42\nr\x08\x10\x01\x18\xac\x02\xd0\x01\x01R\x05title\x12-\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x0b\xfa\x42\x08r\x06\x18\x88\'\xd0\x01\x01R\x0b\x64\x65scription\x12L\n\x0bitem_groups\x18\x04 \x03(\x0b\x32+.strmprivacy.api.entities.v1alpha.ItemGroupR\nitemGroups\x12\x37\n\x05users\x18\x05 \x03(\x0b\x32!.strmprivacy.api.entities.v1.UserR\x05users\x12\x1f\n\x0bis_template\x18\x06 \x01(\x08R\nisTemplate\x12\x18\n\x02id\x18\x07 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x02id\"\xdc\x07\n\tItemGroup\x12\x1d\n\x04name\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04\x10\x01\x18\x64R\x04name\x12-\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x0b\xfa\x42\x08r\x06\x18\x88\'\xd0\x01\x01R\x0b\x64\x65scription\x12L\n\ntodo_items\x18\x04 \x01(\x0b\x32+.strmprivacy.api.entities.v1alpha.TodoItemsH\x00R\ttodoItems\x12\x65\n\x13\x64\x61ta_contract_items\x18\x05 \x01(\x0b\x32\x33.strmprivacy.api.entities.v1alpha.DataContractItemsH\x00R\x11\x64\x61taContractItems\x12\\\n\x10info_asset_items\x18\x06 \x01(\x0b\x32\x30.strmprivacy.api.entities.v1alpha.InfoAssetItemsH\x00R\x0einfoAssetItems\x12X\n\x0e\x64ocument_items\x18\x07 \x01(\x0b\x32/.strmprivacy.api.entities.v1alpha.DocumentItemsH\x00R\rdocumentItems\x12X\n\x0epipeline_items\x18\x08 \x01(\x0b\x32/.strmprivacy.api.entities.v1alpha.PipelineItemsH\x00R\rpipelineItems\x12X\n\x0e\x66reeform_items\x18\n \x01(\x0b\x32/.strmprivacy.api.entities.v1alpha.FreeformItemsH\x00R\rfreeformItems\x12k\n\x15risk_assessment_items\x18\x0b \x01(\x0b\x32\x35.strmprivacy.api.entities.v1alpha.RiskAssessmentItemsH\x00R\x13riskAssessmentItems\x12k\n\x15risk_mitigation_items\x18\x0c \x01(\x0b\x32\x35.strmprivacy.api.entities.v1alpha.RiskMitigationItemsH\x00R\x13riskMitigationItems\x12[\n\x0frecording_items\x18\r \x01(\x0b\x32\x30.strmprivacy.api.entities.v1alpha.RecordingItemsH\x00R\x0erecordingItems\x12\x1b\n\x02id\x18\t \x01(\tB\x0b\xfa\x42\x08r\x06\xd0\x01\x01\xb0\x01\x01R\x02idB\x0c\n\x05items\x12\x03\xf8\x42\x01\"\x83\x03\n\x0eItemProperties\x12\x1b\n\x02id\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xd0\x01\x01\xb0\x01\x01R\x02id\x12?\n\rcreation_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0c\x63reationTime\x12\x35\n\x08\x64ue_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x64ueTime\x12\x43\n\x0f\x63ompletion_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0e\x63ompletionTime\x12;\n\x07\x63reator\x18\x05 \x01(\x0b\x32!.strmprivacy.api.entities.v1.UserR\x07\x63reator\x12=\n\x08\x61ssignee\x18\x06 \x01(\x0b\x32!.strmprivacy.api.entities.v1.UserR\x08\x61ssignee\x12\x1b\n\thelp_text\x18\x07 \x01(\tR\x08helpText\"\xeb\x01\n\tTodoItems\x12J\n\x05items\x18\x02 \x03(\x0b\x32\x34.strmprivacy.api.entities.v1alpha.TodoItems.TodoItemR\x05items\x1a\x91\x01\n\x08TodoItem\x12Y\n\x0fitem_properties\x18\x01 \x01(\x0b\x32\x30.strmprivacy.api.entities.v1alpha.ItemPropertiesR\x0eitemProperties\x12*\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x08\xfa\x42\x05r\x03\x18\x88\'R\x0b\x64\x65scription\"\xa9\x02\n\x11\x44\x61taContractItems\x12Z\n\x05items\x18\x01 \x03(\x0b\x32\x44.strmprivacy.api.entities.v1alpha.DataContractItems.DataContractItemR\x05items\x1a\xb7\x01\n\x10\x44\x61taContractItem\x12Y\n\x0fitem_properties\x18\x01 \x01(\x0b\x32\x30.strmprivacy.api.entities.v1alpha.ItemPropertiesR\x0eitemProperties\x12H\n\x03ref\x18\x02 \x01(\x0b\x32,.strmprivacy.api.entities.v1.DataContractRefB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x03ref\"\xc2\x05\n\x0eInfoAssetItems\x12T\n\x05items\x18\x01 \x03(\x0b\x32>.strmprivacy.api.entities.v1alpha.InfoAssetItems.InfoAssetItemR\x05items\x1a\xd9\x04\n\rInfoAssetItem\x12Y\n\x0fitem_properties\x18\x01 \x01(\x0b\x32\x30.strmprivacy.api.entities.v1alpha.ItemPropertiesR\x0eitemProperties\x12\x1c\n\x04name\x18\x02 \x01(\tB\x08\xfa\x42\x05r\x03\x18\xac\x02R\x04name\x12_\n\x05state\x18\x03 \x01(\x0e\x32\x44.strmprivacy.api.entities.v1alpha.InfoAssetItems.InfoAssetItem.StateB\x03\xe0\x41\x03R\x05state\x12u\n\x0e\x63lassification\x18\x04 \x01(\x0b\x32M.strmprivacy.api.entities.v1alpha.InfoAssetItems.InfoAssetItem.ClassificationR\x0e\x63lassification\x12J\n\ninfo_asset\x18\x05 \x01(\x0b\x32+.strmprivacy.api.entities.v1alpha.InfoAssetR\tinfoAsset\x1a\x63\n\x0e\x43lassification\x12\x1c\n\x04name\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\x18\xac\x02R\x04name\x12\x1b\n\tcolor_css\x18\x02 \x01(\tR\x08\x63olorCss\x12\x16\n\x06points\x18\x04 \x01(\x05R\x06points\"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\t\n\x05\x44RAFT\x10\x01\x12\r\n\tIN_REVIEW\x10\x02\x12\x0c\n\x08\x41PPROVED\x10\x03\"\xfd\x01\n\rDocumentItems\x12R\n\x05items\x18\x01 \x03(\x0b\x32<.strmprivacy.api.entities.v1alpha.DocumentItems.DocumentItemR\x05items\x1a\x97\x01\n\x0c\x44ocumentItem\x12Y\n\x0fitem_properties\x18\x01 \x01(\x0b\x32\x30.strmprivacy.api.entities.v1alpha.ItemPropertiesR\x0eitemProperties\x12\x1a\n\x08\x66ilename\x18\x02 \x01(\tR\x08\x66ilename\x12\x10\n\x03uri\x18\x03 \x01(\tR\x03uri\"\xeb\x02\n\rPipelineItems\x12R\n\x05items\x18\x02 \x03(\x0b\x32<.strmprivacy.api.entities.v1alpha.PipelineItems.PipelineItemR\x05items\x1a\x85\x02\n\x0cPipelineItem\x12Y\n\x0fitem_properties\x18\x01 \x01(\x0b\x32\x30.strmprivacy.api.entities.v1alpha.ItemPropertiesR\x0eitemProperties\x12@\n\x06stream\x18\x02 \x01(\x0b\x32&.strmprivacy.api.entities.v1.StreamRefH\x00R\x06stream\x12G\n\tbatch_job\x18\x03 \x01(\x0b\x32(.strmprivacy.api.entities.v1.BatchJobRefH\x00R\x08\x62\x61tchJobB\x0f\n\x08pipeline\x12\x03\xf8\x42\x01\"\x8b\x02\n\rFreeformItems\x12J\n\x05items\x18\x02 \x03(\x0b\x32\x34.strmprivacy.api.entities.v1alpha.FreeformItems.ItemR\x05items\x1a\xad\x01\n\x04Item\x12Y\n\x0fitem_properties\x18\x01 \x01(\x0b\x32\x30.strmprivacy.api.entities.v1alpha.ItemPropertiesR\x0eitemProperties\x12\x1a\n\x08question\x18\x02 \x01(\tR\x08question\x12\x16\n\x06\x61nswer\x18\x03 \x01(\tR\x06\x61nswer\x12\x16\n\x06remark\x18\x04 \x01(\tR\x06remark\"\xd0\x02\n\x13RiskAssessmentItems\x12P\n\x05items\x18\x02 \x03(\x0b\x32:.strmprivacy.api.entities.v1alpha.RiskAssessmentItems.ItemR\x05items\x1a\xe6\x01\n\x04Item\x12Y\n\x0fitem_properties\x18\x01 \x01(\x0b\x32\x30.strmprivacy.api.entities.v1alpha.ItemPropertiesR\x0eitemProperties\x12\x12\n\x04risk\x18\x02 \x01(\tR\x04risk\x12\'\n\x0fharm_likelihood\x18\x03 \x01(\tR\x0eharmLikelihood\x12#\n\rharm_severity\x18\x04 \x01(\tR\x0charmSeverity\x12!\n\x0coverall_risk\x18\x05 \x01(\tR\x0boverallRisk\"\xf2\x02\n\x13RiskMitigationItems\x12P\n\x05items\x18\x02 \x03(\x0b\x32:.strmprivacy.api.entities.v1alpha.RiskMitigationItems.ItemR\x05items\x1a\x88\x02\n\x04Item\x12Y\n\x0fitem_properties\x18\x01 \x01(\x0b\x32\x30.strmprivacy.api.entities.v1alpha.ItemPropertiesR\x0eitemProperties\x12\x12\n\x04risk\x18\x02 \x01(\tR\x04risk\x12!\n\x0coverall_risk\x18\x03 \x01(\tR\x0boverallRisk\x12-\n\x12mitigation_measure\x18\x05 \x01(\tR\x11mitigationMeasure\x12#\n\rresidual_risk\x18\x06 \x01(\tR\x0cresidualRisk\x12\x1a\n\x08\x61pproval\x18\x07 \x01(\tR\x08\x61pproval\"\xfb\x01\n\x0eRecordingItems\x12K\n\x05items\x18\x02 \x03(\x0b\x32\x35.strmprivacy.api.entities.v1alpha.RecordingItems.ItemR\x05items\x1a\x9b\x01\n\x04Item\x12Y\n\x0fitem_properties\x18\x01 \x01(\x0b\x32\x30.strmprivacy.api.entities.v1alpha.ItemPropertiesR\x0eitemProperties\x12\x1e\n\nparticular\x18\x02 \x01(\tR\nparticular\x12\x18\n\x07remarks\x18\x04 \x01(\tR\x07remarks\"\xfd\x07\n\tInfoAsset\x12\x1a\n\x08template\x18\x01 \x01(\tR\x08template\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x18\n\x07\x65mbargo\x18\x03 \x01(\x08R\x07\x65mbargo\x12k\n\x10\x62usiness_impacts\x18\x04 \x03(\x0b\x32@.strmprivacy.api.entities.v1alpha.InfoAsset.BusinessImpactRatingR\x0f\x62usinessImpacts\x12\'\n\x0fsecurity_levels\x18\x05 \x03(\tR\x0esecurityLevels\x12%\n\x0esecurity_level\x18\x06 \x01(\tR\rsecurityLevel\x12O\n\x08sections\x18\x07 \x03(\x0b\x32\x33.strmprivacy.api.entities.v1alpha.InfoAsset.SectionR\x08sections\x12\x1f\n\x0bis_template\x18\x08 \x01(\x08R\nisTemplate\x1ax\n\x07Section\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12Y\n\x0csub_sections\x18\x02 \x03(\x0b\x32\x36.strmprivacy.api.entities.v1alpha.InfoAsset.SubSectionR\x0bsubSections\x1a\xaf\x01\n\nSubSection\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12 \n\x0b\x65xplanation\x18\x03 \x01(\tR\x0b\x65xplanation\x12I\n\x06\x63hecks\x18\x04 \x03(\x0b\x32\x31.strmprivacy.api.entities.v1alpha.InfoAsset.CheckR\x06\x63hecks\x1aV\n\x05\x43heck\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0b\x64\x65tail_info\x18\x02 \x01(\tR\ndetailInfo\x12\x18\n\x07\x63hecked\x18\x03 \x01(\x08R\x07\x63hecked\x1a\x8c\x01\n\x14\x42usinessImpactRating\x12\x14\n\x05label\x18\x01 \x01(\tR\x05label\x12^\n\x08\x63\x61tegory\x18\x02 \x01(\x0b\x32\x42.strmprivacy.api.entities.v1alpha.InfoAsset.BusinessImpactCategoryR\x08\x63\x61tegory\x1a\x64\n\x16\x42usinessImpactCategory\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x14\n\x05value\x18\x03 \x01(\x02R\x05valueBs\n#io.strmprivacy.api.entities.v1alphaP\x01ZJgithub.com/strmprivacy/api-definitions-go/v3/api/entities/v1alpha;entitiesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'strmprivacy.api.entities.v1alpha.entities_v1alpha_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#io.strmprivacy.api.entities.v1alphaP\001ZJgithub.com/strmprivacy/api-definitions-go/v3/api/entities/v1alpha;entities'
  _PROJECTPLAN.fields_by_name['title']._options = None
  _PROJECTPLAN.fields_by_name['title']._serialized_options = b'\372B\nr\010\020\001\030\254\002\320\001\001'
  _PROJECTPLAN.fields_by_name['description']._options = None
  _PROJECTPLAN.fields_by_name['description']._serialized_options = b'\372B\010r\006\030\210\'\320\001\001'
  _PROJECTPLAN.fields_by_name['id']._options = None
  _PROJECTPLAN.fields_by_name['id']._serialized_options = b'\372B\005r\003\260\001\001'
  _ITEMGROUP.oneofs_by_name['items']._options = None
  _ITEMGROUP.oneofs_by_name['items']._serialized_options = b'\370B\001'
  _ITEMGROUP.fields_by_name['name']._options = None
  _ITEMGROUP.fields_by_name['name']._serialized_options = b'\372B\006r\004\020\001\030d'
  _ITEMGROUP.fields_by_name['description']._options = None
  _ITEMGROUP.fields_by_name['description']._serialized_options = b'\372B\010r\006\030\210\'\320\001\001'
  _ITEMGROUP.fields_by_name['id']._options = None
  _ITEMGROUP.fields_by_name['id']._serialized_options = b'\372B\010r\006\320\001\001\260\001\001'
  _ITEMPROPERTIES.fields_by_name['id']._options = None
  _ITEMPROPERTIES.fields_by_name['id']._serialized_options = b'\372B\010r\006\320\001\001\260\001\001'
  _TODOITEMS_TODOITEM.fields_by_name['description']._options = None
  _TODOITEMS_TODOITEM.fields_by_name['description']._serialized_options = b'\372B\005r\003\030\210\''
  _DATACONTRACTITEMS_DATACONTRACTITEM.fields_by_name['ref']._options = None
  _DATACONTRACTITEMS_DATACONTRACTITEM.fields_by_name['ref']._serialized_options = b'\372B\005\212\001\002\020\001'
  _INFOASSETITEMS_INFOASSETITEM_CLASSIFICATION.fields_by_name['name']._options = None
  _INFOASSETITEMS_INFOASSETITEM_CLASSIFICATION.fields_by_name['name']._serialized_options = b'\372B\005r\003\030\254\002'
  _INFOASSETITEMS_INFOASSETITEM.fields_by_name['name']._options = None
  _INFOASSETITEMS_INFOASSETITEM.fields_by_name['name']._serialized_options = b'\372B\005r\003\030\254\002'
  _INFOASSETITEMS_INFOASSETITEM.fields_by_name['state']._options = None
  _INFOASSETITEMS_INFOASSETITEM.fields_by_name['state']._serialized_options = b'\340A\003'
  _PIPELINEITEMS_PIPELINEITEM.oneofs_by_name['pipeline']._options = None
  _PIPELINEITEMS_PIPELINEITEM.oneofs_by_name['pipeline']._serialized_options = b'\370B\001'
  _PROJECTPLAN._serialized_start=232
  _PROJECTPLAN._serialized_end=554
  _ITEMGROUP._serialized_start=557
  _ITEMGROUP._serialized_end=1545
  _ITEMPROPERTIES._serialized_start=1548
  _ITEMPROPERTIES._serialized_end=1935
  _TODOITEMS._serialized_start=1938
  _TODOITEMS._serialized_end=2173
  _TODOITEMS_TODOITEM._serialized_start=2028
  _TODOITEMS_TODOITEM._serialized_end=2173
  _DATACONTRACTITEMS._serialized_start=2176
  _DATACONTRACTITEMS._serialized_end=2473
  _DATACONTRACTITEMS_DATACONTRACTITEM._serialized_start=2290
  _DATACONTRACTITEMS_DATACONTRACTITEM._serialized_end=2473
  _INFOASSETITEMS._serialized_start=2476
  _INFOASSETITEMS._serialized_end=3182
  _INFOASSETITEMS_INFOASSETITEM._serialized_start=2581
  _INFOASSETITEMS_INFOASSETITEM._serialized_end=3182
  _INFOASSETITEMS_INFOASSETITEM_CLASSIFICATION._serialized_start=3011
  _INFOASSETITEMS_INFOASSETITEM_CLASSIFICATION._serialized_end=3110
  _INFOASSETITEMS_INFOASSETITEM_STATE._serialized_start=3112
  _INFOASSETITEMS_INFOASSETITEM_STATE._serialized_end=3182
  _DOCUMENTITEMS._serialized_start=3185
  _DOCUMENTITEMS._serialized_end=3438
  _DOCUMENTITEMS_DOCUMENTITEM._serialized_start=3287
  _DOCUMENTITEMS_DOCUMENTITEM._serialized_end=3438
  _PIPELINEITEMS._serialized_start=3441
  _PIPELINEITEMS._serialized_end=3804
  _PIPELINEITEMS_PIPELINEITEM._serialized_start=3543
  _PIPELINEITEMS_PIPELINEITEM._serialized_end=3804
  _FREEFORMITEMS._serialized_start=3807
  _FREEFORMITEMS._serialized_end=4074
  _FREEFORMITEMS_ITEM._serialized_start=3901
  _FREEFORMITEMS_ITEM._serialized_end=4074
  _RISKASSESSMENTITEMS._serialized_start=4077
  _RISKASSESSMENTITEMS._serialized_end=4413
  _RISKASSESSMENTITEMS_ITEM._serialized_start=4183
  _RISKASSESSMENTITEMS_ITEM._serialized_end=4413
  _RISKMITIGATIONITEMS._serialized_start=4416
  _RISKMITIGATIONITEMS._serialized_end=4786
  _RISKMITIGATIONITEMS_ITEM._serialized_start=4522
  _RISKMITIGATIONITEMS_ITEM._serialized_end=4786
  _RECORDINGITEMS._serialized_start=4789
  _RECORDINGITEMS._serialized_end=5040
  _RECORDINGITEMS_ITEM._serialized_start=4885
  _RECORDINGITEMS_ITEM._serialized_end=5040
  _INFOASSET._serialized_start=5043
  _INFOASSET._serialized_end=6064
  _INFOASSET_SECTION._serialized_start=5433
  _INFOASSET_SECTION._serialized_end=5553
  _INFOASSET_SUBSECTION._serialized_start=5556
  _INFOASSET_SUBSECTION._serialized_end=5731
  _INFOASSET_CHECK._serialized_start=5733
  _INFOASSET_CHECK._serialized_end=5819
  _INFOASSET_BUSINESSIMPACTRATING._serialized_start=5822
  _INFOASSET_BUSINESSIMPACTRATING._serialized_end=5962
  _INFOASSET_BUSINESSIMPACTCATEGORY._serialized_start=5964
  _INFOASSET_BUSINESSIMPACTCATEGORY._serialized_end=6064
# @@protoc_insertion_point(module_scope)
