# get paths of fonts and images
font_path = './font/'
image_path = './img/'

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
HP = {"infantry": 200, "": 100}
cost = {"infantry": -50}
attack = {}