# get paths of fonts and images
font_path = './font/'
image_path = './img/'
ui_path = image_path + 'ui/'
cha_path = image_path + 'character/'

# define fonts and images
ALGER = font_path + 'ALGER.TTF'
ebrima = font_path + 'ebrima.ttf'
AGENCYB = font_path + 'AGENCYB.TTF'

# ui
main_page = ui_path + 'mainpage.png'
fight = ui_path + 'fighting.png'
pause_page = ui_path + 'pausepage.png'
pause_button = ui_path + 'pausebutton.png'
play_button = ui_path + 'play.png'
quit_button = ui_path + 'Quit.png'
back_button = ui_path + 'back.png'
continue_button = ui_path + 'continue.png'
cursor = ui_path + 'cursor.png'
title = ui_path + 'title.png'
coin_box = ui_path + 'coin_box.png'

# ornament
flags = [image_path + 'flag/' + '1.png', image_path + 'flag/' + '2.png', image_path + 'flag/' + '3.png',
         image_path + 'flag/' + '4.png', image_path + 'flag/' + '5.png']
campfires = [image_path + 'campfire/' + '1.png', image_path + 'campfire/' + '2.png']

# action
attacking_images = {
    'INFANTRY': cha_path + 'infantry/' + 'attacking.png',
    'ARCHER': cha_path + 'archer/' + 'shooting.png',
    'VIKING': cha_path + 'viking/' + 'attacking.png',
    'BARBARIAN': cha_path + 'barbarian/' + 'attacking.png',
    'SHIELD': cha_path + 'shield/' + 'attacking.png',
    'OGRE': cha_path + 'ogre/' + 'attacking.png',
    'ELEMENTALS': cha_path + 'elementals/' + 'attacking.png',
    'FAIRY': cha_path + 'fairy/' + 'healing.png',
    'MASKER': cha_path + 'masker/' + 'attacking.png',
    'ARCHMAGE': cha_path + 'archmage/' + 'attacking.png',
    'MANIPULATOR': cha_path + 'manipulator/' + 'attacking.png',
    'MINER': cha_path + 'miner/' + 'attacking.png'
}
dying_images = {
    'INFANTRY': cha_path + 'infantry/' + 'dying.png',
    'ARCHER': cha_path + 'archer/' + 'dying.png',
    'VIKING': cha_path + 'viking/' + 'dying.png',
    'BARBARIAN': cha_path + 'barbarian/' + 'dying.png',
    'SHIELD': cha_path + 'shield/' + 'dying.png',
    'OGRE': cha_path + 'ogre/' + 'dying.png',
    'ELEMENTALS': cha_path + 'elementals/' + 'dying.png',
    'FAIRY': cha_path + 'fairy/' + 'dying.png',
    'MASKER': cha_path + 'masker/' + 'dying.png',
    'ARCHMAGE': cha_path + 'archmage/' + 'dying.png',
    'MANIPULATOR': cha_path + 'manipulator/' + 'dying.png',
    'MINER': cha_path + 'miner/' + 'dying.png'
}
idle_images = {
    'INFANTRY': cha_path + 'infantry/' + 'idle.png',
    'ARCHER': cha_path + 'archer/' + 'idle.png',
    'SHIELD': cha_path + 'shield/' + 'idle.png',
    'FAIRY': cha_path + 'fairy/' + 'idle.png',
    'ARCHMAGE': cha_path + 'archmage/' + 'idle.png',
    'MANIPULATOR': cha_path + 'manipulator/' + 'idle.png',
    'MINER': cha_path + 'miner/' + 'hurt.png'
}
walking_images = {
    'VIKING': cha_path + 'viking/' + 'walking.png',
    'BARBARIAN': cha_path + 'barbarian/' + 'walking.png',
    'OGRE': cha_path + 'ogre/' + 'walking.png',
    'ELEMENTALS': cha_path + 'elementals/' + 'walking.png',
    'MASKER': cha_path + 'masker/' + 'walking.png'
}
ability_images = {
    'ELEMENTALS': cha_path + 'elementals/' + 'run_attacking.png',
    'MASKER': cha_path + 'masker/' + 'sliding.png'
}

