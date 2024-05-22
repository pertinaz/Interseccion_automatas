
class DFA:
    def __init__(self, states, alphabet, transitionFunction, initialState, acceptingStates):
        self.states = states
        self.alphabet = alphabet
        self.transitionFunction = transitionFunction
        self.initialState = initialState
        self.acceptingStates = acceptingStates

# regresa un nuevo DFA que representa la intersección de los lenguajes aceptados por los dos DFAs
def interseccionDFA(dfa1, dfa2):
    # El conjunto de estados será el producto cartesiano de los estados de los dos DFAs
    states = [(q1, q2) for q1 in dfa1.states for q2 in dfa2.states]
    alphabet = dfa1.alphabet
    initialState = (dfa1.initialState, dfa2.initialState)

    # Los estados de aceptación son aquellos en los que ambos componentes son estados de aceptación
    acceptingStates = [(q1, q2) for q1 in dfa1.states for q2 in dfa2.states if q1 in dfa1.acceptingStates and q2 in dfa2.acceptingStates]

    # La función de transición para el nuevo DFA
    transitionFunction = {}
    for (q1, q2) in states:
        for a in alphabet:
            nextState1 = dfa1.transitionFunction.get((q1, a))
            nextState2 = dfa2.transitionFunction.get((q2, a))
            if nextState1 is not None and nextState2 is not None:
                transitionFunction[((q1, q2), a)] = (nextState1, nextState2)

    return DFA(states, alphabet, transitionFunction, initialState, acceptingStates)