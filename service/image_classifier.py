import proto.image_pb2
import proto.image_pb2_grpc

from funcmodel.func.image_classify import ImageClassify


class ImageClassiferServicer(proto.image_pb2_grpc.ImageClassifyServicer):
    def __init__(self, image_classifier: ImageClassify) -> None:
        self.image_classifier = image_classifier
        super().__init__()

    def ClassifyImage(self, request: proto.image_pb2.ImageClassifierRequest, context):
        class_index = self.image_classifier.input(request.image)
        return proto.image_pb2.ImageClassifierReply(state=0, class_index=class_index)
