import socket

target_ip = "127.0.0.1"
target_port = 2222

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, target_port))

s.send(b"admin\n")
s.send(b"123456\n")

s.close()

print("Fake attack sent")