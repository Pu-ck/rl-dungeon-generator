import tcod.event
import tcod
from generate_dungeon import generate_dungeon
from collision import collision
from entities import StairsUp
from entities import Player

# Console width and height
WIDTH = 80
HEIGHT = 60
NUMBER_OF_ROOMS = 35


def main():

    # Console setup
    tileset = tcod.tileset.load_truetype_font(
        path="Px437_IBM_BIOS.ttf", tile_width=12, tile_height=12
    )
    console = tcod.Console(WIDTH, HEIGHT, order="F")

    # Player object
    player = Player(3, 3, "@", (255, 255, 255))

    # Stairs objects
    stairs_down = Player(WIDTH - 3, HEIGHT - 3, "↓", (255, 255, 255))
    stairs_up = StairsUp(3, 3, "↑", (255, 255, 255))

    # Lists for all objects
    room_tile_list = []
    map_tile_list = []
    water_list = []
    wall_list = []
    door_list = []

    # Main loop
    with tcod.context.new(
        columns=console.width, rows=console.height, tileset=tileset
    ) as context:
        while True:

            # Generating new dungeon
            generate_dungeon(
                wall_list,
                door_list,
                room_tile_list,
                map_tile_list,
                water_list,
                WIDTH,
                HEIGHT,
                NUMBER_OF_ROOMS,
                console,
                context,
            )

            while True:
                console.clear()

                # Previous player's coordinates - for collision detection
                current_x = player.position_x
                current_y = player.position_y

                # Controlling player
                player.movement()

                # Player-walls collision detection
                collision(player, wall_list, current_x, current_y)

                # Drawing objects
                for map_tile in map_tile_list:
                    console.print(
                        map_tile.position_x,
                        map_tile.position_y,
                        string=map_tile.char,
                        bg=(0, 0, 32),
                        fg=map_tile.color,
                    )
                for room_tile in room_tile_list:
                    console.print(
                        room_tile.position_x,
                        room_tile.position_y,
                        string=room_tile.char,
                        bg=room_tile.background_color,
                        fg=room_tile.color,
                    )
                for water in water_list:
                    console.print(
                        water.position_x,
                        water.position_y,
                        string=water.char,
                        fg=water.color,
                    )
                for door in door_list:
                    console.print(
                        door.position_x,
                        door.position_y,
                        string=door.char,
                        bg=(0, 0, 32),
                        fg=door.color,
                    )
                for wall in wall_list:
                    console.print(
                        wall.position_x,
                        wall.position_y,
                        string=wall.char,
                        bg=(0, 0, 0),
                        fg=wall.color,
                    )

                console.print(
                    stairs_up.position_x,
                    stairs_up.position_y,
                    string=stairs_up.char,
                    fg=stairs_up.color,
                )
                console.print(
                    stairs_down.position_x,
                    stairs_down.position_y,
                    string=stairs_down.char,
                    fg=stairs_down.color,
                )
                console.print(
                    player.position_x,
                    player.position_y,
                    string=player.char,
                    fg=player.color,
                )

                context.present(console)

                # Player-stairs collision detection
                if (
                    player.position_x == stairs_down.position_x
                    and player.position_y == stairs_down.position_y
                ):
                    break

            # Clearing lists and console, resetting player position
            console.clear()
            map_tile_list.clear()
            wall_list.clear()
            door_list.clear()
            room_tile_list.clear()
            water_list.clear()
            player.position_x = 3
            player.position_y = 3


if __name__ == "__main__":
    main()
