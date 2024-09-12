from concurrent import futures
import time
import grpc
from flask import Flask
import advanced_greeting_pb2
import advanced_greeting_pb2_grpc

app = Flask(__name__)

class AdvancedGreeterServicer(advanced_greeting_pb2_grpc.AdvancedGreeterServicer):
    def SayHello(self, request, context):
        return advanced_greeting_pb2.HelloReply(message=f"Hello, {request.name}!")

    def GreetManyTimes(self, request, context):
        for i in range(5):
            yield advanced_greeting_pb2.HelloReply(message=f"Hello {request.name}, response #{i+1}")
            time.sleep(1)

    def LongGreet(self, request_iterator, context):
        result = []
        for request in request_iterator:
            result.append(f"Hello {request.name}")
        return advanced_greeting_pb2.HelloReply(message=", ".join(result))

    def GreetEveryone(self, request_iterator, context):
        for request in request_iterator:
            yield advanced_greeting_pb2.HelloReply(message=f"Hello {request.name}!")

@app.route('/')
def hello():
    return "Advanced gRPC Flask Server is running!"

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    advanced_greeting_pb2_grpc.add_AdvancedGreeterServicer_to_server(AdvancedGreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    app.run(port=5000)

if __name__ == '__main__':
    serve()
