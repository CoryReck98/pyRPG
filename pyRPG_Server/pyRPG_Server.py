from multiprocessing import Process, Queue
import select
import socket
import time

import map as spawn_map
import multiplayer


# Returns IP to bind to.
def ip():
    return 'localhost'
# Returns port to bind to.
def port():
    return 5000

# Starts map with given name.
def start_map(name):
    return 0

# Accepts connections, manages IPC, manages input
def connector(queue):
    # Make server socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serversocket.bind((ip(), port()))

    # maps is a dict from map_name to [get_queue, send_queue]
    maps = {}
    while True: # Main loop, connections are received, data is processed.
        # Check if we have readable data.

        # List of all players that need to be put in new maps. List of (mapname, player)
        move_requests = []

        can_read, can_write, errors = select.select([serversocket], [], [], 0)
        if can_read != []: # We have some data to process...
            (data, addr) = serversocket.recvfrom(65507) # Receive the data.
            plr_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # Socket player connects to.
            plr = multiplayer.player(25, 10, plr_sock, addr)                       # New player object for request.
            move_requests.append(("start", plr))
            print("Player connected")

        if not queue.empty(): # Some owner input
            command = queue.get()
            if command == "end":
                serversocket.close() # End server
                for map, data in maps.items(): # End maps.
                    data[1].put(("end",))
                return
            elif command == "test":
                print("Test...")
            else:
                print("Unknown command \"", command, '"')

        # Go through map queue input.
        
        to_close = [] # List of maps to close.
        for mapname, data in maps.items():
            while not data[0].empty():
                cmd = data[0].get() # Get command from map.
                if cmd[0] == "end": # Close map command
                    to_close.append(mapname) # Remove map, should have returned anyways.
                elif cmd[0] == "mov": # Move player command
                    move_requests.append((cmd[1], cmd[2])) # Add move request.

        for mapname in to_close: # Remove closed maps.
            del maps[mapname]

        # Handle move requests.
        for req in move_requests:
            if req[0] in maps:          # Map currently exists
                maps[req[0]][1].put(("add", req[1]))
            else:                       # Map doesn't exist, add map
                name = req[0]
                get = Queue()
                send = Queue()
                proc = Process(target=spawn_map.run_map, args=(name, send, get)) # Create map process
                send.put(("add", req[1]))
                proc.start()
                maps[name] = [get, send]    # Add map to list



# Gives user input to the queue.
def inputter():
    input_queue = Queue()
    proc = Process(target=connector, args=(input_queue,))
    proc.start()
    while True:
        inpt = input()
        input_queue.put(inpt)
        if inpt == "end":
            return

if __name__ == "__main__":
    inputter()