king_path = cha_path + 'king/'
king_image = [{'idle': king_path + 'king1/' + 'idle.png', 'attacking': king_path + 'king1/' + 'attacking.png',
               'dying': king_path + 'king1/' + 'dying.png'},
              {'idle': king_path + 'king2/' + 'idle.png', 'attacking': king_path + 'king2/' + 'attacking.png',
               'dying': king_path + 'king2/' + 'dying.png'},
              {'idle': king_path + 'king3/' + 'idle.png', 'attacking': king_path + 'king3/' + 'attacking.png',
               'dying': king_path + 'king3/' + 'dying.png'}]

# card
card_path = image_path + 'card/'
miner_card = card_path + 'miner.png'
infantry_card = card_path + 'infantry.png'
archer_card = card_path + 'archer.png'
shield_card = card_path + 'shield.png'
mortar_card = card_path + 'mortar.png'
fairy_card = card_path + 'fairy.png'
archmage_card = card_path + 'archmage.png'
manipulator_card = card_path + 'manipulator.png'

# preview
preview_path = image_path + 'preview/'
pre_paths = {'INFANTRY': preview_path + 'infantry.png',
             'ARCHER': preview_path + 'archer.png',
             'SHIELD': preview_path + 'shield.png',
             'FAIRY': preview_path + 'fairy.png',
             'ARCHMAGE': preview_path + 'archmage.png',
             'MANIPULATOR': preview_path + 'manipulator.png',
             'MINER': preview_path + 'miner.png'}

# object
obj_path = image_path + 'object/'
coin_image = obj_path + 'coin.png'
arrow_image = obj_path + 'arrow.png'
shell_image = obj_path + 'shell.png'
elementals_slash = obj_path + 'slash.png'
fairy_spells = obj_path + 'fairy_spells.png'
big_spells = obj_path + 'big_spells.png'
vector_spells = obj_path + 'vector_spells.png'

# unfinished
mortar_image = cha_path + 'mortar/' + 'mortar.png'

# ui and map
screen_width, screen_height = 1280, 720
screen_center = (screen_width / 2, screen_height / 2)
map_point1, map_point2 = (160, 280), (1060, 680)
campfire_x, campfire_y = 30, [380, 580]
coin_box_pos = (100, 100)
num_row, num_column = 4, 9
rows = [330, 430, 530, 630]

# fps
fps = 60

# size
flag_size = (65, 130)
campfire_size = (65, 130)
character_size = (100, 100)
tower_size = {'ARCHER': (character_size[0], character_size[1]),
              'SHIELD': (character_size[0] * 1.3, character_size[1] * 1.3),
              'INFANTRY': (character_size[0] * 1.2, character_size[1] * 1.2),
              'FAIRY': (character_size[0], character_size[1]),
              'ARCHMAGE': (character_size[0], character_size[1]),
              'MANIPULATOR': (character_size[0], character_size[1]),
              'MINER': (character_size[0], character_size[1])}
king_size = (character_size[0] * 1.2, character_size[1] * 1.2)

enemy_size = {'VIKING': (character_size[0] * 1.2, character_size[1] * 1.2),
              'BARBARIAN': (character_size[0] * 1.2, character_size[1] * 1.2),
              'OGRE': (character_size[0] * 1.4, character_size[1] * 1.2),
              'ELEMENTALS': (character_size[0] * 1.2, character_size[1] * 1.2),
              'MASKER': (character_size[0] * 1.2, character_size[1] * 1.2)}
card_size = (130, 155)
arrow_size = (32, 10)
shell_size = (48, 20)
slash_size = (50, 50)
spells_size = (25, 25)
coin_box_size = (160, 45)
coin_size = (50, 50)

# initialize inventory
init_coin = 5000
init_food = 50

