# get paths of fonts and images
font_path = './font/'
image_path = './img/'

# define fonts and images
ALGER = font_path + 'ALGER.TTF'
ebrima = font_path + 'ebrima.ttf'
AGENCYB = font_path + 'AGENCYB.TTF'

main_page = image_path + 'mainpage.png'
fight = image_path + 'fighting.png'
pause_page = image_path + 'pausepage.png'

pause_button = image_path + 'pausebutton.png'
play_button = image_path + 'play.png'
quit_button = image_path + 'Quit.png'
back_button = image_path + 'back.png'
continue_button = image_path + 'continue.png'
cursor = image_path + 'cursor.png'
title = image_path + 'title.png'

flags = [image_path + 'flag/' + '1.png', image_path + 'flag/' + '2.png', image_path + 'flag/' + '3.png',
         image_path + 'flag/' + '4.png', image_path + 'flag/' + '5.png']

campfires = [image_path + 'campfire/' + '1.png', image_path + 'campfire/' + '2.png']

infantry_attacking = image_path + 'infantry/' + 'attacking.png'
infantry_walking = image_path + 'infantry/' + 'walking.png'
infantry_dying = image_path + 'infantry/' + 'dying.png'

archer_card = image_path + 'archer/' + 'card.png'
archer_idle = image_path + 'archer/' + 'idle.png'
archer_shooting = image_path + 'archer/' + 'shooting.png'
archer_dying = image_path + 'archer/' + 'dying.png'
arrow_image = image_path + 'archer/' + 'arrow.png'

barbarian_attacking = image_path + 'barbarian/' + 'attacking.png'
barbarian_walking = image_path + 'barbarian/' + 'walking.png'
barbarian_dying = image_path + 'barbarian/' + 'dying.png'

shield_card = image_path + 'shield/' + 'card.png'
shield_idle = image_path + 'shield/' + 'idle.png'
shield_attacking = image_path + 'shield/' + 'attacking.png'
shield_dying = image_path + 'shield/' + 'dying.png'

mortar_card = image_path + 'mortar/' + 'card.png'
mortar_image = image_path + 'mortar/' + 'mortar.png'
shell_image = image_path + 'mortar/' + 'shell.png'

# define values
screen_width, screen_height = 1280, 720
screen_center = (screen_width / 2, screen_height / 2)
fps = 60
map_point1, map_point2 = (160, 280), (1060, 680)

flag_size = (70, 140)
campfire_size = (70, 140)

soldier_size = (100, 100)
archer_size = (soldier_size[0], soldier_size[1])
shield_size = (soldier_size[0] * 1.2, soldier_size[1] * 1.2)

infantry_size = (soldier_size[0] * 1.2, soldier_size[1] * 1.2)
barbarian_size = (soldier_size[0] * 1.2, soldier_size[1] * 1.2)

card_size = (125, 150)
arrow_size = (32, 10)
shell_size = (48, 20)
num_row, num_column = 4, 9
rows = [330, 430, 530, 630]

# initialize inventory
init_coin = 5000
init_food = 50

# define soldiers' attribution
my_soldier_type = ['archer', 'shield', 'mortar']
enemy_type = ['infantry', 'barbarian']
num_image = {"infantry": {"walking": 18, "attacking": 12, "dying": 15},
             "archer": {"idle": 12, "shooting": 15, "dying": 15},
             "barbarian": {"walking": 18, "attacking": 12, "dying": 15},
             "shield": {"idle": 18, "attacking": 12, "dying": 15}}

level1 = [[['infantry'], [3]],
          [['infantry', 'barbarian'], [4, 1]],
          [['infantry', 'barbarian'], [6, 2]],
          [['infantry', 'barbarian'], [6, 2]],
          [2, 20, 20, 15]]

# common value
HP_value = {"infantry": 200, "archer": 150, "shield": 500, "barbarian": 150, "swordsman": 300, "cannon": 100}
damage_value = {"infantry": -10, "archer": -18, "shield": -10, "barbarian": -8, "swordsman": -15, "cannon": -30}
attack_interval = {"infantry": 2, "shield": 3, "archer": 2, "barbarian": 1, "swordsman": 2, "cannon": 1}
# my soldier value
cost_value = {"archer": -75, "shield": -100, "mortar": -125, "swordsman": -100}
# attack_range = {"archer": 250, "cannon": 150}
# enemy value
move_speed = {"infantry": 0.75, "barbarian": 1, "swordsman": 0.5}
reward_value = {"infantry": 30, "barbarian": 40, "swordsman": 60}
