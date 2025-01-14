# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/l10n/localization_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.annotations import scope_pb2 as eolymp_dot_annotations_dot_scope__pb2
from eolymp.l10n import term_pb2 as eolymp_dot_l10n_dot_term__pb2
from eolymp.l10n import translation_pb2 as eolymp_dot_l10n_dot_translation__pb2
from eolymp.wellknown import expression_pb2 as eolymp_dot_wellknown_dot_expression__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&eolymp/l10n/localization_service.proto\x12\x0b\x65olymp.l10n\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a\x16\x65olymp/l10n/term.proto\x1a\x1d\x65olymp/l10n/translation.proto\x1a!eolymp/wellknown/expression.proto\"2\n\x0f\x43reateTermInput\x12\x1f\n\x04term\x18\x01 \x01(\x0b\x32\x11.eolymp.l10n.Term\"#\n\x10\x43reateTermOutput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\"4\n\x10ImportTermsInput\x12 \n\x05terms\x18\x01 \x03(\x0b\x32\x11.eolymp.l10n.Term\"[\n\x11ImportTermsOutput\x12\x15\n\rcreated_count\x18\x01 \x01(\x05\x12\x15\n\rupdated_count\x18\x02 \x01(\x05\x12\x18\n\x10\x64\x65precated_count\x18\x03 \x01(\x05\"\xe4\x03\n\x0eListTermsInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12\x33\n\x07\x66ilters\x18( \x01(\x0b\x32\".eolymp.l10n.ListTermsInput.Filter\x1aY\n\x15\x45xpressionTranslation\x12\x0e\n\x06locale\x18\x01 \x01(\t\x12\x30\n\x06status\x18\x03 \x01(\x0b\x32 .eolymp.wellknown.ExpressionEnum\x1a\xa3\x02\n\x06\x46ilter\x12\r\n\x05query\x18\x64 \x01(\t\x12*\n\x02id\x18\x01 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12/\n\x03key\x18\x02 \x03(\x0b\x32\".eolymp.wellknown.ExpressionString\x12\x33\n\x07message\x18\x03 \x03(\x0b\x32\".eolymp.wellknown.ExpressionString\x12\x30\n\x06status\x18\x04 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\x12\x46\n\x0btranslation\x18\x05 \x03(\x0b\x32\x31.eolymp.l10n.ListTermsInput.ExpressionTranslation\"B\n\x0fListTermsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12 \n\x05items\x18\x02 \x03(\x0b\x32\x11.eolymp.l10n.Term\"C\n\x0fUpdateTermInput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\x12\x1f\n\x04term\x18\x02 \x01(\x0b\x32\x11.eolymp.l10n.Term\"\x12\n\x10UpdateTermOutput\"#\n\x10RestoreTermInput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\"\x13\n\x11RestoreTermOutput\"%\n\x12\x44\x65precateTermInput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\"\x15\n\x13\x44\x65precateTermOutput\"\"\n\x0f\x44\x65leteTermInput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\"\x12\n\x10\x44\x65leteTermOutput\"$\n\x11\x44\x65scribeTermInput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\"5\n\x12\x44\x65scribeTermOutput\x12\x1f\n\x04term\x18\x01 \x01(\x0b\x32\x11.eolymp.l10n.Term\"%\n\x0e\x41\x64\x64LocaleInput\x12\x13\n\x0blocale_code\x18\x01 \x01(\t\"\x11\n\x0f\x41\x64\x64LocaleOutput\"(\n\x11RemoveLocaleInput\x12\x13\n\x0blocale_code\x18\x01 \x01(\t\"\x14\n\x12RemoveLocaleOutput\"\x9f\x01\n\x10ListLocalesInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12\x35\n\x07\x66ilters\x18( \x01(\x0b\x32$.eolymp.l10n.ListLocalesInput.Filter\x1a\x36\n\x06\x46ilter\x12,\n\x04\x63ode\x18\x01 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\"\xa1\x01\n\x11ListLocalesOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x34\n\x05items\x18\x02 \x03(\x0b\x32%.eolymp.l10n.ListLocalesOutput.Locale\x1aG\n\x06Locale\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x18\n\x10translated_terms\x18\n \x01(\x05\x12\x15\n\rmissing_terms\x18\x0b \x01(\x05\"T\n\x12TranslateTermInput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\x12-\n\x0btranslation\x18\x02 \x01(\x0b\x32\x18.eolymp.l10n.Translation\"-\n\x13TranslateTermOutput\x12\x16\n\x0etranslation_id\x18\x01 \x01(\t\"\xd2\x02\n\x15ListTranslationsInput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12:\n\x07\x66ilters\x18( \x01(\x0b\x32).eolymp.l10n.ListTranslationsInput.Filter\x1a\xcd\x01\n\x06\x46ilter\x12*\n\x02id\x18\x01 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x33\n\x07message\x18\x02 \x03(\x0b\x32\".eolymp.wellknown.ExpressionString\x12\x30\n\x06status\x18\x03 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\x12\x30\n\x06locale\x18\x04 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\"P\n\x16ListTranslationsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12\'\n\x05items\x18\x02 \x03(\x0b\x32\x18.eolymp.l10n.Translation\":\n\x17SuggestTranslationInput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\x12\x0e\n\x06locale\x18\x02 \x01(\t\",\n\x18SuggestTranslationOutput\x12\x10\n\x08messages\x18\x01 \x03(\t\"p\n\x16UpdateTranslationInput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\x12\x16\n\x0etranslation_id\x18\x02 \x01(\t\x12-\n\x0btranslation\x18\x03 \x01(\x0b\x32\x18.eolymp.l10n.Translation\"\x19\n\x17UpdateTranslationOutput\"B\n\x17\x41pproveTranslationInput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\x12\x16\n\x0etranslation_id\x18\x02 \x01(\t\"\x1a\n\x18\x41pproveTranslationOutput\"A\n\x16RejectTranslationInput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\x12\x16\n\x0etranslation_id\x18\x02 \x01(\t\"\x19\n\x17RejectTranslationOutput\"A\n\x16\x44\x65leteTranslationInput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\x12\x16\n\x0etranslation_id\x18\x02 \x01(\t\"\x19\n\x17\x44\x65leteTranslationOutput\"+\n\x18\x44\x65scribeTranslationInput\x12\x0f\n\x07term_id\x18\x01 \x01(\t\"<\n\x19\x44\x65scribeTranslationOutput\x12\x1f\n\x04term\x18\x01 \x01(\x0b\x32\x11.eolymp.l10n.Term\"\xac\x01\n\x17ImportTranslationsInput\x12\x0e\n\x06locale\x18\x01 \x01(\t\x12L\n\x0ctranslations\x18\x02 \x03(\x0b\x32\x36.eolymp.l10n.ImportTranslationsInput.TranslationsEntry\x1a\x33\n\x11TranslationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"1\n\x18ImportTranslationsOutput\x12\x15\n\rcreated_count\x18\x01 \x01(\x05\")\n\x17\x45xportTranslationsInput\x12\x0e\n\x06locale\x18\x01 \x01(\t\"\x9e\x01\n\x18\x45xportTranslationsOutput\x12M\n\x0ctranslations\x18\x02 \x03(\x0b\x32\x37.eolymp.l10n.ExportTranslationsOutput.TranslationsEntry\x1a\x33\n\x11TranslationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xd0\x19\n\x13LocalizationService\x12\x7f\n\nCreateTerm\x12\x1c.eolymp.l10n.CreateTermInput\x1a\x1d.eolymp.l10n.CreateTermOutput\"4\x82\xe3\n\x13\x8a\xe3\n\x0fl10n:term:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x08\"\x06/terms\x12{\n\tListTerms\x12\x1b.eolymp.l10n.ListTermsInput\x1a\x1c.eolymp.l10n.ListTermsOutput\"3\x82\xe3\n\x12\x8a\xe3\n\x0el10n:term:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n2\x82\xd3\xe4\x93\x02\x08\x12\x06/terms\x12\x89\x01\n\nUpdateTerm\x12\x1c.eolymp.l10n.UpdateTermInput\x1a\x1d.eolymp.l10n.UpdateTermOutput\">\x82\xe3\n\x13\x8a\xe3\n\x0fl10n:term:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x12\x1a\x10/terms/{term_id}\x12\x94\x01\n\x0bRestoreTerm\x12\x1d.eolymp.l10n.RestoreTermInput\x1a\x1e.eolymp.l10n.RestoreTermOutput\"F\x82\xe3\n\x13\x8a\xe3\n\x0fl10n:term:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x1a\"\x18/terms/{term_id}/restore\x12\x9c\x01\n\rDeprecateTerm\x12\x1f.eolymp.l10n.DeprecateTermInput\x1a .eolymp.l10n.DeprecateTermOutput\"H\x82\xe3\n\x13\x8a\xe3\n\x0fl10n:term:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x1c\"\x1a/terms/{term_id}/deprecate\x12\x89\x01\n\nDeleteTerm\x12\x1c.eolymp.l10n.DeleteTermInput\x1a\x1d.eolymp.l10n.DeleteTermOutput\">\x82\xe3\n\x13\x8a\xe3\n\x0fl10n:term:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x12*\x10/terms/{term_id}\x12\x8e\x01\n\x0c\x44\x65scribeTerm\x12\x1e.eolymp.l10n.DescribeTermInput\x1a\x1f.eolymp.l10n.DescribeTermOutput\"=\x82\xe3\n\x12\x8a\xe3\n\x0el10n:term:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0\x41\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x12\x12\x10/terms/{term_id}\x12\x82\x01\n\x0bImportTerms\x12\x1d.eolymp.l10n.ImportTermsInput\x1a\x1e.eolymp.l10n.ImportTermsOutput\"4\x82\xe3\n\x13\x8a\xe3\n\x0fl10n:term:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x08\x1a\x06/terms\x12\x8e\x01\n\tAddLocale\x12\x1b.eolymp.l10n.AddLocaleInput\x1a\x1c.eolymp.l10n.AddLocaleOutput\"F\x82\xe3\n\x15\x8a\xe3\n\x11l10n:locale:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x18\x1a\x16/locales/{locale_code}\x12\x97\x01\n\x0cRemoveLocale\x12\x1e.eolymp.l10n.RemoveLocaleInput\x1a\x1f.eolymp.l10n.RemoveLocaleOutput\"F\x82\xe3\n\x15\x8a\xe3\n\x11l10n:locale:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x18*\x16/locales/{locale_code}\x12\x85\x01\n\x0bListLocales\x12\x1d.eolymp.l10n.ListLocalesInput\x1a\x1e.eolymp.l10n.ListLocalesOutput\"7\x82\xe3\n\x14\x8a\xe3\n\x10l10n:locale:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\n2\x82\xd3\xe4\x93\x02\n\x12\x08/locales\x12\xa6\x01\n\rTranslateTerm\x12\x1f.eolymp.l10n.TranslateTermInput\x1a .eolymp.l10n.TranslateTermOutput\"R\x82\xe3\n\x1a\x8a\xe3\n\x16l10n:translation:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x1f\"\x1d/terms/{term_id}/translations\x12\xaf\x01\n\x10ListTranslations\x12\".eolymp.l10n.ListTranslationsInput\x1a#.eolymp.l10n.ListTranslationsOutput\"R\x82\xe3\n\x19\x8a\xe3\n\x15l10n:translation:read\xea\xe2\n\x0c\xf5\xe2\n\x00\x00\xc8\x41\xf8\xe2\n\xc8\x01\x82\xd3\xe4\x93\x02\x1f\x12\x1d/terms/{term_id}/translations\x12\xc3\x01\n\x11\x44\x65leteTranslation\x12#.eolymp.l10n.DeleteTranslationInput\x1a$.eolymp.l10n.DeleteTranslationOutput\"c\x82\xe3\n\x1a\x8a\xe3\n\x16l10n:translation:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x30*./terms/{term_id}/translations/{translation_id}\x12\xbd\x01\n\x12SuggestTranslation\x12$.eolymp.l10n.SuggestTranslationInput\x1a%.eolymp.l10n.SuggestTranslationOutput\"Z\x82\xe3\n\x19\x8a\xe3\n\x15l10n:translation:read\xea\xe2\n\x0c\xf5\xe2\n\x00\x00\xc8\x41\xf8\xe2\n\xc8\x01\x82\xd3\xe4\x93\x02\'\x12%/terms/{term_id}/suggestions/{locale}\x12\xc3\x01\n\x11UpdateTranslation\x12#.eolymp.l10n.UpdateTranslationInput\x1a$.eolymp.l10n.UpdateTranslationOutput\"c\x82\xe3\n\x1a\x8a\xe3\n\x16l10n:translation:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x30\x1a./terms/{term_id}/translations/{translation_id}\x12\xce\x01\n\x12\x41pproveTranslation\x12$.eolymp.l10n.ApproveTranslationInput\x1a%.eolymp.l10n.ApproveTranslationOutput\"k\x82\xe3\n\x1a\x8a\xe3\n\x16l10n:translation:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x38\"6/terms/{term_id}/translations/{translation_id}/approve\x12\xca\x01\n\x11RejectTranslation\x12#.eolymp.l10n.RejectTranslationInput\x1a$.eolymp.l10n.RejectTranslationOutput\"j\x82\xe3\n\x1a\x8a\xe3\n\x16l10n:translation:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x37\"5/terms/{term_id}/translations/{translation_id}/reject\x12\xae\x01\n\x12ImportTranslations\x12$.eolymp.l10n.ImportTranslationsInput\x1a%.eolymp.l10n.ImportTranslationsOutput\"K\x82\xe3\n\x1a\x8a\xe3\n\x16l10n:translation:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x18\x1a\x16/translations/{locale}\x12\xad\x01\n\x12\x45xportTranslations\x12$.eolymp.l10n.ExportTranslationsInput\x1a%.eolymp.l10n.ExportTranslationsOutput\"J\x82\xe3\n\x19\x8a\xe3\n\x15l10n:translation:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x18\x12\x16/translations/{locale}B+Z)github.com/eolymp/go-sdk/eolymp/l10n;l10nb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.l10n.localization_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/eolymp/go-sdk/eolymp/l10n;l10n'
  _IMPORTTRANSLATIONSINPUT_TRANSLATIONSENTRY._options = None
  _IMPORTTRANSLATIONSINPUT_TRANSLATIONSENTRY._serialized_options = b'8\001'
  _EXPORTTRANSLATIONSOUTPUT_TRANSLATIONSENTRY._options = None
  _EXPORTTRANSLATIONSOUTPUT_TRANSLATIONSENTRY._serialized_options = b'8\001'
  _LOCALIZATIONSERVICE.methods_by_name['CreateTerm']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['CreateTerm']._serialized_options = b'\202\343\n\023\212\343\n\017l10n:term:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\010\"\006/terms'
  _LOCALIZATIONSERVICE.methods_by_name['ListTerms']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['ListTerms']._serialized_options = b'\202\343\n\022\212\343\n\016l10n:term:read\352\342\n\013\365\342\n\000\000\240@\370\342\n2\202\323\344\223\002\010\022\006/terms'
  _LOCALIZATIONSERVICE.methods_by_name['UpdateTerm']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['UpdateTerm']._serialized_options = b'\202\343\n\023\212\343\n\017l10n:term:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\022\032\020/terms/{term_id}'
  _LOCALIZATIONSERVICE.methods_by_name['RestoreTerm']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['RestoreTerm']._serialized_options = b'\202\343\n\023\212\343\n\017l10n:term:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\032\"\030/terms/{term_id}/restore'
  _LOCALIZATIONSERVICE.methods_by_name['DeprecateTerm']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['DeprecateTerm']._serialized_options = b'\202\343\n\023\212\343\n\017l10n:term:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\034\"\032/terms/{term_id}/deprecate'
  _LOCALIZATIONSERVICE.methods_by_name['DeleteTerm']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['DeleteTerm']._serialized_options = b'\202\343\n\023\212\343\n\017l10n:term:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\022*\020/terms/{term_id}'
  _LOCALIZATIONSERVICE.methods_by_name['DescribeTerm']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['DescribeTerm']._serialized_options = b'\202\343\n\022\212\343\n\016l10n:term:read\352\342\n\013\365\342\n\000\000\240A\370\342\nd\202\323\344\223\002\022\022\020/terms/{term_id}'
  _LOCALIZATIONSERVICE.methods_by_name['ImportTerms']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['ImportTerms']._serialized_options = b'\202\343\n\023\212\343\n\017l10n:term:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\010\032\006/terms'
  _LOCALIZATIONSERVICE.methods_by_name['AddLocale']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['AddLocale']._serialized_options = b'\202\343\n\025\212\343\n\021l10n:locale:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\030\032\026/locales/{locale_code}'
  _LOCALIZATIONSERVICE.methods_by_name['RemoveLocale']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['RemoveLocale']._serialized_options = b'\202\343\n\025\212\343\n\021l10n:locale:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\030*\026/locales/{locale_code}'
  _LOCALIZATIONSERVICE.methods_by_name['ListLocales']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['ListLocales']._serialized_options = b'\202\343\n\024\212\343\n\020l10n:locale:read\352\342\n\013\365\342\n\000\000 A\370\342\n2\202\323\344\223\002\n\022\010/locales'
  _LOCALIZATIONSERVICE.methods_by_name['TranslateTerm']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['TranslateTerm']._serialized_options = b'\202\343\n\032\212\343\n\026l10n:translation:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\037\"\035/terms/{term_id}/translations'
  _LOCALIZATIONSERVICE.methods_by_name['ListTranslations']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['ListTranslations']._serialized_options = b'\202\343\n\031\212\343\n\025l10n:translation:read\352\342\n\014\365\342\n\000\000\310A\370\342\n\310\001\202\323\344\223\002\037\022\035/terms/{term_id}/translations'
  _LOCALIZATIONSERVICE.methods_by_name['DeleteTranslation']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['DeleteTranslation']._serialized_options = b'\202\343\n\032\212\343\n\026l10n:translation:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\0020*./terms/{term_id}/translations/{translation_id}'
  _LOCALIZATIONSERVICE.methods_by_name['SuggestTranslation']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['SuggestTranslation']._serialized_options = b'\202\343\n\031\212\343\n\025l10n:translation:read\352\342\n\014\365\342\n\000\000\310A\370\342\n\310\001\202\323\344\223\002\'\022%/terms/{term_id}/suggestions/{locale}'
  _LOCALIZATIONSERVICE.methods_by_name['UpdateTranslation']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['UpdateTranslation']._serialized_options = b'\202\343\n\032\212\343\n\026l10n:translation:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\0020\032./terms/{term_id}/translations/{translation_id}'
  _LOCALIZATIONSERVICE.methods_by_name['ApproveTranslation']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['ApproveTranslation']._serialized_options = b'\202\343\n\032\212\343\n\026l10n:translation:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\0028\"6/terms/{term_id}/translations/{translation_id}/approve'
  _LOCALIZATIONSERVICE.methods_by_name['RejectTranslation']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['RejectTranslation']._serialized_options = b'\202\343\n\032\212\343\n\026l10n:translation:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\0027\"5/terms/{term_id}/translations/{translation_id}/reject'
  _LOCALIZATIONSERVICE.methods_by_name['ImportTranslations']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['ImportTranslations']._serialized_options = b'\202\343\n\032\212\343\n\026l10n:translation:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\030\032\026/translations/{locale}'
  _LOCALIZATIONSERVICE.methods_by_name['ExportTranslations']._options = None
  _LOCALIZATIONSERVICE.methods_by_name['ExportTranslations']._serialized_options = b'\202\343\n\031\212\343\n\025l10n:translation:read\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\030\022\026/translations/{locale}'
  _CREATETERMINPUT._serialized_start=244
  _CREATETERMINPUT._serialized_end=294
  _CREATETERMOUTPUT._serialized_start=296
  _CREATETERMOUTPUT._serialized_end=331
  _IMPORTTERMSINPUT._serialized_start=333
  _IMPORTTERMSINPUT._serialized_end=385
  _IMPORTTERMSOUTPUT._serialized_start=387
  _IMPORTTERMSOUTPUT._serialized_end=478
  _LISTTERMSINPUT._serialized_start=481
  _LISTTERMSINPUT._serialized_end=965
  _LISTTERMSINPUT_EXPRESSIONTRANSLATION._serialized_start=582
  _LISTTERMSINPUT_EXPRESSIONTRANSLATION._serialized_end=671
  _LISTTERMSINPUT_FILTER._serialized_start=674
  _LISTTERMSINPUT_FILTER._serialized_end=965
  _LISTTERMSOUTPUT._serialized_start=967
  _LISTTERMSOUTPUT._serialized_end=1033
  _UPDATETERMINPUT._serialized_start=1035
  _UPDATETERMINPUT._serialized_end=1102
  _UPDATETERMOUTPUT._serialized_start=1104
  _UPDATETERMOUTPUT._serialized_end=1122
  _RESTORETERMINPUT._serialized_start=1124
  _RESTORETERMINPUT._serialized_end=1159
  _RESTORETERMOUTPUT._serialized_start=1161
  _RESTORETERMOUTPUT._serialized_end=1180
  _DEPRECATETERMINPUT._serialized_start=1182
  _DEPRECATETERMINPUT._serialized_end=1219
  _DEPRECATETERMOUTPUT._serialized_start=1221
  _DEPRECATETERMOUTPUT._serialized_end=1242
  _DELETETERMINPUT._serialized_start=1244
  _DELETETERMINPUT._serialized_end=1278
  _DELETETERMOUTPUT._serialized_start=1280
  _DELETETERMOUTPUT._serialized_end=1298
  _DESCRIBETERMINPUT._serialized_start=1300
  _DESCRIBETERMINPUT._serialized_end=1336
  _DESCRIBETERMOUTPUT._serialized_start=1338
  _DESCRIBETERMOUTPUT._serialized_end=1391
  _ADDLOCALEINPUT._serialized_start=1393
  _ADDLOCALEINPUT._serialized_end=1430
  _ADDLOCALEOUTPUT._serialized_start=1432
  _ADDLOCALEOUTPUT._serialized_end=1449
  _REMOVELOCALEINPUT._serialized_start=1451
  _REMOVELOCALEINPUT._serialized_end=1491
  _REMOVELOCALEOUTPUT._serialized_start=1493
  _REMOVELOCALEOUTPUT._serialized_end=1513
  _LISTLOCALESINPUT._serialized_start=1516
  _LISTLOCALESINPUT._serialized_end=1675
  _LISTLOCALESINPUT_FILTER._serialized_start=1621
  _LISTLOCALESINPUT_FILTER._serialized_end=1675
  _LISTLOCALESOUTPUT._serialized_start=1678
  _LISTLOCALESOUTPUT._serialized_end=1839
  _LISTLOCALESOUTPUT_LOCALE._serialized_start=1768
  _LISTLOCALESOUTPUT_LOCALE._serialized_end=1839
  _TRANSLATETERMINPUT._serialized_start=1841
  _TRANSLATETERMINPUT._serialized_end=1925
  _TRANSLATETERMOUTPUT._serialized_start=1927
  _TRANSLATETERMOUTPUT._serialized_end=1972
  _LISTTRANSLATIONSINPUT._serialized_start=1975
  _LISTTRANSLATIONSINPUT._serialized_end=2313
  _LISTTRANSLATIONSINPUT_FILTER._serialized_start=2108
  _LISTTRANSLATIONSINPUT_FILTER._serialized_end=2313
  _LISTTRANSLATIONSOUTPUT._serialized_start=2315
  _LISTTRANSLATIONSOUTPUT._serialized_end=2395
  _SUGGESTTRANSLATIONINPUT._serialized_start=2397
  _SUGGESTTRANSLATIONINPUT._serialized_end=2455
  _SUGGESTTRANSLATIONOUTPUT._serialized_start=2457
  _SUGGESTTRANSLATIONOUTPUT._serialized_end=2501
  _UPDATETRANSLATIONINPUT._serialized_start=2503
  _UPDATETRANSLATIONINPUT._serialized_end=2615
  _UPDATETRANSLATIONOUTPUT._serialized_start=2617
  _UPDATETRANSLATIONOUTPUT._serialized_end=2642
  _APPROVETRANSLATIONINPUT._serialized_start=2644
  _APPROVETRANSLATIONINPUT._serialized_end=2710
  _APPROVETRANSLATIONOUTPUT._serialized_start=2712
  _APPROVETRANSLATIONOUTPUT._serialized_end=2738
  _REJECTTRANSLATIONINPUT._serialized_start=2740
  _REJECTTRANSLATIONINPUT._serialized_end=2805
  _REJECTTRANSLATIONOUTPUT._serialized_start=2807
  _REJECTTRANSLATIONOUTPUT._serialized_end=2832
  _DELETETRANSLATIONINPUT._serialized_start=2834
  _DELETETRANSLATIONINPUT._serialized_end=2899
  _DELETETRANSLATIONOUTPUT._serialized_start=2901
  _DELETETRANSLATIONOUTPUT._serialized_end=2926
  _DESCRIBETRANSLATIONINPUT._serialized_start=2928
  _DESCRIBETRANSLATIONINPUT._serialized_end=2971
  _DESCRIBETRANSLATIONOUTPUT._serialized_start=2973
  _DESCRIBETRANSLATIONOUTPUT._serialized_end=3033
  _IMPORTTRANSLATIONSINPUT._serialized_start=3036
  _IMPORTTRANSLATIONSINPUT._serialized_end=3208
  _IMPORTTRANSLATIONSINPUT_TRANSLATIONSENTRY._serialized_start=3157
  _IMPORTTRANSLATIONSINPUT_TRANSLATIONSENTRY._serialized_end=3208
  _IMPORTTRANSLATIONSOUTPUT._serialized_start=3210
  _IMPORTTRANSLATIONSOUTPUT._serialized_end=3259
  _EXPORTTRANSLATIONSINPUT._serialized_start=3261
  _EXPORTTRANSLATIONSINPUT._serialized_end=3302
  _EXPORTTRANSLATIONSOUTPUT._serialized_start=3305
  _EXPORTTRANSLATIONSOUTPUT._serialized_end=3463
  _EXPORTTRANSLATIONSOUTPUT_TRANSLATIONSENTRY._serialized_start=3157
  _EXPORTTRANSLATIONSOUTPUT_TRANSLATIONSENTRY._serialized_end=3208
  _LOCALIZATIONSERVICE._serialized_start=3466
  _LOCALIZATIONSERVICE._serialized_end=6746
# @@protoc_insertion_point(module_scope)
