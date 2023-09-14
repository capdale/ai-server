from concurrent import futures

import grpc

from proto.image_pb2_grpc import add_ImageClassifyServicer_to_server
from service.image_classifier import ImageClassiferServicer


def main():
    print("Proto server load")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ImageClassifyServicer_to_server(ImageClassiferServicer(), server)

    server.add_insecure_port("[::]:50050")

    server.start()

    print("Proto server start")

    server.wait_for_termination()


if __name__ == "__main__":
    main()
