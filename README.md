# Computer-Vision-Rock-Paper-Scissors

## Overview

This is a game project that involves creating a deep learning model using a computer vision software called Teacheable Machine and a neutral network to train images of hand gestures that indicate Rock, Paper, Scissors (and nothing) to use in the game of the same name. Tensorflow and Python are the technologies used for this project.

## Milestone 1: Create the Model from Teacheable Machine

- Four classes are created from Teacheable Machine, an open-source computer vision software that takes images using the laptop camera as inputs to represent the different classes: Rock, Paper, Scissors and Nothing.

- Around 2000-2500 images are taken for each class, making as many variations of each hand gesture as possible to maximise the effectiveness of the model during the training phase so that it can accurately predict the class for new images. 
- Many of the variations of each class are different hand placements with respect to the head, using different hands and different ways to show a rock, paper or scissors gesture from a camera's perspective. This will increase the likelihood of the model getting the class right.

- In the game, the computer randomly selects a class whilst the person playing motions a hand gesture. The model determines the class from the hand gesture and the game programme pits it against the class randomly generated from the computer, simulating the game where the person plays against the computer. The programme determines who wins the game by comparing the classes.

## Milestone 2: Create Conda Environment and install Packages: ipykernel, tensorflow and opencv-python
Conda environment created:
![image](https://user-images.githubusercontent.com/80417833/191304295-10a66727-4e8e-4139-a5df-2472ca3f847f.png)
Pip installed for my_env:
![image](https://user-images.githubusercontent.com/80417833/191303682-e8be3384-47ac-462f-9ef6-39c153143c2e.png)
Packages installed within my_env using pip:
![image](https://user-images.githubusercontent.com/80417833/191302966-588abd36-7030-400b-93a7-0476efce68f5.png)
![image](https://user-images.githubusercontent.com/80417833/191303073-3b463a30-3b72-4e3b-b3c7-b24b17d34ad8.png)
![image](https://user-images.githubusercontent.com/80417833/191303417-e68182f2-2404-4f75-8a24-988d5dc87656.png)

## Milestone 3: Code the Rock, Paper, Scissors Game without the Camera/Model

- Created class called RPS.
- RPS has as methods: get_user_choice,get_computer choice, get_winner.
- RPS has attribute options which stores in a list the strings, 'rock', 'paper', 'scissors'.
- Function play(options) plays the game using the RPS methods
- Options shown under if __name__ == __main__

class RPS with __init__ method:
```python
class RPS:

    def __init__(self, options):
        self.options = options
```

get_user_choice gets the input from user in a while loop, accepting under the condition that it exists within options:
```python
    def get_user_choice(self):
        valid_input = False
        while not valid_input:
            user_choice = input('Select Rock or Paper or Scissors: ').lower()
            if user_choice.isalpha and user_choice in self.options:
                return user_choice
            else:
                print('invalid option')
```

get_computer_choice uses the choice function from the random library to pick one from the options (except nothing):
```python
    def get_computer_choice(self):
        computer_choice = choice(self.options)
        return computer_choice
```

get_winner determines by the logic of the game if the user or computer wins the game by storing the (user) winning outcomes in an array and comparing them with the list created with the inputs from both players:
```python
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
```

play(options):
```python
def play(options):
    game = RPS(options)     
    game.get_winner()
```

game options for user and computer within `if __name__ == '__main__':` block:
```python
if __name__ == '__main__':
    options = ['rock','paper','scissors']
    play(options)
```


## Milestone 4: Replace the Manual User Input with the Model

- The function get_user_choice is replaced by get_prediction, which replaces the manual user input with the processed ouput of the model.
- The model output is an array of four numbers representing the prediction probability of each class, of which the class with the highest number is automatically chosen as the user input to the game vs computer.
- The time.time() + 5 variable is used to give the user 5 seconds to present a gesture to the camera, beyond which the predicted class is taken as input.

```python
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
```

## Milsetone 5: Complete Game which plays until User or Computer wins Three Rounds of RPS

- The game while loop runs until user or computer wins three times. 
- The outcome of each game played is stored in the variable round = game.get_winner() 
  - Its outcome recorded as a point added to either computer_wins or user_wins 
  - This resets for each new game.

```python
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
```


