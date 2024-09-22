import pgzrun
import random

WIDTH = 800
HEIGHT = 600
center_x = WIDTH//2
center_y = HEIGHT//2
center = (center_x, center_y)
final_level = 5
start_speed = 5
ITEMS = ["bag", "battery", "bottle", "chips"]
game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    global game_over, game_complete, current_level, items

    screen.clear()
    screen.blit("bground", (0,0))
    if game_over:
        display_message("Game Over!!!!!", "that sucks to be you.")
    elif game_complete:
        display_message("Game Won!!!!!", "dang. heres a cookie 🍪🍪🍪🍪🍪🍪🍪")

    else:
        for item in items:
            item.draw()


def display_message(heading, subheading):
    screen.draw.text(heading, center = (center_x, (center_y-15)), fontsize = 50, color = ("white"))
    screen.draw.text(subheading,center =  (center_x, (center_y +15)), fontsize =  30, color = ("white"))


def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(num_extra_items):
    items_to_create = get_option_to_create(num_extra_items)

    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items


def get_option_to_create(num_extra_items):

    items_to_create = ["paper"]
    for i in range (num_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items = []                          

    for i in items_to_create:
        item = Actor(i + "img")
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout)+1
    gap_size = WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_x_pos = (index+1)*gap_size
        item.x = new_x_pos


def handle_game_over():
    global game_over
    game_over = True


def handle_game_complete():
    global current_level, final_level, items, game_complete, animations
    stop_animating(animations)
    if current_level == final_level:
        game_complete = True
    else:
        current_level = current_level+1
        items = []


def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def animate_items(actors_to_animate):
    global animations
    for actor in actors_to_animate:
        dur = start_speed-current_level
        actor.anchor = ("center", "bottom")
        animation = animate(actor, duration = dur, on_finished = handle_game_over, y = HEIGHT)
        animations.append(animation)

def stop_animating(actors_to_stop_animating):
    for actor in actors_to_stop_animating:
        if actor.running:
            actor.stop()
        

pgzrun.go()

#Enumerate
#Enumerate is the function that allows you to get both the index number AND the item at the same time, only from a list. 
#Usually for loops only let you get one, but this functions allows both to be done 
#All capital variables
#all capital variables mean that you cannot change the variable, making them impossible to change unless done manually, not able to
#done in any other function
#Lowercase variables
#lowecase variables are able to be changed in another function anytime anywhere, unlike all capital variables

