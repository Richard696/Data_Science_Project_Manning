sample_space = {"Heads", "Tails"}

#Compute the probability of heads
probability_heads = 1/len(sample_space)
print(f'Probability of choosing heads is {probability_heads}\n')

# Def event condition

def is_heads_or_tails(outcome): return outcome in {"Heads", "Tails"}
def is_neither(outcome): return not is_heads_or_tails(outcome)

#Def additioning event condition
def is_heads(outcome):
    return outcome =="Heads"

def is_tails(outcome):
    return outcome == "Tails"

#defining an event detection function
def get_event(event_condition, sample_space):
    return set([outcome for outcome in sample_space
        if event_condition(outcome)])

"""Let execute the get_event on the four event condition"""
event_conditions = [is_heads_or_tails, is_heads, is_tails,is_neither]

for event_condition in event_conditions:
    print(f"Event condition: {event_condition.__name__}")
    event = get_event(event_condition, sample_space)
    print(f'Event: {event}\n\n')

# Computing event probability
def compute_probability(event_condition, generic_sample_space):
    event = get_event(event_condition, generic_sample_space)
    return len(event)/len(generic_sample_space)

print('Probability for generic sample space')
for event_condition in event_conditions:
    prob = compute_probability(event_condition, sample_space)
    name = event_condition.__name__
    print(f"Probability of event arising from '{name} is {prob}")

# analyse the bias coin
weighted_sample_space = {'Heads': 4, 'Tails': 1}

# Checking the weighted sample space size
sample_space_size = sum(weighted_sample_space.values())
assert sample_space_size == 5

# Checking the weighted event size
event =  get_event(is_heads_or_tails, weighted_sample_space)
event_size = sum(weighted_sample_space[outcome] for outcome in event)
assert event_size == 5

# define a generalized event probability function
def compute_weighted_probability(event_condition, generic_sample_space):
    event = get_event(event_condition, generic_sample_space)
    if type(generic_sample_space) == type(set()):
        return len(event)/len(generic_sample_space)
    event_size = sum(generic_sample_space[outcome]
            for outcome in event)
    return event_size/sum(generic_sample_space.values())

print('\n\nProbability for weighted sample space')

# compute the weighted event probability
for event_condition in event_conditions:
    prob = compute_weighted_probability(event_condition, weighted_sample_space)
    name = event_condition.__name__
    print(f"Probaility of event arising from '{name}' is {prob}")


