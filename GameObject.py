import string
from Physics.PhysicsEngine import PhysicsEngine
from Rendering.RenderEngine import RenderEngine
from imports import *
from HelperClasses import *

# This is what a user will instantiate whenever they want to generate an 'entity'
# Game object holds a positional value

# The game object shall not have an 'update' function, since it's  components are tracked by their
#     respective engines, the game object mainly allows for a layer of abstraction for the game manager
#     such that it groups the components under a single transform. It also allows for grouping via tags or other potential features
#     which will allow for the game manager to query for a group of objects or define interactions

# One (potential) thing to add is to allow for any amount of components per object. Each component also carries its own
#     relative position to the object. Look into this in the future
class GameObject:
    # each game object has a pointer to the render and physics engine. May not be the best idea, but allows them to make 
    def __init__(self, name : string, renderEngine : RenderEngine, physicsEngine : PhysicsEngine, transform : Transform):
        self.name = name
        self.transform : Transform = transform
        self.renderEngine = renderEngine
        self.physicsEngine = physicsEngine
        self.renderObject = None
        self.physicsObject = None
        # Tags are used to group and select multiple objects
        self.tags = {} 

    # does it make sense to allow the game object to have direct access to the engines? Should the game manager not handle this?
    def addRenderObject(self, mesh, shader, texture, isLightable = True, isLight = False, color = [0, 0, 0, 0]):
        # maybe turn params into defaults
        self.renderObject = self.renderEngine.createRenderObject(self.name, self.transform, mesh, shader, texture, isLightable, isLight, color)

    def addPhysicsObject(self, collisionModel = None, mass = 1):
        self.physicsObject = self.physicsEngine.createPhysicsObject(self.name, self.transform, collisionModel, mass)

    def addTag(self):
        pass

     