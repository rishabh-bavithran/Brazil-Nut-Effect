import pygame
import math
import random
import numpy as np

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
 
class Mynode(Node):
    def __init__(self):
        super().__init__("Mynode")

        # Initialize pygame
        pygame.init()

        # Set up the screen
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))

        # Set up the clock
        clock = pygame.time.Clock()

        # Define the robots
        num_robots = 200
        robots = []
        #robot['r'] = random.randint(10, 60)
        robot_speed = 5

        for i in range(num_robots):
            robot = {'x': random.uniform(60, screen_width-60),
                    'y': random.uniform(60, screen_height-60),
                    'vx': random.uniform(-robot_speed, robot_speed),
                    'vy': random.uniform(-robot_speed, robot_speed),
                    'r': random.randint(10, 35)}
            robots.append(robot)

        # Define the object
        object_radius = 20
        object = {'x': random.uniform(object_radius, screen_width-object_radius),
                'y': random.uniform(object_radius, screen_height-object_radius),
                'vx': 0,
                'vy': 0,
                'force': 1}

        # Set up the gravitational force
        gravity_direction = np.pi/2
        gravity_strength = 0.5

        # Run the simulation
        count = 0
        while (count < 500):
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Clear the screen
            screen.fill((0, 0, 0))

            # Apply forces to the robots
            for robot in robots:
                # Random unit force in a random direction
                random_direction = random.uniform(0, 2*np.pi)
                random_force = 1
                fx = random_force*np.cos(random_direction)
                fy = random_force*np.sin(random_direction)

                # Gravitational force
                gx = gravity_strength*np.cos(gravity_direction)
                gy = gravity_strength*np.sin(gravity_direction)

                # Net force
                net_force_x = fx + gx
                net_force_y = fy + gy

                # Update velocity
                robot['vx'] += net_force_x
                robot['vy'] += net_force_y

                # Limit speed
                speed = np.sqrt(robot['vx']**2 + robot['vy']**2)
                if speed > robot_speed:
                    robot['vx'] = robot['vx']/speed*robot_speed
                    robot['vy'] = robot['vy']/speed*robot_speed

                # Move the robot
                robot['x'] += robot['vx']
                robot['y'] += robot['vy']

                # Check for collisions with the screen edges
                if robot['x'] < robot['r']:
                    robot['x'] = robot['r']
                    robot['vx'] = -robot['vx']
                elif robot['x'] > screen_width-robot['r']:
                    robot['x'] = screen_width-robot['r']
                    robot['vx'] = -robot['vx']
                if robot['y'] < robot['r']:
                    robot['y'] = robot['r']
                    robot['vy'] = -robot['vy']
                elif robot['y'] > screen_height-robot['r']:
                    robot['y'] = screen_height-robot['r']
                    robot['vy'] = -robot['vy']

                # Check for collisions with other robots
                for other_robot in robots:
                    if other_robot == robot:
                        continue
                    distance = np.sqrt((robot['x']-other_robot['x'])**2 + (robot['y']-other_robot['y'])**2)
                    if distance < robot['r'] + other_robot['r']:
                        # Collision detected, push the robots away from each other
                        overlap = 1.85*robot['r'] - distance
                        direction = np.arctan2(robot['y']-other_robot['y'], robot['x']-other_robot['x'])
                        robot['x'] += 0.5*overlap*np.cos(direction)
                        robot['y'] += 0.5*overlap*np.sin(direction)
                        other_robot['x'] -= 0.5*overlap*np.cos(direction)
                        other_robot['y'] -= 0.5*overlap*np.sin(direction)

            # Apply forces to the object
            fx = object['force']*np.cos(gravity_direction)
            fy = object['force']*np.sin(gravity_direction)
            object['vx'] += fx
            object['vy'] += fy

            # Move the object
            object['x'] += object['vx']
            object['y'] += object['vy']

            # Check for collisions with the screen edges
            if object['x'] < object_radius:
                object['x'] = object_radius
                object['vx'] = -object['vx']
            elif object['x'] > screen_width-object_radius:
                object['x'] = screen_width-object_radius
                object['vx'] = -object['vx']
            if object['y'] < object_radius:
                object['y'] = object_radius
                object['vy'] = -object['vy']
            elif object['y'] > screen_height-object_radius:
                object['y'] = screen_height-object_radius
                object['vy'] = -object['vy']

            # Check for collisions with the object
            for rr in robots:
                distance2 = np.sqrt((object['x']-rr['x'])**2 + (object['y']-rr['y'])**2)
                if distance2 < 1.27*(rr['r'] + object_radius):
                    # Collision detected, push the robot away from the object
                    overlap2 = robot['r'] + object_radius - distance2
                    direction2 = np.arctan2(rr['y']-object['y'], rr['x']-object['x'])
                    rr['x'] += 0.5*overlap2*np.cos(direction2)
                    rr['y'] += 0.5*overlap2*np.sin(direction2)
                    object['x'] -= 0.5*overlap2*np.cos(direction2)
                    object['y'] -= 0.5*overlap2*np.sin(direction2)

            if object['vx']>3:
                object['vx']=3
            if object['vy']>3:
                object['vy']=3
            
            # Draw the robots and the object
            for robot in robots:
                pygame.draw.circle(screen, (255, 255, 255), (int(robot['x']), int(robot['y'])), robot['r'])
            pygame.draw.circle(screen, (255, 0, 0), (int(object['x']), int(object['y'])), object_radius)

            # Update the screen
            pygame.display.update()

            # Set the clock
            clock.tick(60)
            count +=1
        sum = 0
        counter = 0
        for rob in robots:
            if (rob['y']>object['y']-5):
                if (rob['y']<object['y']+5):
                    sum += rob['r']
                    counter += 1

        average = sum / counter
        self.get_logger().info(" the object radius is:" +str(object_radius) + " the estimated radius is: " +str(average))

 
def main(args=None):
    rclpy.init(args=args)
    node = Mynode()
    rclpy.spin(node)
    rclpy.shutdown()
 
if __name__ == "__main__":
    main()


