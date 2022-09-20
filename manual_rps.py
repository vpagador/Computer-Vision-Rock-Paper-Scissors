from random import choice

class RPS:

    def __init__(self, options):
        self.options = options

    def get_winner(self):
        # store user win outcomes in list
        win_outcomes = [['rock','scissors'], ['scissors','paper'], ['paper','rock']]

        user = self.get_user_choice()
        computer = self.get_computer_choice()
        # store in battle variable in order of user then computer
        battle = [user,computer]
        print(battle)
        # determine outcome of game depending on exisitence of any win_outcome
        if user == computer:
            print('draw')
        elif battle in win_outcomes:
            print('You win!')
        else:
            print('You lose!')

    def get_computer_choice(self):
        computer_choice = choice(self.options)
        return computer_choice

    def get_user_choice(self):
        valid_input = False
        while not valid_input:
            user_choice = input('Select Rock or Paper or Scissors: ').lower()
            if user_choice.isalpha and user_choice in self.options:
                return user_choice
            else:
                print('invalid option')

def play(options):
    game = RPS(options)     
    game.get_winner()

    pass

if __name__ == '__main__':
    options = ['rock','paper','scissors']
    play(options)
