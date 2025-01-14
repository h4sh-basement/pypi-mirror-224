import pkg_resources
import sys
import numpy as np
from typing import List, Tuple, Dict, Any, Optional, Union, Callable
import pygame
import gymnasium as gym
from gym.spaces import Box as BoxType
from gym.spaces import Dict as DictType
from gym.spaces import Discrete as DiscreteType
from gym.spaces import MultiDiscrete as MultiDiscreteType
from gym.spaces import MultiBinary as MultiBinaryType
from CoderSchoolAI.Environment.Attributes import ObsAttribute, ActionAttribute
from CoderSchoolAI.Environment.Agent import Agent
from CoderSchoolAI.Environment.Shell import Shell
SpaceType = Union[BoxType, DiscreteType, MultiDiscreteType, MultiBinaryType]
"""
For more information regarding Spaces, see https://gym.openai.com/docs/spaces/
"""
from enum import IntEnum
from collections import deque

from CoderSchoolAI.Training.Algorithms import QLearning
from CoderSchoolAI.Util.data_utils import distance, euclidean_distance 
from CoderSchoolAI.Util.search_utils import HeapQueue
# They are the same function, some would rather use distance because it makes more sense.


class SnakeAgent(Agent):
    class ActionMode(IntEnum):
        USER = 0        
        QLearning = 1
        
    class SnakeAction(IntEnum):
        """
        Actions that may be taken by the snake.
        """
        LEFT = 0
        RIGHT = 1
        UP = 2
        DOWN = 3
        NOACTION = 4
    DIRECTIONS = {
            SnakeAction.LEFT: (-1, 0),
            SnakeAction.RIGHT: (1, 0),
            SnakeAction.UP: (0, -1),
            SnakeAction.DOWN: (0, 1),
            SnakeAction.NOACTION: (0, 0),
        }
    def __init__(self,
                 is_user_control:bool = False,
                 is_q_table:bool = False,
                 is_search_enabled:bool = False,
                 policy_kwargs=dict(alpha=0.5,gamma=0.9,epsilon=0.9, epsilon_decay=0.995, stop_epsilon=0.01),
                ):
        """
        
        """
        super().__init__(is_user_control)
        self.body = deque([(i, 0) for i in range(3)])
        self.last_action = SnakeAgent.SnakeAction.RIGHT
        self._last_removed = None
        self.is_q_table = is_q_table
        self.is_search_enabled = is_search_enabled
        if self.is_q_table:
            self.qlearning = QLearning(self.get_actions(), **policy_kwargs)

        
    def _move_snake(self, action: 'SnakeAgent.SnakeAction') -> 'SnakeAgent.SnakeAction':
        """
        Moves the snake in the new direction, or the old direction if the snake direction has not changed (No Action).
        """
        feedback = 0
        _head = self.body[-1]
        if action == SnakeAgent.SnakeAction.NOACTION or np.dot( self.DIRECTIONS[action], self.DIRECTIONS[self.last_action]) < 0:
            feedback = -0.2 if action != SnakeAgent.SnakeAction.NOACTION else -0.05
            action = self.last_action
        _new_head = _head[0] + self.DIRECTIONS[action][0], _head[1] + self.DIRECTIONS[action][1]
        # print('Action: ', action, 'Pos:', _new_head)
        self._last_removed = self.body.popleft()
        self.body.append(_new_head)
        self.last_action = action
        return action, feedback
    
    def increment_score(self):
        """
        Increments the score of the snake.
        """
        self.body.appendleft(self._last_removed)
        
    def reset_snake(self):
        """
        Resets the snake to its starting position.
        """
        self.body = deque([(i, 0) for i in range(3)])
        self.last_action = SnakeAgent.SnakeAction.RIGHT
        self._last_removed = None
    
    def get_actions(self):
        return list(SnakeAgent.SnakeAction)
    
    def head_intersects_body(self) -> bool:
        """
        This function returns True if the head of the snake intersects with the body of the snake.
        """
        _head = self.body[-1]
        for i in range(len(self.body)-2):
            if _head[0] == self.body[i][0] and _head[1] == self.body[i][1]:
                return True
        return False
    
    def get_q_table_state(self, state) ->Tuple:
        """
        State should contain:
        - the (x,y) of the apple, 
        - the direction (0, 1, 2, 3) of the snake, 
        - the (x, y) of the head of the snake, 
        """
        a_x, a_y = state['apple_pos']
        dir = state['moving_direction']
        s_x, s_y = state['snake_pos']
        d_x, d_y = a_x - s_x, a_y - s_y
        l = self.DIRECTIONS[SnakeAgent.SnakeAction.LEFT][0] + s_x, self.DIRECTIONS[SnakeAgent.SnakeAction.LEFT][1] + s_y
        r = self.DIRECTIONS[SnakeAgent.SnakeAction.RIGHT][0] + s_x, self.DIRECTIONS[SnakeAgent.SnakeAction.RIGHT][1] + s_y
        u = self.DIRECTIONS[SnakeAgent.SnakeAction.UP][0] + s_x, self.DIRECTIONS[SnakeAgent.SnakeAction.UP][1] + s_y
        d = self.DIRECTIONS[SnakeAgent.SnakeAction.DOWN][0] + s_x, self.DIRECTIONS[SnakeAgent.SnakeAction.DOWN][1] + s_y
        l_t, r_t, u_t, d_t = 1, 1, 1, 1
        for pos in self.body:
            if pos == l:
                l_t = 0
            elif pos == r:
              r_t = 0
            elif pos == u:
                u_t = 0
            elif pos == d:
                d_t = 0
        return (d_x, d_y, dir, l_t, r_t, u_t, d_t)
        

    def get_next_action(self, state) -> Tuple['SnakeAgent.SnakeAction', float]:
        """
        Gets the next action to take in the current state, and any feedback from the snake.
        Returns:
        -   Action to take in the current state.
        """
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if self.is_q_table:
            state = self.get_q_table_state(state)
            action = self.qlearning.choose_action(state)
        elif self.is_user_control:
            action = self.get_user_action(events)
        elif self.is_search_enabled:
            action = self.get_astar_action(state)
        else:
            # implement your own logic here if not using Q-learning
            pass
        return action
    
    def get_user_action(self, events) -> 'SnakeAgent.SnakeAction':
        """
        This is an Example of how to use the user input to control the Snake.
        """
        # Process user input and return the corresponding action
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            return SnakeAgent.SnakeAction.DOWN
        elif keys[pygame.K_a]:
            return SnakeAgent.SnakeAction.LEFT
        elif keys[pygame.K_d]:
            return SnakeAgent.SnakeAction.RIGHT
        elif keys[pygame.K_w]:
            return SnakeAgent.SnakeAction.UP
        return SnakeAgent.SnakeAction.NOACTION

    def get_astar_action(self, state) -> 'SnakeAgent.SnakeAction':
        """
        A* search logic here and return the next action based on the result of A* search.
        """ 
        def find_path_astar(start, end, snake_body):
                start = tuple(start)
                end = tuple(end)
                frontier = HeapQueue()
                frontier.push((0, start))
                c_from = {}
                min_cost = {}
                c_from[start] = None
                min_cost[start] = 0
        
                while frontier.size() > 0:
                    priority, pos = frontier.pop()
                    if pos == end:
                        break
                    
                    for action in list(SnakeAgent.SnakeAction):
                        offset = SnakeAgent.DIRECTIONS[action]
                        new_pos = (pos[0] + offset[0], pos[1] + offset[1])
                        new_cost = min_cost[pos] + 1
                        if new_pos not in c_from or new_cost < min_cost[new_pos] and not any([new_pos[0]==s[0] and new_pos[1]==s[1] for s in snake_body]):
                            min_cost[new_pos] = new_cost
                            priority = new_cost + distance(new_pos, end)
                            frontier.push((priority, new_pos))
                            c_from[new_pos] = (pos, action)

                current = end
                path = [current]
                while current != start:
                    current, action = c_from[current]
                    path.append((current, action))
                path.reverse()  # optional
                return path
        path = find_path_astar(state['snake_pos'], state['apple_pos'], self.body)
        try:
            print(path[0][1])
            return path[0][1]
        except IndexError:
            return SnakeAgent.SnakeAction.NOACTION

    def update(self, state, action, next_state, reward):
        """
        This is an example of how to update the state of the Snake Agent
        """
        pass

