import  sys
import _pickle as pickle
import json

import websocket


class Network:

    def __init__(self):
        self.client = websocket.WebSocket()
        # self.host = "127.0.0.1"
        self.host = "13.71.64.234"
        self.port = 5555
        self.addr = f"ws://{self.host}:{self.port}"

    def connect(self, name):
        self.client.connect(self.addr)
        self.client.send(name)
        c_id = self.client.recv()

        if type(c_id) == bytes:
            c_id = c_id.decode("utf-8")

        print(f"Val recieved connecting: {c_id}")
        return c_id

    def disconnect(self):
        self.client.close()

    def send(self, data, j=True):
        try:
            if j:
                self.client.send(json.dumps(data))
            else:
                self.client.send(data)

            reply = self.client.recv()

            try:
                reply = json.loads(reply)
            except Exception as e:
                print("Error loading json", "-"*20)
                print(f"reply: {reply}")
                print("Error loading json", "-"*20)
                print(e)

            return reply
        except Exception as e:
            print(e)
