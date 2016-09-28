from sys import exit 
from random import randint

class Scene(object):
    
    def enter(self):
        print "This class needs to be attributed a subclass prior to"
        print "implementation"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.start_scene
        last_scene = self.scene_map.next_scene('finale')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        current_scene.enter()

class Death(Scene):
    
    def enter(self):
        print "You are dead."
        print "Game Over."
        exit(1)

class CentralCorridor(Scene):
    
    def enter(self):
        print "Welcome to the space hulk."
        print "The ship is full of monsters and your goal is to get in an"
        print "escape pod down to the planet."
        print "To get there you will need to get a bomb from the armory to"
        print "blow up the ship and stop the aliens pursuing you, get through"
        print "the code lock on the bridge and then find a working escape pod."
        print "Good luck adventurer."
        print "Watch out, there is a space ork coming right for you!"
        print "What do you do?"
        
        action = raw_input("> ")
        
        if action == 'run':
            print "You can run, but you can't hide."
            print "Fight like a man, man!"
            return 'death'
            
        elif action == 'punch':
            print "Unfortunately for you space orks are pretty tough."
            print "It (he?) takes the punch like a champ and then bites your" 
            print "head off!"
            return 'death'
        
        elif action == 'shoot':
            print "You take out your trusty revolver and unload wildly at the"
            print "hurtling ork. It goes down in a flurry of bullets."
            print "However, you don't have any weapons left now so you will"
            print "have to re-arm yourself or use stealth in future."
            return 'laser_weapon_armory'
        
        else:
            print "You don't make sense, bro"
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    
    def enter(self):
        print "You walk into the ship's armory"
        print "to get the bomb that you need to blow up the ship."
        print "However, you are dismayed to see that there are a bunch of"
        print "bad guys all around the bomb."
        return 'the_bridge'

class TheBridge(Scene):
    
    def enter(self):
        print "You enter the bridge."
        print "You do some action."
        print "You exit hurriedly to the escape pods."
        return 'escape_pod'

class EscapePod(Scene):
    
    def enter(self):
        print "You enter the room with the escape pods."
        print "You choose a pod."
        print "Miraculously, it is the correct pod. Well done!"
        return 'finale'

class Finale(Scene):
    
    def enter(self):
        print "You blast out of the space ship watching your bomb detonate"
        print "seconds later. Your ship heads towards the planet below and"
        print "you are safe."
        print "(for now)"

class Map(object):
    
    scenes = {
        'death': Death(),
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'finale': Finale()
        }
    
    def __init__(self, start_scene):
        self.start_scene = Map.scenes.get(start_scene)
    
    def next_scene(self, scene_name):
        next = Map.scenes.get(scene_name)
        return next     ## this return creates an instance of the next room
                        ## the engine will then call the enter method on it

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
