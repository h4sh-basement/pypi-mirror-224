# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ondewo.t2s import text_to_speech_pb2 as ondewo_dot_t2s_dot_text__to__speech__pb2


class Text2SpeechStub(object):
    """endpoints of t2s generate service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Synthesize = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/Synthesize',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.SynthesizeRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.SynthesizeResponse.FromString,
        )
        self.BatchSynthesize = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/BatchSynthesize',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.BatchSynthesizeRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.BatchSynthesizeResponse.FromString,
        )
        self.NormalizeText = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/NormalizeText',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.NormalizeTextRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.NormalizeTextResponse.FromString,
        )
        self.GetT2sPipeline = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/GetT2sPipeline',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.FromString,
        )
        self.CreateT2sPipeline = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/CreateT2sPipeline',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.FromString,
        )
        self.DeleteT2sPipeline = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/DeleteT2sPipeline',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.UpdateT2sPipeline = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/UpdateT2sPipeline',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.ListT2sPipelines = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/ListT2sPipelines',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sPipelinesRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sPipelinesResponse.FromString,
        )
        self.ListT2sLanguages = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/ListT2sLanguages',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sLanguagesRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sLanguagesResponse.FromString,
        )
        self.ListT2sDomains = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/ListT2sDomains',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sDomainsRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sDomainsResponse.FromString,
        )
        self.GetServiceInfo = channel.unary_unary(
            '/ondewo.t2s.Text2Speech/GetServiceInfo',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2SGetServiceInfoResponse.FromString,
        )


class Text2SpeechServicer(object):
    """endpoints of t2s generate service
    """

    def Synthesize(self, request, context):
        """Synthesizes an specific text sent in the request with the configuration requirements and retrieves a response
        that includes the synthesized text to audio and the configuration wanted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchSynthesize(self, request, context):
        """will this safe time when doing batch predict on the AI model?
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NormalizeText(self, request, context):
        """Normalize a text according to a specific pipeline normalization rules.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetT2sPipeline(self, request, context):
        """Retrieves the configuration of the specified pipeline.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateT2sPipeline(self, request, context):
        """Creates a pipeline with the specified configuration and retrieves its id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteT2sPipeline(self, request, context):
        """Deletes the specified pipeline.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateT2sPipeline(self, request, context):
        """Update a specified pipeline with certain configuration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListT2sPipelines(self, request, context):
        """Retrieve the list of pipelines with an specific requirement.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListT2sLanguages(self, request, context):
        """Retrieve the list of languages given a specific config request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListT2sDomains(self, request, context):
        """Retrieve the list of domains given a specific config request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServiceInfo(self, request, context):
        """Returns a message containing the version of the running text to speech server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Text2SpeechServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Synthesize': grpc.unary_unary_rpc_method_handler(
            servicer.Synthesize,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.SynthesizeRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.SynthesizeResponse.SerializeToString,
        ),
        'BatchSynthesize': grpc.unary_unary_rpc_method_handler(
            servicer.BatchSynthesize,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.BatchSynthesizeRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.BatchSynthesizeResponse.SerializeToString,
        ),
        'NormalizeText': grpc.unary_unary_rpc_method_handler(
            servicer.NormalizeText,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.NormalizeTextRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.NormalizeTextResponse.SerializeToString,
        ),
        'GetT2sPipeline': grpc.unary_unary_rpc_method_handler(
            servicer.GetT2sPipeline,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.SerializeToString,
        ),
        'CreateT2sPipeline': grpc.unary_unary_rpc_method_handler(
            servicer.CreateT2sPipeline,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.SerializeToString,
        ),
        'DeleteT2sPipeline': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteT2sPipeline,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        'UpdateT2sPipeline': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateT2sPipeline,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        'ListT2sPipelines': grpc.unary_unary_rpc_method_handler(
            servicer.ListT2sPipelines,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sPipelinesRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sPipelinesResponse.SerializeToString,
        ),
        'ListT2sLanguages': grpc.unary_unary_rpc_method_handler(
            servicer.ListT2sLanguages,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sLanguagesRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sLanguagesResponse.SerializeToString,
        ),
        'ListT2sDomains': grpc.unary_unary_rpc_method_handler(
            servicer.ListT2sDomains,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sDomainsRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sDomainsResponse.SerializeToString,
        ),
        'GetServiceInfo': grpc.unary_unary_rpc_method_handler(
            servicer.GetServiceInfo,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.T2SGetServiceInfoResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'ondewo.t2s.Text2Speech', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class Text2Speech(object):
    """endpoints of t2s generate service
    """

    @staticmethod
    def Synthesize(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.Text2Speech/Synthesize',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.SynthesizeRequest.SerializeToString,
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.SynthesizeResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchSynthesize(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.Text2Speech/BatchSynthesize',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.BatchSynthesizeRequest.SerializeToString,
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.BatchSynthesizeResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NormalizeText(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.Text2Speech/NormalizeText',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.NormalizeTextRequest.SerializeToString,
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.NormalizeTextResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetT2sPipeline(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.Text2Speech/GetT2sPipeline',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.SerializeToString,
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateT2sPipeline(request,
                          target,
                          options=(),
                          channel_credentials=None,
                          call_credentials=None,
                          insecure=False,
                          compression=None,
                          wait_for_ready=None,
                          timeout=None,
                          metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.Text2Speech/CreateT2sPipeline',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.SerializeToString,
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteT2sPipeline(request,
                          target,
                          options=(),
                          channel_credentials=None,
                          call_credentials=None,
                          insecure=False,
                          compression=None,
                          wait_for_ready=None,
                          timeout=None,
                          metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.Text2Speech/DeleteT2sPipeline',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.T2sPipelineId.SerializeToString,
                                             google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateT2sPipeline(request,
                          target,
                          options=(),
                          channel_credentials=None,
                          call_credentials=None,
                          insecure=False,
                          compression=None,
                          wait_for_ready=None,
                          timeout=None,
                          metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.Text2Speech/UpdateT2sPipeline',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.Text2SpeechConfig.SerializeToString,
                                             google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListT2sPipelines(request,
                         target,
                         options=(),
                         channel_credentials=None,
                         call_credentials=None,
                         insecure=False,
                         compression=None,
                         wait_for_ready=None,
                         timeout=None,
                         metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.Text2Speech/ListT2sPipelines',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sPipelinesRequest.SerializeToString,
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sPipelinesResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListT2sLanguages(request,
                         target,
                         options=(),
                         channel_credentials=None,
                         call_credentials=None,
                         insecure=False,
                         compression=None,
                         wait_for_ready=None,
                         timeout=None,
                         metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.Text2Speech/ListT2sLanguages',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sLanguagesRequest.SerializeToString,
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sLanguagesResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListT2sDomains(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.Text2Speech/ListT2sDomains',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sDomainsRequest.SerializeToString,
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.ListT2sDomainsResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServiceInfo(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.Text2Speech/GetServiceInfo',
                                             google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.T2SGetServiceInfoResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class CustomPhonemizersStub(object):
    """endpoints of custom phonemizer
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCustomPhonemizer = channel.unary_unary(
            '/ondewo.t2s.CustomPhonemizers/GetCustomPhonemizer',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.CustomPhonemizerProto.FromString,
        )
        self.CreateCustomPhonemizer = channel.unary_unary(
            '/ondewo.t2s.CustomPhonemizers/CreateCustomPhonemizer',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.CreateCustomPhonemizerRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.FromString,
        )
        self.DeleteCustomPhonemizer = channel.unary_unary(
            '/ondewo.t2s.CustomPhonemizers/DeleteCustomPhonemizer',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.UpdateCustomPhonemizer = channel.unary_unary(
            '/ondewo.t2s.CustomPhonemizers/UpdateCustomPhonemizer',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.UpdateCustomPhonemizerRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.CustomPhonemizerProto.FromString,
        )
        self.ListCustomPhonemizer = channel.unary_unary(
            '/ondewo.t2s.CustomPhonemizers/ListCustomPhonemizer',
            request_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListCustomPhonemizerRequest.SerializeToString,
            response_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListCustomPhonemizerResponse.FromString,
        )


class CustomPhonemizersServicer(object):
    """endpoints of custom phonemizer
    """

    def GetCustomPhonemizer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCustomPhonemizer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCustomPhonemizer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCustomPhonemizer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCustomPhonemizer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CustomPhonemizersServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetCustomPhonemizer': grpc.unary_unary_rpc_method_handler(
            servicer.GetCustomPhonemizer,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.CustomPhonemizerProto.SerializeToString,
        ),
        'CreateCustomPhonemizer': grpc.unary_unary_rpc_method_handler(
            servicer.CreateCustomPhonemizer,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.CreateCustomPhonemizerRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.SerializeToString,
        ),
        'DeleteCustomPhonemizer': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteCustomPhonemizer,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        'UpdateCustomPhonemizer': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateCustomPhonemizer,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.UpdateCustomPhonemizerRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.CustomPhonemizerProto.SerializeToString,
        ),
        'ListCustomPhonemizer': grpc.unary_unary_rpc_method_handler(
            servicer.ListCustomPhonemizer,
            request_deserializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListCustomPhonemizerRequest.FromString,
            response_serializer=ondewo_dot_t2s_dot_text__to__speech__pb2.ListCustomPhonemizerResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'ondewo.t2s.CustomPhonemizers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class CustomPhonemizers(object):
    """endpoints of custom phonemizer
    """

    @staticmethod
    def GetCustomPhonemizer(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.CustomPhonemizers/GetCustomPhonemizer',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.SerializeToString,
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.CustomPhonemizerProto.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCustomPhonemizer(request,
                               target,
                               options=(),
                               channel_credentials=None,
                               call_credentials=None,
                               insecure=False,
                               compression=None,
                               wait_for_ready=None,
                               timeout=None,
                               metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.CustomPhonemizers/CreateCustomPhonemizer',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.CreateCustomPhonemizerRequest.SerializeToString,
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCustomPhonemizer(request,
                               target,
                               options=(),
                               channel_credentials=None,
                               call_credentials=None,
                               insecure=False,
                               compression=None,
                               wait_for_ready=None,
                               timeout=None,
                               metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.CustomPhonemizers/DeleteCustomPhonemizer',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.PhonemizerId.SerializeToString,
                                             google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCustomPhonemizer(request,
                               target,
                               options=(),
                               channel_credentials=None,
                               call_credentials=None,
                               insecure=False,
                               compression=None,
                               wait_for_ready=None,
                               timeout=None,
                               metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.CustomPhonemizers/UpdateCustomPhonemizer',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.UpdateCustomPhonemizerRequest.SerializeToString,
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.CustomPhonemizerProto.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCustomPhonemizer(request,
                             target,
                             options=(),
                             channel_credentials=None,
                             call_credentials=None,
                             insecure=False,
                             compression=None,
                             wait_for_ready=None,
                             timeout=None,
                             metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ondewo.t2s.CustomPhonemizers/ListCustomPhonemizer',
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.ListCustomPhonemizerRequest.SerializeToString,
                                             ondewo_dot_t2s_dot_text__to__speech__pb2.ListCustomPhonemizerResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
