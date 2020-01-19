# Project for Programming in Cognitive and Brain Sciences class - 2019

## Simulating agents utilizing a homeostatic reinforcement learning algorithm in an anticipatory responding experiment

This project aims to reproduce the simulation summarized by Figure 1 of **Keramati & Gutkin (2019)**.
The article can be freely accessed at: https://elifesciences.org/articles/04811

Briefly, the authors simulate rats in an eperimental task, in which they receive a forced drop of temperature by an ethanol injection.
The injection always follows a cue, so the rats can learn an anticipatory tolerance response and increase their temperature in advance.
There are 10 trial blocks overall, during the 9th block (the extinction block), there is no injection, but there is a cue.
Each block is a day, and there are 4 measurements of temperature at 30, 60, 90 and 120 minutes following the time of injection.

Plotted are:
- the temperature changes following the injection
- the temperature changes following the tolerance response
- the temperature changes following both an injection and a tolerance response
- the probability of initiating a tolerance response
- the temperature measurements

The authors simulate the rats' behaviour using their homeostatic reinforcement learning algoirithm, which computes rewards based on
deviations from a homeostatic setpoint (for details, see the article).

Note however, that the results of my project only qualitatively match the original work in some places, since some information required for
a perfect match (such as initial Q values or the exact function used to simulate the temperature changes) are not found in the article.

To run the simulation simply execute the python script called 'homeo_RL.py'. The script will run the simulation, store the interesting data in variables and create the plots from the study.

## Previous coding experience

I have gained programming experience in MATLAB and R.
I have used MATLAB in my undergraduate studies for running a behavioural experiment and for analysing  EEG data. I also tend to use MATLAB when I try to educate myself in computational neuroscience.
I have used R mainly for data analysis in my undergraduate studies. R is basically my first choice when it comes to statistical computing.

## What I learned in the course

I have learned the basics of python thanks to the course. It is a language I always wanted to get into as it is much more general than MATLAB and R. I found it very useful and pretty quickly grasped the basics of it thanks to the lectures and the TDs. I definitely have not become proficient in it yet, but now I know how to start to get better. I think my choice of project was fitting for my goals for this class.
Also, I have finally learned hwo to use github, which was a second thing I always procrastinated learning. This is very useful as well.

## What I missed in the course

I think the major shortcoming of the course is that it aims to be very general. This makes sense because people without any coding experience and those who are already good programmers are in the same group. But this makes the course a bit unfocused and most of the time instead of getting in depth knowledge on a topic we just very quickly went over it. I think it would make sense to separate people according to what they think they should be learning and wht experience they already have. This way people can get some more detailed knowledge on their own interests.