VIKING, BARBARIAN, OGRE, ELEMENTALS, MASKER = 'VIKING', 'BARBARIAN', 'OGRE', 'ELEMENTALS', 'MASKER'

# level
level1 = [[[VIKING, BARBARIAN, OGRE, ELEMENTALS, MASKER], [1, 1, 1, 1, 1], 2],
          [[OGRE, ELEMENTALS], [2, 1], 10],
          [[BARBARIAN, VIKING], [2, 2], 10],
          [[MASKER, ELEMENTALS], [2, 2], 15],
          None]

# define soldiers' attribution
tower_type = ['INFANTRY', 'ARCHER', 'SHIELD', 'FAIRY', 'ARCHMAGE', 'MANIPULATOR', 'MINER', 'MORTAR', 'KING']
enemy_type = ['VIKING', 'BARBARIAN', 'OGRE', 'ELEMENTALS', 'MASKER']
num_image = {
    "INFANTRY": {"idle": 12, "attacking": 12, "dying": 15},
    "ARCHER": {"idle": 12, "shooting": 15, "dying": 15},
    'KING': {"idle": 12, "attacking": 12, "dying": 15},
    "BARBARIAN": {"walking": 18, "attacking": 12, "dying": 9},
    'VIKING': {"walking": 18, "attacking": 12, "dying": 15},
    "SHIELD": {"idle": 18, "attacking": 12, "dying": 15},
    'OGRE': {"walking": 18, "attacking": 12, "dying": 15},
    'ELEMENTALS': {"walking": 24, "attacking": 12, "dying": 15, "run_attacking": 12},
    'FAIRY': {"idle": 12, "attacking": 12, "dying": 15},
    'MASKER': {"walking": 24, "attacking": 12, "dying": 15, "sliding": 6},
    'ARCHMAGE': {"idle": 12, "attacking": 12, "dying": 15},
    'MANIPULATOR': {"idle": 12, "attacking": 12, "dying": 15},
    'MINER': {"idle": 12, "attacking": 12, "dying": 15}
}
# common value
HP_value = {"INFANTRY": 150, "ARCHER": 150, "SHIELD": 500, "VIKING": 300, "BARBARIAN": 150,
            'OGRE': 600, 'KING': 150, 'ELEMENTALS': 200, 'FAIRY': 150, 'MASKER': 200,
            'ARCHMAGE': 150, 'MANIPULATOR': 200, 'MINER': 200}
damage_value = {"INFANTRY": -5, "ARCHER": -15, "SHIELD": -10, "VIKING": -10, "BARBARIAN": -8,
                'OGRE': -5, 'KING': -10, 'ELEMENTALS': -15, 'FAIRY': 8, 'MASKER': -12,
                'ARCHMAGE': -10, 'MANIPULATOR': -5, 'MINER': 0}
attack_range = {"ELEMENTALS": 500, 'ARCHMAGE': 600}
# my soldier value
cost_value = {"INFANTRY": -50, "ARCHER": -100, "SHIELD": -175, 'FAIRY': -175, 'ARCHMAGE': -300,
              'MANIPULATOR': -150, "MORTAR": -750, 'MINER': -50}
cd_value = {"INFANTRY": 1, "ARCHER": 1, "SHIELD": 1, 'FAIRY': 1, 'ARCHMAGE': 1, 'MANIPULATOR': 1,
            'MINER': 1, "MORTAR": 30}
cd_init = {"INFANTRY": True, "ARCHER": True, "SHIELD": True, 'FAIRY': True, 'ARCHMAGE': True,
           'MANIPULATOR': True, 'MINER': True, "MORTAR": False}
# enemy value
move_speed = {"VIKING": 0.8, "BARBARIAN": 1.2, 'OGRE': 0.6, 'ELEMENTALS': 0.75, 'MASKER': 0.8}
reward_value = {"VIKING": 30, "BARBARIAN": 40, 'OGRE': 60, 'ELEMENTALS': 100, 'MASKER': 50}
