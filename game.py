# Python Text Adventure
# Learn Python the Hard Way

# 

from sys import exit
from random import randint
from Person import Person
import time

class Scene(object):
    
    def __init__(self):
        self.person = Person()

    def enter(self):
        print "This scene is not yet configured. Subclass it amd implement enter()."
        exit(1)
        
    def get_action(self):
        action = raw_input("> ")
        if (action == "exit"):
            exit(0)
            self.get_action()
        elif (action == "read map" and self.person.has_item("map")):
            print " _~_     ___ "
            print "|_L_|---|_r_|"
            print " ___     _|_ "
            print "|_S_|---|_r_|"
            print "         _|_ "
            print "        |_x_|"
            return self.get_action()
        elif (action == "read paper" and self.person.has_item("paper")):
            print "*******"
            print "Hurry to the passage, the machines have"
            print "found us! If you encounter one then use the"
            print "trap we put in place by shouting the password" 
            print "*******" 
            return self.get_action()
        elif (action == "inventory"):
            print self.person.items
            return self.get_action()
        else:
            return action

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print ""
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Start(Scene):

    def enter(self):
        self.print_description()
       
        action = self.get_action()
        while (action != "north"):
            if (action == ""):
                pass
            elif (action == "pick up paper" or action == "read paper" or action == "take paper"):
                self.person.add_item("paper")
                print "You pick up the paper"
            elif action == "look":
                self.print_description()
            else:
                print "I don't understand that. type 'look' to examine surroundings."
            action = self.get_action()

        return 'road_south'

    def print_description(self):
        if (self.person.has_item("paper") == False and self.person.has_item("map") == False):
            print "With a throbbing headache and a bump on the head"
            print "you slowly wake up to find yourself on a deserted road."
        print "The road has weeds growing through the large cracks in the asphalt."
        if (self.person.has_item("paper") == False):
            print "You see a piece of paper on the ground and the"
        print "the road continues to the north."
 

class RoadSouth(Scene):
    
    def enter(self):
        self.print_description()

        action = self.get_action()

        while (action == ""): # action was carried out in parent get_action method
            action = self.get_action()
        if (action == "look"):
            return 'road_south'
        elif (action == "west"):
            return 'store_outside'
        elif (action == "north" and self.person.has_item("robot head") == False):
            return 'road_north'
        elif (action == "north" and self.person.has_item("robot head") == True):
            return 'road_north_dead'
        elif (action == "south"):
            return 'start'
        elif (action == "look"):
            return 'road_south'
        elif (action == "take map" or action == "read map" or action == "pick up map"):
            print "You take the map"
            self.person.add_item("map")
            return 'road_south'
        else:
            print "\nI don't understand that. Type 'commands' to see a list of commands "
            return 'road_south'

    def print_description(self):
        print "The road has become even worse."
        print "To the west you see a convenience store and"
        print "the road continues to the north and south."
        if (self.person.has_item("map") == False): 
           print "A map of some sort is wedged in a crack in the road."

class StoreOutside(Scene):
    
    def enter(self):
        self.print_description()
        action = self.get_action()

        while (action == ""): # action was carried out in parent get_action method
            action = self.get_action()
        if (action == "east"):
            return 'road_south'
        elif (action == "press button" or action == "push button"):
            return self.play_riddle()
        else:
            print "I don't understand that. Type 'commands' to get a list of commands."
            return 'store_outside'
        
    def play_riddle(self):
        print "An electronic voice says"
        print "\"The baker cooks a dozen and a score. Two are burned, how many are edible?\""
        print "(answer correctly or end puzzle by walking east)"
        while (True):
            answer = int(raw_input("[answer]> "))
            if (answer == 31):
                print "The door opens with a hiss and you walk in"
                return 'store_inside'
            elif (answer == "east"):
                return 'store_outside'            
            else:
                print "ERR"
            

    def print_description(self):
        print "The store looks well stocked" 
        print "however it appears to be locked up tight." 
        print "There is a button beside the door."
        print "The road can be seen to the east."

