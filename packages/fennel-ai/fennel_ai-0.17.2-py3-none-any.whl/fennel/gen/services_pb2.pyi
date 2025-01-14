"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import connector_pb2
import dataset_pb2
import expectations_pb2
import featureset_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class SyncRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATASETS_FIELD_NUMBER: builtins.int
    PIPELINES_FIELD_NUMBER: builtins.int
    OPERATORS_FIELD_NUMBER: builtins.int
    FEATURE_SETS_FIELD_NUMBER: builtins.int
    FEATURES_FIELD_NUMBER: builtins.int
    EXTRACTORS_FIELD_NUMBER: builtins.int
    MODELS_FIELD_NUMBER: builtins.int
    SOURCES_FIELD_NUMBER: builtins.int
    EXTDBS_FIELD_NUMBER: builtins.int
    EXPECTATIONS_FIELD_NUMBER: builtins.int
    @property
    def datasets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dataset_pb2.CoreDataset]: ...
    @property
    def pipelines(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dataset_pb2.Pipeline]: ...
    @property
    def operators(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[dataset_pb2.Operator]: ...
    @property
    def feature_sets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[featureset_pb2.CoreFeatureset]: ...
    @property
    def features(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[featureset_pb2.Feature]: ...
    @property
    def extractors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[featureset_pb2.Extractor]: ...
    @property
    def models(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[featureset_pb2.Model]: ...
    @property
    def sources(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[connector_pb2.Source]: ...
    @property
    def extdbs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[connector_pb2.ExtDatabase]: ...
    @property
    def expectations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[expectations_pb2.Expectations]: ...
    def __init__(
        self,
        *,
        datasets: collections.abc.Iterable[dataset_pb2.CoreDataset] | None = ...,
        pipelines: collections.abc.Iterable[dataset_pb2.Pipeline] | None = ...,
        operators: collections.abc.Iterable[dataset_pb2.Operator] | None = ...,
        feature_sets: collections.abc.Iterable[featureset_pb2.CoreFeatureset] | None = ...,
        features: collections.abc.Iterable[featureset_pb2.Feature] | None = ...,
        extractors: collections.abc.Iterable[featureset_pb2.Extractor] | None = ...,
        models: collections.abc.Iterable[featureset_pb2.Model] | None = ...,
        sources: collections.abc.Iterable[connector_pb2.Source] | None = ...,
        extdbs: collections.abc.Iterable[connector_pb2.ExtDatabase] | None = ...,
        expectations: collections.abc.Iterable[expectations_pb2.Expectations] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["datasets", b"datasets", "expectations", b"expectations", "extdbs", b"extdbs", "extractors", b"extractors", "feature_sets", b"feature_sets", "features", b"features", "models", b"models", "operators", b"operators", "pipelines", b"pipelines", "sources", b"sources"]) -> None: ...

global___SyncRequest = SyncRequest
