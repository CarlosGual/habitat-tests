import os
import sys
import habitat

# data_path = sys.path.append(os.path.dirname(__file__), '/home/carlos/repositorios/habitat-lab')

ABS_PATH = '/home/carlos/repositorios/habitat-lab/'

config = habitat.get_config(
    config_paths="configs/objectnav_mp3d.yaml"
)

try:
    env.close()
except NameError:
    pass
env = habitat.Env(config=config)
