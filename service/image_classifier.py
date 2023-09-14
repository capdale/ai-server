import proto.image_pb2
import proto.image_pb2_grpc


class ImageClassiferServicer(proto.image_pb2_grpc.ImageClassifyServicer):
    def ClassifyImage(self, request, context):
        return proto.image_pb2.ImageClassifierReply(state=1, class_index=1)
