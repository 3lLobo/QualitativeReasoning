import numpy as np
from entity import *

# Create all states

states = create_states()
print(len(states))

# Filter real states

fil_states = filter_states(states)

# make connections ID?

ids = np.linspace(0, len(fil_states), len(fil_states), dtype=int)
zip_states = list(zip(ids, fil_states))
connections = make_connections(zip_states)
print(len(connections))

# Draw Graph
# TODO delete obsolete states

state_dict = {id: state for id, state in zip_states}

draw_graph(connections, state_dict)

https://github.com/sgraaf/QualitativeReasoning/blob/master/utils.py

https://github.com/tycho01/qualitative-reasoning/blob/master/12205583_6195180.pdf

https://www.overleaf.com/project/5d25d983da20bb7915bdb672