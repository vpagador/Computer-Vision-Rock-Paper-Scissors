from random import choice
import cv2
from keras.models import load_model
import numpy as np
import time  


class RPS:

    def __init__(self, options):
        self.options = options

    def get_winner(self):
        # store user win outcomes in list
        win_outcomes = [['rock','scissors'], ['scissors','paper'], ['paper','rock']]

        who_won ='draw'
        user = self.get_prediction()
        computer = self.get_computer_choice()
        # store in battle variable in order of user then computer
        battle = [user,computer]
        print(battle)
        # determine outcome of game depending on exisitence of any win_outcome
        if user == computer:
            print('\ndraw')
        elif battle in win_outcomes:
            print('\nYou win!')
            who_won ='user'
        else:
            print('\nYou lose!')
            who_won ='computer'
        return who_won

    def get_computer_choice(self):
        computer_choice = choice(self.options[0:2])
        return computer_choice

    def get_prediction(self):
        model = load_model('converted_keras/keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        select_class = None
        
        end_time = time.time() + 5

        while True: 
            timer = time.time() 

            # load model and predict data
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            print(prediction, time.time())
            
            # retrieve class with highest probability
            print(max(prediction[0]))
            class_list = []

            for i in prediction[0]:
                class_list.append(i)
            for i in range(len(class_list)):
                if class_list[i] == max(prediction[0]):
                    select_class = self.options[i]

            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif timer >= end_time:
                print(f'\nYou chose {select_class}')
                break

        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return select_class

def play(options):
    game = RPS(options)
    num_rounds = 3
    computer_wins=0
    user_wins =0
    # play games until user or computer gets 3 wins first
    game_winner = 'n'
    while game_winner == 'n':    
        round = game.get_winner()
        if round =='user':
            user_wins += 1
        elif round =='computer':
            computer_wins +=1
        # show score
        print(f'{user_wins} - {computer_wins}')
        if user_wins == num_rounds:
            game_winner = 'y'
            print(f'\nYou won {num_rounds} rounds')
        elif computer_wins == num_rounds:
            game_winner = 'y'
            print(f'\nYou lost {num_rounds} rounds')
        
    
if __name__ == '__main__':
    options = ['paper','scissors','rock', 'nothing']
    play(options)

# %%