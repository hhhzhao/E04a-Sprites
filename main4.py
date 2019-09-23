#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.blue_4)

        self.poses_list = arcade.SpriteList()


    def setup(self):
        pose = ['action1','action2','back','cheer1','cheer2','climb1','climb2','duck','fall','hang','hold1','hold2','hurt','idle','jump','kick','skid','slide','stand','swim1','swim2','talk','walk1','walk2']

        for i in range (20):
            poses = random.choice(pose)
            x = random.randint(0,800)
            y = random.randint(0,600)
            self.poses_sprite = arcade.Sprite("assets/Poses/adventurer_{poses}.png".format(poses=poses), 0.5)
            self.poses_sprite.center_x = x
            self.poses_sprite.center_y = y
            self.poses_list.append(self.poses_sprite)
        

    def on_draw(self):
        arcade.start_render()
        self.poses_list.draw()


    def update(self, delta_time):
        pass


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()