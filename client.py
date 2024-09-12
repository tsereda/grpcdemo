import grpc
import advanced_greeting_pb2
import advanced_greeting_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = advanced_greeting_pb2_grpc.AdvancedGreeterStub(channel)
        
        # Unary RPC
        response = stub.SayHello(advanced_greeting_pb2.HelloRequest(name='World'))
        print("Unary RPC response:", response.message)
        
        # Server Streaming RPC
        responses = stub.GreetManyTimes(advanced_greeting_pb2.HelloRequest(name='Stream'))
        for response in responses:
            print("Server Streaming response:", response.message)
        
        # Client Streaming RPC
        requests = iter([advanced_greeting_pb2.HelloRequest(name=name) for name in ["Alice", "Bob", "Charlie"]])
        response = stub.LongGreet(requests)
        print("Client Streaming response:", response.message)
        
        # Bidirectional Streaming RPC
        requests = iter([advanced_greeting_pb2.HelloRequest(name=name) for name in ["Dave", "Eve", "Frank"]])
        responses = stub.GreetEveryone(requests)
        for response in responses:
            print("Bidirectional Streaming response:", response.message)

if __name__ == '__main__':
    run()