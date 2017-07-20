import gym
from gym import spaces
from gym.utils import seeding

import pyglet
import numpy as np

from maze_explorer import MazeExplorer

class MazeExplorerEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second' : 50
    }

    def __init__(self):
        # Start engine, invisible
        self.engine = MazeExplorer(False)

        self.action_space = spaces.Discrete(self.engine.actions_num)
        self.observation_space = spaces.Box(low=0, high=1, shape=(self.engine.observation_num,))

        self.viewer = None
        self.state = None

        self._seed()

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))

        # Act in the environment
        reward = self.engine.act(action)

        # Create observation from sensor proximities
        observation = [o.proximity_norm() for o in self.engine.world_layer.player.sensors]
        # Include battery level in state
        observation.append(self.engine.world_layer.player.stats['battery']/100)
        self.state = observation

        # observation, reward, done, info.
        return np.array(self.state), reward, self.engine.world_layer.player.game_over, {}

    def _reset(self):
        #self.state = self.np_random.uniform(low=-0.05, high=0.05, size=(4,))
        self.state = self.np_random.uniform(low=0, high=1, size=(self.engine.observation_num,))
        self.engine.create_scene()

        return np.array(self.state)

    def _render(self, mode='human', close=False):
        #if close:
        #    if self.viewer is not None:
        #        self.viewer.close()
        #        self.viewer = None
        #    return

        #if self.viewer is None:
        #    self.viewer = self.engine.director.window

        #if self.state is None: return None

        #return self.viewer.render(return_rgb_array = mode=='rgb_array')

        buffer = pyglet.image.get_buffer_manager().get_color_buffer()
        image_data = buffer.get_image_data()
        arr = np.fromstring(image_data.data, dtype=np.uint8, sep='')
        # In https://github.com/openai/gym-http-api/issues/2, we
        # discovered that someone using Xmonad on Arch was having
        # a window of size 598 x 398, though a 600 x 400 window
        # was requested. (Guess Xmonad was preserving a pixel for
        # the boundary.) So we use the buffer height/width rather
        # than the requested one.
        arr = arr.reshape(buffer.height, buffer.width, 4)
        arr = arr[::-1,:,0:3]

        return arr