class StoreInside(Scene):

    def enter(self):
        self.print_description()
        action = self.get_action()
        
        while (action == ""): # action was carried out in parent get_action method
            action = self.get_action()
        if (action == "take rifle" or action == "get rifle" or action == "pick up rifle"):
            print "You take the rifle and load the bullet"
            self.person.add_item("rifle")
            self.person.add_item("bullet")
            return 'store_inside'
        elif (action == "east"):
            return 'store_outside'
        elif ("food" in action):
            print "Thousands of cans of food and no can opener..."
            return 'store_inside'
        else:
            print "I don't understand that. type 'commands' for a list of commands"
            return 'store_inside'

        


    def print_description(self):
        print "The store contains shelves of food and supplies."
        if (self.person.has_item("rifle") == False):
            print "On the counter lies a rifle with one bullet"
        print "Sun shines through the exit door to the east"
        

class RoadNorth(Scene):

    def enter(self):
        self.print_description()

        action = self.get_action()
        
        while (action == ""): # action was carried out in parent get_action method
            action = self.get_action()
        print action
        if (action == "shoot rope"):
            print "What do you shoot it with?"
            action = self.get_action()
        if (action == "shoot rope with rifle" and self.person.has_item("rifle") == True):
            print "As the robot raises its gun to mow you down"
            print "you quickly raise your rifle and shoot the rope that"
            print "holds the metal box in place. The box drops on the"
            print "robot crushing it seconds before it would have killed you."
            self.person.add_item("robot head")
            return 'road_north_dead'
        elif (action == "shout"):
            print "shout what?"
        elif (action == "shout the password"):
            print "The red light turns green on the box and"
            print "a grenade drops out of the bottom. The grenade"
            print "explodes on the robot throwing metal and fire"
            print "all around. You are thrown back but remain"
            print "relatively unscathed."
            self.person.add_item("robot head")
            return 'road_north_dead'
        elif (action == "south"):
            return 'road_south'
        else:
            print "The robot raises its gun and shoots you in the face"
            replay = raw_input("replay y/n? ")
            while (replay == "y" or replay == "n"):
                if (replay == "y"):
                    self.person.remove_all()
                    return 'start'
                elif (replay == "n"):
                    print "goodbye"
                    exit(0)
                        
    def print_description(self):
        print "As you walk north, suddenly from behind a"
        print "building a robot walks out. It is twice as tall"
        print "as a normal human and is holding a machine-gun."
        print "Directly above the robot is a metal box with a"
        print "blinking red light hanging by a rope"
            


class RoadNorthDead(Scene):

    def enter(self):
        self.print_description()
        
        action = self.get_action()
        while (action == ""): # action was carried out in parent get_action method
            action = self.get_action()
        if (action == "west"):
            return 'library'
        elif (action == "south"):
            return 'road_south'
        else:
            print "I don't understand that. type 'inventory' to see what you're carrying"
            return 'road_north_dead'
        

    def print_description(self):
        print "With a shudder you think of how close"
        print "you came to being killed by the machine."
        print "The road continues to the south and to"
        print "the west a library can be seen."
        print "You can hear a dull roar coming nearer that"
        print "sounds like metallic marching"



