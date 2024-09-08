# Fall 2024 Mini Project assignment by Lucia Gil and Andrew Sasamori

## Exercise 1: Applications of Analog Input
1. what are the "max_bright" and "min_bright" values you found?

 `max_bright` value that corresponded to LED duty cycle of about 100% was found at **32000**

   `min_bright` value that corresponded to LED duty cycle of about 0% was found at **18000**

#### Example output of first 15 values

```txt
30919
30695
30839
31991
31463
31841
31527
31255
31335
31923
30935
31191
31431
31511
31559
```

## Exrcise 2: Sound

1. Using the code in exercise_sound.py as a starting point, modify the code to play several notes in a sequence from a song of your choosing.

We decided to play the song "Happy Birthday", we first found the frequency of the notes: 

```txt
Notes For Happy Birthday
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
C5 = 523.25
```
Then we created an array with the notes the duration and the correct order the notes shoud be played: 

```txt
happy_birthday = [
    (C4, 1), (C4, 1), (D4, 1), (C4, 1), (F4, 1), (E4, 2),
    (C4, 1), (C4, 1), (D4, 1), (C4, 1), (G4, 1), (F4, 2),
    (C4, 1), (C4, 1), (C5, 1), (A4, 1), (F4, 1), (E4, 1), (D4, 2),
    (B4, 1), (B4, 1), (A4, 1), (F4, 1), (G4, 1), (F4, 2)
]
```
Then we wrote a loop for the notes to be played.


## Exrcise 3: Game

1. Edit the exercise_game.py code to compute average, minimum, maximum response time for 10 flashes total.

2. Upload the response time data to a cloud service of your choice.