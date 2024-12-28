class WhiskersGameState:
    def __init__(self, whiskers_choices):
        self.whiskers_choices = whiskers_choices
        self.current_state = 'intro'

    def get_next_line(self):
        if self.current_state in self.whiskers_choices:
            story = self.whiskers_choices[self.current_state]
            if self.whiskers_choices.current_story_index < len(story):
                line = story[self.whiskers_choices.current_story_index]
                if self.whiskers_choices.current_char_index < len(line):
                    # Get the next character
                    char = line[self.whiskers_choices.current_char_index]
                    self.whiskers_choices.current_char_index += 1
                    return char
                else:
                    # If the whole line is displayed, move to the next line
                    self.whiskers_choices.current_story_index += 1
                    self.whiskers_choices.current_char_index = 0
                    return '\n'  # New line after the whole line is displayed
            else:
                # Move to the next state after the story is complete
                self.transition_to_next_state()
                return None  # No more lines to display
        return None
    
    def get_current_stage_info(self):
        if self.current_state == 'intro':
            return { 'scene_desc': self.get_next_line(), 'question': None }
        return self.whiskers_choices.get_stage_info(self.current_state)

    def transition_to_next_state(self, choice=None):
        current_info = self.whiskers_choices.get_stage_info(self.current_state)
        next_states = current_info['next_state']
        if choice in next_states:
            self.current_state = next_states[choice]
            return True
        else:
            return False