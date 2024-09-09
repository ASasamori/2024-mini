# Fall 2024 Mini Project assignment by Lucia Gil and Andrew Sasamori

## Exercise 1: Applications of Analog Input

1. what are the "max_bright" and "min_bright" values you found?

1. `max_bright` value that corresponded to LED duty cycle of about 100% was found at **43000**
   `min_bright` value that corresponded to LED duty cycle of about 0% was found at **19000**

#### Example output of first few values

```txt
19460
19860
22277
22597
22853
22965
23029
23877
27062
28743
28454
28246
25574
23957
25670
26662
26694
28198
31367
31415
29687
24565
25158
32071
37161
40953
41786
41834
42378
42474
42474
42650
42634
42714
42970
42954
43050
42954
42970
43114
42810
42378
42426
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
