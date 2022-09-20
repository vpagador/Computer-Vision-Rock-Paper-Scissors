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

get_user_choice gets the input from user in a while loop, accepting under the condition that it exists within options:
![image](https://user-images.githubusercontent.com/80417833/191307796-01ce62f2-7486-4a3e-8f56-7528a9a85573.png)

get_computer_choice uses the choice function from the random library to pick one from the options:
![image](https://user-images.githubusercontent.com/80417833/191306264-99cbdbd7-7ce4-4da1-b265-50a997da4114.png)

get_winner determines by the logic of the game if the user or computer wins the game by storing the (user) winning outcomes in an array and comparing with the list created with the inputs from both players:
![image](https://user-images.githubusercontent.com/80417833/191306722-067cc9a9-d781-4f63-b5b0-33ad07173111.png)