class Library(Scene):
    
    def enter(self):
        if (self.person.has_item("rug") != True):
            self.print_description()
            

        action = self.get_action()

        while (action == ""): # action was carried out in parent get_action method
            action = self.get_action()
        if ("Guide" in action):
            print "An electronic voice says:"
            print "What is the answer to the ultimate question of life, the universe, and everything?"
            answer = raw_input("[answer]> ")
            if (int(answer) == 42):
                print "Correct!"
                self.person.add_item("Hitchhiker's Guide to the Galaxy")
                return 'passage'
            else:
                print "Wrong!"
                self.print_description_rug()
                return 'library'
        elif (action == "move rug" or action == "lift rug"):
            self.person.add_item("rug")
            print "You move the rug to reveal a trapdoor underneath"
            return 'library'
        elif ((action == "open trapdoor" or action == "lift trapdoor") and self.person.has_item("rug") == True):
            print "You lift the trapdoor and descend into the darkness..."
            return 'under_library'
        elif (action == "east"):
            print "You walk outside to find yourself surrounded by"
            print "deadly looking robots. They raise their guns simultaneously"
            print "and blow you into pieces no larger than a quarter."
            replay = raw_input("replay y/n? ")
            while (replay == "y" or replay == "n"):
                if (replay == "y"):
                    self.person.remove_all()
                    return 'start'
                elif (replay == "n"):
                    print "goodbye"
                    exit(0)
        
        else:
            print "I don't understand that."
            return 'library'
            
        
    
    def print_description(self):
        print "You walk into a dusty room with books strewn about everywhere."
        print "A rug lies in the middle of the room and on a bookshelf lies"
        print "a lone copy of \"The Hitchhiker's Guide to the Galaxy\"."
        print "The marching to the east has now become an ear splitting roar."
    def print_description_rug(self):
        print "In the middle of the room lies a trapdoor"
        print "On a shelf lies a loan copy of  \"The Hitchhiker's Guide to the Galaxy\"."


class Passage(Scene):

    def enter(self):
        self.print_description()
        
        action = self.get_action()

        return 'passage'

    def print_description(self):
        print "The bookshelf opens to reveal a passage behind it."
        print "You walk in and the shelf closes behind you."
        time.sleep(1)
        print "..."
        time.sleep(5)
        print "Suddenly a flashlight turns on and a voice whispers"
        print "\"Glad you made it. We are ready to explode the mines"
        print "that we have in place for the machines.\"\n"
        time.sleep(5)
        print "You hear a set of explosions outside the library"
        print "and the roar of the marching machines dies away.\n"
        time.sleep(5)
        print "\n*****\nYou win!\n*****\n"
        exit(0)
        

class UnderLibrary(Scene):

    def enter(self):
        self.print_description()

        action = self.get_action()

        while (action == ""): # action was carried out in parent get_action method
            action = self.get_action()
        if (action == "read sign" or action == "look at sign"):
            print "The sign reads:"
            print "    in 1998 the government buried an atomic bomb"
            print "    beneath the General Store in town."
            print "    This button detonates the bomb, which will destroy"
            print "    the entire town and all of its occupants."
            print "    Only those in this bunker can survive the bomb blast."
            print "    It is your decision whether to press the button or not."
            action = raw_input("press button? > ")
            if (action == "yes" or action == "y"):
                print "You slowly press the button and listen as an explosion"
                print "shakes the bunker. You put on the suit and climb the stairs."
                print "You walk out into a desert wasteland with no man-made materials"
                print "in sight."
                print "\n*****\nYou win!\n*****\n"
                exit(0)
            elif (action == "no" or action == "n"):
                print "You hear a crash and suddenly robots"
                print "start descending into the bunker."
                print "They raise their guns and kill you."
                print "\n*****\nYou lose!\n*****\n"
                exit(0)
        elif (action == "press button"):
            print "You should read the sign first."
            return 'under_passage'
        else:
            print "I don't understand that."
            return 'under_passage'

    def print_description(self):
        print "You stumble in the pitch black until you find"
        print "a light switch. Flipping it on reveals a bare"
        print "cement room that looks like a bunker."
        print "In a corner lies what appears to be a hazardous waste suit."
        print "On one wall a large red button can be seen with a sign"
        print "next to it."

class Map(object):
    
    scenes = {
        'start': Start(),
        'road_south': RoadSouth(),
        'road_north': RoadNorth(),
        'road_north_dead': RoadNorthDead(),
        'store_outside': StoreOutside(),
        'store_inside': StoreInside(),
        'library': Library(),
        'passage': Passage(),
        'under_library': UnderLibrary()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('start')
a_game = Engine(a_map)
a_game.play()
