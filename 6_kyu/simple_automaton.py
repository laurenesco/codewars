# https://www.codewars.com/kata/5268acac0d3f019add000203

class Automaton(object):
    
    # Captures automaton states as keys, accept state status as values
    START_STATE = "q1"
    ACCEPT_STATE = "q2"
    STATE_TRANSITIONS = {
        "q1": {
            "0": "q1",
            "1": "q2"
        },
        "q2": {
            "0": "q3",
            "1": "q2"
        },    
        "q3": {
            "0": "q2",
            "1": "q2"
        }
    }

    def __init__(self):
        pass
        
    def read_commands(self, commands):
        """
        Accept or reject the commands based on whether we end in our accept state, q2
        """
        state = self.START_STATE
        
        for symbol in commands:
            state = self.STATE_TRANSITIONS[current_state][symbol]
        
        return state == self.ACCEPT_STATE

my_automaton = Automaton()
