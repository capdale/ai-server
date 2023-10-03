from concurrent import futures
import yaml

import grpc

from proto.image_pb2_grpc import add_ImageClassifyServicer_to_server
from service.image_classifier import ImageClassiferServicer
from funcmodel.func.image_classify import ImageClassify

MAX_SEND_MESSAGE_LENGTH = 8388608
MAX_RECV_MESSAGE_LENGTH = 8388608


def main():
    print("server load")
    print("load config file (find config.yaml)")

    with open("config.yaml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    server_address = config["service"]["address"]

    image_classfier = ImageClassify("./funcmodel/weight/cnn.pt")

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        options=[
            ("grpc.max_send_message_length", MAX_SEND_MESSAGE_LENGTH),
            ("grpc.max_receive_message_length", MAX_RECV_MESSAGE_LENGTH),
        ],
    )
    add_ImageClassifyServicer_to_server(ImageClassiferServicer(image_classfier), server)

    server.add_insecure_port(server_address)

    server.start()

    print("server start")

    server.wait_for_termination()


if __name__ == "__main__":
    main()