class SnakeEnv(Shell):
    #Static Variables of the SnakeEnv
    WORLD_COLOR = (0, 0, 0)
    BODY_COLOR = (0, 255, 0)
    HEAD_COLOR = (165, 42, 42)
    APPLE_COLOR = (255, 0, 0)
    
    class GameObjects(IntEnum):
        EMPTY = 0
        BODY = 1
        HEAD = 2
        APPLE = 3
        
        
    def __init__(self, 
                 target_fps=6, # Framerate at which the Game Loop will run
                 is_user_control=False, #Flag that indicates whether the user is controlling the environment or not
                 cell_size=20, # Number of pixels in a Cell
                 height=25, # Height of the Grid
                 width=25, # Width of the Grid
                 max_length_of_snake=100, # Maximum length of the snake
                 verbose=False, # Flag that indicates whether the environment should print Environment Information
                 snake_is_q_table=False, # Flag that indicates whether the snake is using Q-learning or not
                 snake_is_search_enabled=False, # Flag that indicates whether the snake is using A* search or not
                 policy_kwargs=dict(alpha=0.5,gamma=0.9,epsilon=0.9, epsilon_decay=0.995, stop_epsilon=0.01), # Hyperparameters for the Q-learning algorithm
                 console_only=False, # Makes the environment run only as a console application.
                 ):
        """
        - target_fps: Framerate at which the Game Loop will run
        - is_user_control: Flag that indicates whether the user is controlling the environment or not
        - cell_size: Number of pixels in a Cell
        - height: Height of the Grid
        - width: Width of the Grid
        - max_length_of_snake: Maximum length of the snake
        """
        super().__init__(target_fps, is_user_control, resolution=(height*cell_size, width*cell_size), verbose=verbose, environment_name="Snake-Env", console_only=console_only)
        self.height = height
        self.width = width
        self.cell_size = cell_size
        self.max_length_of_snake = max_length_of_snake
        self.snake_agent = SnakeAgent(self.is_user_control, snake_is_q_table, snake_is_search_enabled, policy_kwargs)
        
        # Initialize game_state attributes, internal variables, and callbacks
        self.game_state = np.zeros((height, width, 1), dtype=np.float32)
        self.__last_moving_direction = SnakeAgent.SnakeAction.RIGHT
        self.apple_position = self.spawn_new_apple()
        self._apples_consumed = 0
        self._soft_reset = False
        apple_res = pkg_resources.resource_filename('CoderSchoolAI', 'Assets/Snake/Apple.png')
        self.apple_asset = pygame.image.load(apple_res).convert()
        self.apple_asset = pygame.transform.scale(self.apple_asset, (self.cell_size, self.cell_size))

        """Register the Attributes"""
        # Game State Attribute
        self.register_attribute(ObsAttribute(name="game_state", 
        # Number of parameters in the environment to be trained on x height of image x width of image. In this case we are only training on object types.
                                             space= BoxType(shape=(1, height, width), low=0, high=1, dtype=np.float32), 
                                             update_func=self.__update_game_state_callback))
        if self.verbose:
            print('Registered: game_state Attribute.')
        # Moving Direction Attribute
        self.register_attribute(ObsAttribute(name="moving_direction",  
                                             space= DiscreteType(n=1), 
                                             update_func=self.__update_moving_direction_callback))
        if self.verbose:
            print('Registered: moving_direction Attribute.')
        # Appple Position Attribute
        self.register_attribute(ObsAttribute(name="apple_pos",  
                                             space= MultiDiscreteType(
                                                nvec=[self.height, self.width],
                                                ), 
                                             update_func=self.__update_apple_pos_callback))
        if self.verbose:
            print('Registered: apple_pos Attribute.')
        # Snake Head Position Attribute
        self.register_attribute(ObsAttribute(name="snake_pos",  
                                             space= DiscreteType(n=2), 
                                             update_func=self.__update_snake_head_callback))
        if self.verbose:
            print('Registered: snake_pos Attribute.')
        # Misc Class Items
        self.font = pygame.font.Font(None, 36)  # Default font for the text. 
        

    def reset(self, attributes=None) -> Tuple[Union[Dict[str, ObsAttribute], ObsAttribute, np.ndarray], Union[int, float], Union[bool, np.ndarray]]:
        """
        Example of how to use the Reset Function to reset the Snake Environment.
        """
        if self.verbose:
            print('Resetting Apple Position.') if self._soft_reset else print('Resetting Snake.')

        self.apple_position = self.spawn_new_apple()
        if self._soft_reset:
            self._soft_reset = False
            self._apples_consumed += 1
            
        else:
            self.snake_agent.reset_snake()
            self._apples_consumed = 0
            self.__last_moving_direction = SnakeAgent.SnakeAction.RIGHT
        
        self.update_observation_variables()
        for name, obs in self.ObsAttributes.items():
            obs.update_func()
        return self.get_observation(attributes)

    def step(self, action: Union[int, np.ndarray, Dict[str, ActionAttribute]], d_t: float, attributes = None):
        """
        Example of how to use the Step Function to control the Snake.
        """
        # This will update the proper moving direction of the Snake and update the game state
        self.__last_moving_direction, feedback = self.snake_agent._move_snake(action)
        if self.verbose:
            print(f'Taking Action: {action}')
        # Updates the Observation Variables
        # print(action)
        reward, finished = self.get_current_reward(feedback)
        if not finished:
            self.update_observation_variables()
            for name, obs in self.ObsAttributes.items():
                obs.update_func()
                
        if self.consumed_apple():
                self.snake_agent.increment_score()
        # Returns the new game state, reward, and whether or not the Snake has reached the goal.
        return self.get_observation(attributes), reward, finished
        
    def get_current_reward(self, feedback) -> Tuple[Union[int, float], bool]:
        """
        
        Note the Return Values:
            - Reward (Float) is the returned value of the Agent's Performance.
            - Finished is a boolean (True/False) value that indicates whether or not the Snake has reached the goal.
            
        This function uses:
            - Whether or not the Apple Was Consumed,
            - The Distance from the Snake Head to the Apple,
            - The length of the Snake Body (minus the length of the snake at the Start),
            - Whether or not The Snake is Still inside of our Grid
            
        """
        distance_to_apple = euclidean_distance(self.snake_agent.body[-1], self.apple_position)
        apple_consumed = self.consumed_apple()
        length_of_snake = len(self.snake_agent.body) - 3 # Minus the length of the snake at the Start
        is_in_bounds = self._is_snake_in_bounds()
        head_intersects_body = self.snake_agent.head_intersects_body()
        if not is_in_bounds or head_intersects_body:
            if self.verbose:
                print('Snake Has Intersected with a non-collidable area.')
            self._soft_reset = False
            return -1, True
        if apple_consumed:
            if self.verbose:
                print('Snake Has Consumed an Apple.')
            self._soft_reset = True
            return 1, True
        """
        Here we assign rewards for different viewable attributes of the environment.
        """
        distance_penalty = -distance_to_apple / euclidean_distance((self.width, self.height), (0, 0))
        length_of_snake_reward = length_of_snake / self.max_length_of_snake
        return (distance_penalty + length_of_snake_reward + feedback), False
        
    def update_env(self):
        d_t = self.clock.tick(self.target_fps) / 1000.0
        prev_state = self.get_observation()
        action = self.snake_agent.get_next_action(prev_state)
        new_state, reward, finished = self.step(action, d_t)
        if self.verbose:
            print(f'Reward: {reward}')
        if self.snake_agent.is_q_table:
            self.snake_agent.qlearning.update_q_table(
                self.snake_agent.get_q_table_state(prev_state), int(action), reward, self.snake_agent.get_q_table_state(new_state)
                )
        
        if finished:                
            self.reset()

        self.render_env()

    def render_env(self):
        """
        Renders the Snake Game to the screen Via PyGame.
        """
        if not self.console_only:
            #Fills the world with the Blank Color
            self.screen.fill(self.WORLD_COLOR)
            # Draw the game state
            for pos in self.snake_agent.body:
                    rect = pygame.Rect(pos[0] * self.cell_size, pos[1] * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, self.BODY_COLOR, rect)

            # Draw the head of the snake
            head_position = self.snake_agent.body[-1]
            rect = pygame.Rect(head_position[0] * self.cell_size, head_position[1] * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, self.HEAD_COLOR, rect)

            # Draw the apple
            # rect = pygame.Rect(self.apple_position[0] * self.cell_size, self.apple_position[1] * self.cell_size, self.cell_size, self.cell_size)
            # pygame.draw.rect(self.screen, self.APPLE_COLOR, rect)
            apple_rect = self.apple_asset.get_rect()
            apple_rect.topleft = (self.apple_position[0]*self.cell_size, self.apple_position[1]*self.cell_size)
            self.screen.blit(self.apple_asset, apple_rect)
            
            # Draw the grid Lines
            for i in range(self.width):  # Assuming grid_size is the number of cells
                pygame.draw.line(self.screen, (255, 255, 255), (i * self.cell_size, 0), (i * self.cell_size, self.width * self.cell_size))  # Vertical lines
            for i in range(self.width):  # Assuming grid_size is the number of cells
                pygame.draw.line(self.screen, (255, 255, 255), (0, i * self.cell_size), (self.height * self.cell_size, i * self.cell_size))  # Horizontal lines
            
            #Draw the score
            score_text = self.font.render(f'Score: {self._apples_consumed}', True, (225, 220, 128))
            self.screen.blit(score_text, (self.width * self.cell_size - score_text.get_width() - 5, 5))  # Draw the score on the top right corner

            pygame.display.flip()
            pygame.display.update()    
    
    def update_observation_variables(self):
        """
        This is an Example of how the Game State Data can be updated.
        """
        self.game_state = np.zeros((self.height, self.width, 1), dtype=np.float32)
        self.update_agent_data()
        self.game_state[self.apple_position] = int(SnakeEnv.GameObjects.APPLE) # Apple

    def update_agent_data(self):
        """
        This function will update the Snake's Game State Data relating to the Agent.
        """
        for position in self.snake_agent.body:
            self.game_state[position] = int(SnakeEnv.GameObjects.BODY) # Snake body
        self.game_state[self.snake_agent.body[-1]] = int(SnakeEnv.GameObjects.HEAD) # Snake head
        
    def __update_game_state_callback(self):
        self['game_state'].data = self.game_state.copy().transpose(2, 0, 1) / len(list(SnakeAgent.SnakeAction))
    
    def __update_moving_direction_callback(self):
        self['moving_direction'].data = int(self.__last_moving_direction)
        
    def __update_apple_pos_callback(self):
        self['apple_pos'].data = np.array(self.apple_position).copy()
    
    def __update_snake_head_callback(self):
        self['snake_pos'].data = np.array(self.snake_agent.body[-1]).copy()
        
    def spawn_new_apple(self) -> Tuple[int, int]:
        """
        Generates an Apple at a random position.
        """
        return (np.random.randint(0, self.width - 1), np.random.randint(0, self.height - 1))
    
    def consumed_apple(self,):
        """
        Example of how to check if the Snake has eaten an Apple.
        """
        return self.apple_position[0] == self.snake_agent.body[-1][0] and self.apple_position[1] == self.snake_agent.body[-1][1]

    def _is_snake_in_bounds(self, ):
        """
        Example of how to check if the Snake has exited the Grid.
        """
        head_position = self.snake_agent.body[-1]
        return (0 <= head_position[0] < self.width) and (0 <= head_position[1] < self.height)
    
            
    
    