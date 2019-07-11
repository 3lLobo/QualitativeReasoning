import numpy as np
from entity import *

# Create all states

states = create_states()
print('Total states: ', len(states))
# Filter real states

fil_states = filter_states(states)
print('Number of states: ', len(fil_states))

# make connections ID?

ids = np.linspace(0, len(fil_states), len(fil_states), dtype=int)
zip_states = list(zip(ids, fil_states))
connections = make_connections(zip_states)
print('Number of connections: ', len(connections))

# Draw Graph
# TODO delete obsolete states

state_dict = {id: state for id, state in zip_states}

draw_graph(connections, state_dict)

