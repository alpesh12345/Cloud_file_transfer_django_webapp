import socket
import pickle

"""
Message Name/type we are using :
type = will contain following types
READ = To get the file data from storage
WRITE = To add save the file data to storage

client_username: send client_id here, to distinguish the file of two users
file: To save the file with id at the storage

error = True :  will handle all the error
error_type = type of error
"""

MSG_SIZE = 1024 * 4

# Update all the stroage node IP everytime
storage_1 = {"ip": "172.17.0.1", "port": 8001}
storage_2 = {"ip": "172.17.0.1", "port": 8002}

storage_ip = {1: storage_1, 2: storage_2}


def _send_msg(socket, msg):
    msg = pickle.dumps(msg)
    socket.send(msg)


def _recv_msg(socket, size):
    rec_packet = []
    i = 0
    print("Waiting packet..")
    while True:
        try:
            socket.settimeout(5)
            msg = socket.recv(MSG_SIZE)
            # socket.settimeout(None)
            print(".")

            if not msg:
                break

            rec_packet.append(msg)

        except:
            break

    print("Joining packet..")
    data = b"".join(rec_packet)

    if not data:
        return None

    r_msg = pickle.loads(data)
    # print(r_msg)

    return r_msg