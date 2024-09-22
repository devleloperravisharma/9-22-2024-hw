import pgzrun
import random

WIDTH = 800
HEIGHT = 800
center_x = WIDTH//2
center_y = HEIGHT//2
center = (center_x, center_y)
final_alley = 5
start_speed = 7
CATS = ["tabby", "brown", "grey", "regular"]
game_over = False
game_complete = False
current_alley = 1
cats = []
animations = []

def draw():
    global game_over, game_complete, current_alley, cats

    screen.clear()
    screen.blit("alleyway", (0,0))
    if game_over:
        display_message("Game Over!!", "NO WHY DID YOU LOOSE THE POOR KITTY")
    elif game_complete:
        display_message("Game Won!!!!!!!!!!!!!!!", "YAYYYY KITTYYYYYYYYYY")

    else:
        for cat in cats:
            cat.draw()


def display_message(heading, subheading):
    screen.draw.text(heading, center = (center_x, (center_y-15)), fontsize = 50, color = ("brown"))
    screen.draw.text(subheading,center =  (center_x, (center_y +15)), fontsize =  30, color = ("brown"))


def update():
    global cats
    if len(cats) == 0:
        cats = make_cats(current_alley)

def make_cats(num_extra_cats):
    cats_to_create = get_option_to_create(num_extra_cats)

    new_cats = create_cats(cats_to_create)
    layout_the_cats(new_cats)
    animate_cats(new_cats)
    return new_cats



def get_option_to_create(num_extra_cats):

    cats_to_create = ["calico"]
    for i in range (num_extra_cats):
        random_option = random.choice(CATS)
        cats_to_create.append(random_option)
    return cats_to_create



def create_cats(cats_to_create):
    new_cats = []                          

    for i in cats_to_create:
        cat = Actor(i + "img")
        new_cats.append(cat)
    return new_cats

def layout_the_cats(cats_to_layout):
    number_of_gaps = len(cats_to_layout)+1
    gap_size = HEIGHT/number_of_gaps
    random.shuffle(cats_to_layout)
    for index, cat in enumerate(cats_to_layout):
        new_y_pos = (index+1)*gap_size
        cat.y = new_y_pos

def game_is_over():
    global game_over
    game_over = True


def game_is_complete():
    global current_alley, final_alley, cats, game_complete, animations
    stop_animating_cats(animations)
    if current_alley == final_alley:
        game_complete = True
    else:
        current_alley = current_alley+1
        cats = []

def on_mouse_down(pos):
    global cats, current_alley
    for cat in cats:
        if cat.collidepoint(pos):
            if "calico" in cat.image:
                game_is_complete()
            else:
                game_is_over()



def animate_cats(cats_to_animate):
    global animations
    for cat in cats_to_animate:
        durationn = start_speed-current_alley
        cat.anchor = ("center", "bottom")
        animation = animate(cat, duration = durationn, on_finished = game_is_complete, x = WIDTH)
        animations.append(animation)

def stop_animating_cats(cats_to_stop_animating):
    for cat in cats_to_stop_animating:
        if cat.running:
            cat.stop()
pgzrun.go()
