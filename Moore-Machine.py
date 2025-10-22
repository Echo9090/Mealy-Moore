# ======================================
# Finite State Machine Base Class
# ======================================
class State:
    def __init__(self, name, output=None):
        self.name = name
        self.output = output
        self.transitions = {}

    def add_transition(self, input_symbol, next_state, output=None):
        self.transitions[input_symbol] = (next_state, output)

    def get_next(self, input_symbol):
        return self.transitions.get(input_symbol, (None, None))


# ======================================
# Moore Machine Implementation
# ======================================
class MooreMachine:
    def __init__(self, start_state):
        self.start_state = start_state
        self.current_state = start_state

    def reset(self):
        self.current_state = self.start_state

    def process(self, input_sequence):
        output_sequence = []
        state_sequence = [self.current_state.name]

        for symbol in input_sequence:
            output_sequence.append(self.current_state.output)
            next_state, _ = self.current_state.get_next(symbol)
            if next_state is None:
                break
            self.current_state = next_state
            state_sequence.append(self.current_state.name)

        output_sequence.append(self.current_state.output)
        return state_sequence, output_sequence


# Example Moore setup (based on the left whiteboard diagram)
A = State('A', 0)
B = State('B', 1)
C = State('C', 0)

A.add_transition('0', B)
A.add_transition('1', C)
B.add_transition('0', C)
B.add_transition('1', B)
C.add_transition('0', B)
C.add_transition('1', A)

moore_machine = MooreMachine(A)
states, outputs = moore_machine.process("0110")

print("Moore Machine")
print("States:", states)
print("Outputs:", outputs)
