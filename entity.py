import pygraphviz as pgv

def create_states():
    states = []
    for inflow_mag in ['0', '+']:
        for inflow_grad in ['-', '0', '+']:
            for volume_mag in ['0', '+', 'max']:
                for volume_grad in ['-', '0', '+']:
                    for outflow_mag in ['0', '+', 'max']:
                        for outflow_grad in ['-', '0', '+']:
                            states.append([(inflow_mag, inflow_grad), (volume_mag, volume_grad), (outflow_mag, outflow_grad)])
    return states

def filter_states(states):
    sane_states = []
    for state in states:
        APPEND_FLAG = True
        # All possible wrong state setups
        for tup in state:
            mag, grad = tup
            if mag == 'max' and grad == '+':
                APPEND_FLAG = False
            if mag == '0' and grad == '-':
                APPEND_FLAG = False
        flow, vol, out = state
        if vol[0] != out[0] or vol[1] != vol[1]:
            APPEND_FLAG = False
        if APPEND_FLAG:
            sane_states.append(state)
    return sane_states

def make_connections(id_states):
    connection_list = []
    enum_rev = {'0': 0, '+': 1, 'max': 2}
    for id, state in id_states:
        for id2, state2 in id_states:
            true_count = 0
            for n in range(len(state)):
                entity = state[n]
                entity2 = state2[n]
                # If grad is 0 mag got to stay the same
                if entity[1] == '0' and entity[0] == entity2[0]:
                    true_count += 1
                # If grad is positive magnitude got to rise
                if entity[1] == '+' and enum_rev[entity[0]]+1 == enum_rev[entity2[0]]:
                    true_count += 1
                # If grad is negative magnitude got to sink
                if entity[1] == '-' and enum_rev[entity[0]]-1 == enum_rev[entity2[0]]:
                    true_count += 1
            if true_count == 3:
                connection_list.append((id, id2))
    return connection_list

def draw_graph(connection_list,state_dict):
    G = pgv.AGraph(
        directed=True,
        overlap=False,
        splines=True,
        sep=+0.5,
        normalize=True,
        smoothing='avg_dist')
    print('Drawing Graph ...')
    for connection in connection_list:
        id1, id2 = connection
        G.add_edge(id1, id2)

    G.layout(prog='dot')
    G.draw('ouput.png')
    print('Graph finished!')
