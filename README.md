# Blink Detection Project with OpenCV and dlib

This repository contains a solution for blinking detection with landmark detection on OpenCV and dlib.

<img src="https://i.hizliresim.com/Fjq2fE.png" data-canonical-src="https://i.hizliresim.com/Fjq2fE.png" width="300" height="300" />


#### _Important Note_ : This branch contains only python code. If you want to access all project you should check main branch.

#### _Important Note 2_ : You must keep the landmark file in the same directory as the model. I am sorry about the size of the landmark file but I cannot shrink it.

#### _Important Note 3_ : Don't forget to start Shell as administrator before running the program. If you forget, it may cause a permission error for the reason that I explained in the main branch.
--- 

### Requirements:

```
Python 3.7+
pip install -r requirements.txt
```

--- 

### How It Works:

```
python BlinkDetection.py
```

There are two main parts in this project: Algorithm in python and GUI in C#

#### Algorithm in Python

- In the algorithm part used (shape_predictor_68_face_landmarks.dat) file for detecting face landmarks. Then I found dots that represent eyes. (Image 1: 36-41 for right and 42-47 for left eye).

- When I detect where the eyes are, drew two lines longitudinally and laterally. Now I have open and close information for both eyes.

- But I want to detect blink. But I wanted to detect blinking. Therefore, I have compared the two lines that I have obtained in very short intervals in a while loop and I have taken the ratio of these ratios. 

- If the final ratio is lower than the threshold which I set, our algorithm send a 'blinked' message to our console. You can check Image 2 for the ratio of ratios. 

--- 

### Image 1 And Image 2:



<p float="left"   >
<img src="https://i.hizliresim.com/rwnVIG.png" data-canonical-src="https://i.hizliresim.com/rwnVIG.png" width="400" height="300"  />
<img src="https://i.hizliresim.com/fozbNX.png" data-canonical-src="https://i.hizliresim.com/fozbNX.png" width="400" height="300" />
</p>







 
