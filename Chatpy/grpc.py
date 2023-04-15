import grpc
import chat_pb2
import chat_pb2_grpc

# define server information
HOST = "localhost"
PORT = 8000

# create a gRPC channel to the server
channel = grpc.insecure_channel(f"{HOST}:{PORT}")

# create a gRPC stub for the chat service
stub = chat_pb2_grpc.ChatStub(channel)

# define a username for the client
username = "Alice"

# define a function to send messages to the server
def send_message():
    while True:
        message = input("Enter message: ")
        stub.SendMessage(chat_pb2.Message(username=username, text=message))

# define a function to receive messages from the server
def receive_messages():
    for message in stub.ReceiveMessages(chat_pb2.Empty()):
        print(f"{message.username}: {message.text}")

# start the send and receive message threads
send_thread = threading.Thread(target=send_message)
send_thread.start()

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()