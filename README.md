# Blinking Detection Project with OpenCV

This repository contains a solution for blinking detection with landmark detection on OpenCV. I uploaded a .rar file because the size of the Landmark module is nearly 100MB. The total size of the project is 150MB.

<img src="https://i.hizliresim.com/Fjq2fE.png" data-canonical-src="https://i.hizliresim.com/Fjq2fE.png" width="300" height="300" />


#### Important Note: You should run it as adminastrator. Because communication between python and c # is provided by blinktext.txt file. And if you don't run as adminastrator, program cannot change text file and you will get error.

--- 

### Requirements:

```
Python 3.7+
pip install -r requirements.txt
```

--- 

### How It Works:

There are two main parts in this project: Algorithm in python and GUI in C#

#### Algorithm in Python

- In the algorithm part used (shape_predictor_68_face_landmarks.dat) file for detecting face landmarks. Then I found dots that represent eyes. (Image 1: 36-41 for right and 42-47 for left eye).

- When I detect where the eyes are, drew two lines longitudinally and laterally. Now I have open and close information for both eyes.

- But I want to detect blinking. But I wanted to detect blinking. Therefore, I have compared the two lines that I have obtained in very short intervals in a while loop and I have taken the ratio of these ratios. 

- If the final ratio is lower than the threshold which I set, our algorithm send a 'blinked' message to our C# GUI with blinktext.txt. You can check Image 2 for the ratio of ratios. 

#### GUI in C#

- When the user press the Start Detecting button C# runs python code(blinking_detectionD.py). It can take 10 seconds to start detecting. If the user doesn't blink for 25 seconds, a warning message appears in the lower right corner of the screen.
- Having trouble button deletes the contents of the blinktext1.txt file. blinktext1.txt file contains 'exit' information for while in python code. If any conflict happens and this text becomes 'exit' before the start, the user should press the Having Trouble button.

--- 

### Image 1 And Image 2:



<p float="left"   >
<img src="https://i.hizliresim.com/rwnVIG.png" data-canonical-src="https://i.hizliresim.com/rwnVIG.png" width="400" height="300"  />
<img src="https://i.hizliresim.com/fozbNX.png" data-canonical-src="https://i.hizliresim.com/fozbNX.png" width="400" height="300" />
</p>







 
