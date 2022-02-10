from entities import Wall, MapTile, Water, RoomTile, Door
import random

# Generate random dungeon
def generate_dungeon(
    wall_list,
    door_list,
    room_tile_list,
    map_tile_list,
    water_list,
    width,
    height,
    number_of_rooms,
    console,
    context,
):

    # Create map tiles
    for x in range(width):
        for y in range(width):

            # Randomize symbol and color
            random_char = random.randint(1, 100)

            if random_char < 99:
                char = "."
                color = (100, 100, 100)
            elif random_char == 99:
                char = "o"
                color = (160, 160, 160)
            elif random_char == 100:
                char = '"'
                color = (0, 180, 0)

            if random.randint(0, 250) == 250:
                char = "I"
                color = (190, 190, 190)

            # Map tile object
            map_tile = MapTile(x, y, char=char, color=color)
            map_tile_list.append(map_tile)

            # Randomize water pool position and size
            if random.randint(0, 300) == 300:
                for i in range(random.randint(3, 10)):
                    water = Water(
                        x + random.randint(-1, 1),
                        y + random.randint(-1, 1),
                        char="≈",
                        color=(0, 200, 240),
                    )
                    water_list.append(water)

    generated_room = 0

    # Generate rooms
    for i in range(number_of_rooms):

        # Randomize room position
        position_x = random.randint(0, width)
        position_y = random.randint(0, height)

        # Randomize room size
        size_x = random.randint(5, 14)
        size_y = random.randint(5, 14)

        # Randomize number of doors in room
        number_of_doors = random.randint(1, 3)

        # Change position if room is being drawn outside of map borders or inside another room
        for room_tile in room_tile_list:
            while (
                position_x == room_tile.position_x
                and position_y == room_tile.position_y
                or position_x + size_x > width - 3
                or position_y + size_y > height - 3
                or position_x < 3
                or position_y < 3
            ):
                position_x = random.randint(0, width)
                position_y = random.randint(0, height)

        # Create rooms tiles
        background_color = (0, 0, random.randint(32, 60))
        for x in range(1, size_x):
            for y in range(1, size_y):

                # Randomize symbol and color
                random_char = random.randint(1, 100)

                if random_char < 99:
                    char = "."
                    color = (100, 100, 100)
                elif random_char == 99:
                    char = "o"
                    color = (160, 160, 160)
                elif random_char == 100:
                    char = '"'
                    color = (0, 180, 0)

                if random.randint(0, 250) == 250:
                    char = "I"
                    color = (190, 190, 190)

                # Room tile object
                room_tile = RoomTile(
                    x + position_x,
                    y + position_y,
                    char,
                    color=color,
                    background_color=background_color,
                )
                room_tile_list.append(room_tile)

        # Randomize door position for X walls
        door_postition = random.randint(1, size_x - 1)

        # Create walls
        # Upper X wall
        for i in range(0, size_x):
            random_color = random.randint(80, 150)
            wall = Wall(
                position_x + i,
                position_y,
                "▓",
                color=(random_color, random_color, random_color),
            )

            if i == door_postition and number_of_doors > 0:
                door = Door(position_x + i, position_y, char="═", color=(119, 49, 0))
                door_list.append(door)
                number_of_doors -= 1
                continue

            wall_list.append(wall)

        # Randomize door position for X walls
        door_postition = random.randint(1, size_x - 1)

        # Lower X wall
        for i in range(0, size_x):
            random_color = random.randint(80, 150)
            wall = Wall(
                position_x + i,
                position_y + size_y,
                "▓",
                color=(random_color, random_color, random_color),
            )

            if i == door_postition and number_of_doors > 0:
                door = Door(
                    position_x + i, position_y + size_y, char="═", color=(119, 49, 0)
                )
                door_list.append(door)
                number_of_doors -= 1
                continue

            wall_list.append(wall)

        # Randomize door position for Y walls
        door_postition = random.randint(1, size_y - 1)

        # Left Y wall
        for i in range(0, size_y):
            random_color = random.randint(80, 150)
            wall = Wall(
                position_x,
                position_y + i,
                "▓",
                color=(random_color, random_color, random_color),
            )

            if i == door_postition and number_of_doors > 0:
                door = Door(position_x, position_y + i, char="║", color=(119, 49, 0))
                door_list.append(door)
                number_of_doors -= 1
                continue

            wall_list.append(wall)

        # Randomize door position for Y walls
        door_postition = random.randint(1, size_y - 1)

        # Right Y wall
        for i in range(0, size_y + 1):
            random_color = random.randint(80, 150)
            wall = Wall(
                position_x + size_x,
                position_y + i,
                "▓",
                color=(random_color, random_color, random_color),
            )

            if i == door_postition and number_of_doors > 0:
                door = Door(
                    position_x + size_x, position_y + i, char="║", color=(119, 49, 0)
                )
                door_list.append(door)
                number_of_doors -= 1
                continue

            wall_list.append(wall)

        # Connect overlapping rooms
        for room_tile in room_tile_list:
            for wall in wall_list:
                if (
                    wall.position_x == room_tile.position_x
                    and wall.position_y == room_tile.position_y
                ):
                    wall_list.remove(wall)

        # Remove unnecessary doors
        for room_tile in room_tile_list:
            for door in door_list:
                if (
                    door.position_x == room_tile.position_x
                    and door.position_y == room_tile.position_y
                ):
                    door_list.remove(door)

        generated_room += 1

        # Loading progress bar
        console.print(32, 28, string="Generating dungeon")
        console.print(22 + generated_room, 30, string="▀")
        context.present(console)

    # Create map border walls
    # Upper X wall
    for i in range(0, width):
        random_color = random.randint(80, 150)
        wall = Wall(0 + i, 0, "▓", color=(random_color, random_color, random_color))
        wall_list.append(wall)
    # Lower X wall
    for i in range(0, width):
        random_color = random.randint(80, 150)
        wall = Wall(
            0 + i, 0 + height - 1, "▓", color=(random_color, random_color, random_color)
        )
        wall_list.append(wall)
    # Left Y wall
    for i in range(0, height - 1):
        random_color = random.randint(80, 150)
        wall = Wall(0, 0 + i, "▓", color=(random_color, random_color, random_color))
        wall_list.append(wall)
    # Right Y wall
    for i in range(0, height):
        random_color = random.randint(80, 150)
        wall = Wall(
            0 + width - 1, 0 + i, "▓", color=(random_color, random_color, random_color)
        )
        wall_list.append(wall)

    # Check if map tile is occupied by wall/door
    for map_tile in map_tile_list:
        for wall in wall_list:
            if (
                map_tile.position_x == wall.position_x
                and map_tile.position_y == wall.position_y
            ):
                map_tile.is_occupied = True

        for door in door_list:
            if (
                map_tile.position_x == door.position_x
                and map_tile.position_y == door.position_y
            ):
                map_tile.is_occupied = True

    neighbor_walls_number = 0

    # Check if doors aren't blocked by another door or wall, if so, remove the door and fill the hole with a wall
    for door in door_list:
        for map_tile in map_tile_list:
            if (
                map_tile.position_x == door.position_x + 1
                and map_tile.position_y == door.position_y
                and map_tile.is_occupied == True
            ):
                neighbor_walls_number += 1
            if (
                map_tile.position_x == door.position_x - 1
                and map_tile.position_y == door.position_y
                and map_tile.is_occupied == True
            ):
                neighbor_walls_number += 1
            if (
                map_tile.position_y == door.position_y + 1
                and map_tile.position_x == door.position_x
                and map_tile.is_occupied == True
            ):
                neighbor_walls_number += 1
            if (
                map_tile.position_y == door.position_y - 1
                and map_tile.position_x == door.position_x
                and map_tile.is_occupied == True
            ):
                neighbor_walls_number += 1

        if neighbor_walls_number > 2:
            door_list.remove(door)
            random_color = random.randint(110, 170)
            wall = Wall(
                door.position_x,
                door.position_y,
                "▓",
                color=(random_color, random_color, random_color),
            )
            wall_list.append(wall)

        neighbor_walls_number = 0
