import time
import traceback

import world

# Runs the map with the given name and given queues
def run_map(map_name, get, send):
    try:
        world.load(map_name.split(';')[0]) # Only load everything before first ;
    
        print("Map " + map_name + " started")
        start_time = time.time()
        since_start = 0
    
        while True:
            # Calculate delta time
            delta_time = int((time.time() - start_time) * 1000) - since_start
            if delta_time > 100:
                delta_time = 100
            since_start += delta_time
    
            # Check queue for new messages.
            if not get.empty():
                message = get.get()

                if message[0] == "add": # We're adding a player
                    message[1].attributes["current_map"] += 1 # Count how many maps a player's been in.
                    if message[1].attributes["current_map"] > 255: # Reset once we get past a byte
                        message[1].attributes["current_map"] = 1
    
                    world.players.append(message[1])
                    print("Player added to map " + map_name)
                if message[0] == "end": # Forcibly end map
                    for plr in world.players:
                        plr.attributes["socket"].close()
                    return
            if world.players == []: # No players left
                send.put(("end", ))
                print("Ending map " + map_name)
                return
    
            world.to_del = []
            world.to_del_plr = []
    
            # Update objects
            for index in range(len(world.objects + world.players)):
                obj = (world.objects + world.players)[index]
    
                # Update it
                if obj.update(delta_time) is not None:
                    new_map_loaded = True
                for coll in world.objects[index + 1:]:    # Check for collision
                    if coll.X == obj.X and coll.Y == obj.Y:
                        obj.collide(coll) # Call collisions
                        coll.collide(obj)
    
                #Check if out of bounds
                if world.out_of_bounds(obj.X, obj.Y):
                    world.to_del.append(obj)
    
            # Delete objects that need to be deleted.
            for obj in set(world.to_del): # Set to remove duplicates
                world.objects.remove(obj)
    
            # Remove players that left
            for plr in world.to_del_plr:
                world.players.remove(plr)
    
            # Send data to players.
            # We need (#objects + # players) things to send.
            # Each thing needs an X coord, Y coord, char, and color
            # We devote 1 byte to each, meaning each is 4 bytes
            # Additionally, we need a 1 byte header. Header is 0 for update data
            send_data = bytearray(2 + (len(world.objects) + len(world.players) ) * 4)
            index = 2 # Where to start adding info for next object
            send_data[1] = len(world.objects) + len(world.players)
            for obj in world.objects + world.players: # Loop through objects, get data.
                send_data[index] = obj.X
                index += 1
                send_data[index] = obj.Y
                index += 1
                send_data[index] = ord(obj.char())
                index += 1
                send_data[index] = obj.color()
                index += 1
    
            # Send update to all players
            for plr in world.players:
                plr.attributes["socket"].sendto(send_data + plr.extra_data(), plr.attributes["address"])
                
    except Exception as ex:
        send.put(("end", ))
        print("Ending map " + map_name + " due to error (", ex, ")")
        print( traceback.format_exc())


    
