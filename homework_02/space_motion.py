"""
Simulate the stars/planets/satellites motion in 2D space.
Every two objects in the universe are attracted by the gravitational force

$$\vec{F_{ij}} = \frac{G m_i m_j}{r_{ij}^2} \frac{\vec{r_{ij}}}{\|r_{ij}\|}.$$ 

The force that acts on the object $i$ is the vectorial sum of the forces induced by all other (massive) objects

$$\vec{F_i} = \sum_{j \neq i} \vec{F_{ij}}$$

Use SI units, don't be concerned with the speed of the code - do not optimize!!!

Write function that takes any number of space objects (named tuples) as arguments
(may not be a list of named tuples for any function!!!)
plus the size of the time step and number of time steps.
For each object it calculates the force caused by other objects (vector sum of attractive forces).
It returns the dictionary with name of the object as a key and tuple of lists of coordinates
(one list of x, one of y, every time step one item in list).

Write a decorator that measures number of calling of each function and their runtime of the functions.
The information should be printed to standard output in a form "function_name - number_of_calls - time units\n".
The decorator takes optional parameter units which allows to specify time units for printing (default is ms).
You can implement the unit measurement only for ns, ms, s, min, h and days.

Below is description of all steps for calculating the update.
If you are unsure of precise interface see test script for examples of calling the function.
"""

import time  # measuring time
from collections import namedtuple
import math
# Define universal gravitation constant
G = 6.67408e-11  # N-m2/kg2
SpaceObject = namedtuple('SpaceObject', 'name mass x y vx vy color')
Force = namedtuple('Force', 'fx fy')


def distance(space_object_1: SpaceObject, space_object_2: SpaceObject):
    return math.sqrt((space_object_2.x - space_object_1.x) ** 2 + (space_object_2.y - space_object_1.y) ** 2)


time_conversions_dict = {'ns': 1.0e-9,
                         'ms': 1000,
                         's': 1,
                         'min': 1.0/60.0,
                         'h': 1.0/3600.0,
                         'days': 1.0/86400.0}


def logging(unit='s'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            start_time = time.time()
            val = func(*args, **kwargs)
            end_time = time.time()
            func_time = end_time - start_time
            func_time = func_time * time_conversions_dict[unit]
            print(f"{func.__name__} - {wrapper.calls} - {func_time}{unit}")
            return val
        wrapper.calls = 0
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator


@logging(unit='ms')
def calculate_force(first_space_object: SpaceObject, *args: SpaceObject):
    # input: one of the space objects (indexed as i in below formulas),
    #        other space objects (indexed as j, may be any number of them)
    # returns named tuple (see above) that represents x and y components of the gravitational force
    # calculate force (vector) for each pair (space_object, other_space_object):
    # |F_ij| = G*m_i*m_j/distance^2
    # F_x = |F_ij| * (other_object.x-space_object.x)/distance
    # analogous for F_y
    # for each coordinate (x, y) it sums force from all other space objects
    f_x = 0.0
    f_y = 0.0
    for x in args:
        distance_ij = distance(first_space_object, x)
        if distance_ij == 0:
            continue
        f_ij = math.fabs(G * first_space_object.mass * x.mass / distance_ij ** 2)
        f_x += f_ij * (x.x - first_space_object.x) / distance_ij
        f_y += f_ij * (x.y - first_space_object.y) / distance_ij
    return Force(f_x, f_y)


@logging(unit='s')
def update_space_object(space_object: SpaceObject, force: Force, timestep):
    # here we update coordinates and speed of the object based on the force that acts on it
    # input: space_object we want to update (evolve in time),
    #        force (from all other objects) that acts on it,
    #        size of timestep
    # returns: named tuple (see above) that contains updated coordinates and speed for given space_object
    # hint:
    # acceleration_x = force_x/mass
    # same for y
    # speed_change_x = acceleration_x * time_step
    # same for y
    # speed_new_x = speed_old_x + speed_change_x
    # same for y
    # x_final = x_old + speed_new_x * time_step
    acceleration_x = force.fx / space_object.mass
    acceleration_y = force.fy / space_object.mass
    speed_change_x = acceleration_x * timestep
    speed_change_y = acceleration_y * timestep
    speed_new_x = space_object.vx + speed_change_x
    speed_new_y = space_object.vy + speed_change_y
    x_final = space_object.x + speed_new_x * timestep
    y_final = space_object.y + speed_new_y * timestep
    return SpaceObject(space_object.name, space_object.mass, x_final, y_final, speed_new_x, speed_new_y, space_object.color)


@logging(unit='ms')
def update_motion(timestep, *args):
    # input: timestep and space objects we want to simulate (as named tuples above)
    # returns: list or tuple with updated objects
    # hint:
    # iterate over space objects, for given space object calculate_force with function above, update
    updated_space_objects = []
    for planet in args:
        force = calculate_force(planet, *args)
        updated_space_objects.append(update_space_object(planet, force, timestep))
    return updated_space_objects  # (named tuple with x and y)
    
    
@logging()
def simulate_motion(time_step_size, number_of_time_steps: int, *args: SpaceObject):
    # generator that in every iteration yields dictionary with name of the objects
    # as a key and tuple of coordinates (x first, y second) as values
    # input size of time_step, number of time_steps (integer), space objects (any number of them)
    old_space = args
    for i in range(number_of_time_steps):
        space = update_motion(time_step_size, *old_space)
        space_dictionary = {}
        for planet in space:
            space_dictionary[planet.name] = (planet.x, planet.y)
        old_space = space
        yield space_dictionary
