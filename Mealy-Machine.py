# ======================================
# State Class (shared by all FSMs)
# ======================================
class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, input_symbol, next_state, output):
        """Define a transition: on input_symbol → go to next_state, produce output"""
        self.transitions[input_symbol] = (next_state, output)

    def get_next(self, input_symbol):
        """Return (next_state, output) for a given input symbol"""
        return self.transitions.get(input_symbol, (None, None))


# ======================================
# Mealy Machine Implementation
# ======================================
class MealyMachine:
    def __init__(self, start_state):
        self.start_state = start_state
        self.current_state = start_state

    def reset(self):
        self.current_state = self.start_state

    def process(self, input_sequence):
        output_sequence = []
        state_sequence = [self.current_state.name]

        for symbol in input_sequence:
            next_state, output = self.current_state.get_next(symbol)
            if next_state is None:
                print(f"⚠️ No transition for input '{symbol}' in state '{self.current_state.name}'")
                break
            output_sequence.append(output)
            self.current_state = next_state
            state_sequence.append(self.current_state.name)

        return state_sequence, output_sequence


# ======================================
# Example Mealy setup (from whiteboard)
# ======================================
A = State('A')
B = State('B')

# Define transitions: input / output
A.add_transition('0', A, 'b')
A.add_transition('1', B, 'a')
B.add_transition('0', A, 'q')
B.add_transition('1', B, 'b')

# Initialize the machine
mealy_machine = MealyMachine(A)

# Test input (e.g. from whiteboard: "011001")
input_sequence = "011001"
states, outputs = mealy_machine.process(input_sequence)

# Display results
print("\n--- Mealy Machine Simulation ---")
print(f"Input Sequence:   {' '.join(input_sequence)}")
print(f"State Sequence:   {' → '.join(states)}")
print(f"Output Sequence:  {' '.join(outputs)}")
