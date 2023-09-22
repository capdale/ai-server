from concurrent import futures

import grpc

from proto.image_pb2_grpc import add_ImageClassifyServicer_to_server
from service.image_classifier import ImageClassiferServicer
from funcmodel.func.image_classify import ImageClassify

MAX_SEND_MESSAGE_LENGTH = 8388608
MAX_RECV_MESSAGE_LENGTH = 8388608


def main():
    print("Proto server load")

    image_classfier = ImageClassify("./funcmodel/weight/cnn.pt")

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        options=[
            ("grpc.max_send_message_length", MAX_SEND_MESSAGE_LENGTH),
            ("grpc.max_receive_message_length", MAX_RECV_MESSAGE_LENGTH),
        ],
    )
    add_ImageClassifyServicer_to_server(ImageClassiferServicer(image_classfier), server)

    server.add_insecure_port("localhost:50050")

    server.start()

    print("Proto server start")

    server.wait_for_termination()


if __name__ == "__main__":
    main()
