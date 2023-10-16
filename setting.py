# get paths of fonts and images
font_path = './Wargame/font/'
image_path = './Wargame/img/'

# define fonts and images
ALGER = font_path + 'ALGER.TTF'
ebrima = font_path + 'ebrima.ttf'
Home = image_path + 'home.png'
fight = image_path + 'fighting.png'
setting = image_path + 'setting.png'
play_button = image_path + 'play.png'
infantry_card = image_path + 'myinfantrycard.png'
infantry_attack = image_path + 'infantry_attack.png'
pause_button = image_path + 'pausebutton.png'

# define values
screen_width, screen_height = 1280, 720
screen_center = (screen_width / 2, screen_height / 2)
fps = 60

# initialize inventory
init_coin = 500
init_food = 50

# define soldiers' attribution
HP = {"infantry": 200, "Swordsman": 300, "Archer": 150, "Cannon": 100, "ShieldBearer": 500}
cost = {"infantry": -50, "Swordsman": -100, "Archer": -75, "Cannon": -125, "ShieldBearer": -100}
attack = {"infantry": 50, "Swordsman": 75, "Archer": 100, "Cannon": 150, "ShieldBearer": 25}
defense = {"infantry": 10, "Swordsman": 15, "Archer": 5, "Cannon": 5, "ShieldBearer": 25}
move_speed = {"infantry": 1, "Swordsman": 1, "Archer": 0, "Cannon": 0, "ShieldBearer": 0}
attack_speed = {"infantry": 1, "Swordsman": 1, "Archer": 1, "Cannon": 0.5, "ShieldBearer": 0.25}
attack_range = {"infantry": 1, "Swordsman": 1, "Archer": 5, "Cannon": 3, "ShieldBearer": 1}