# Project for Programming in Cognitive and Brain Sciences class - 2019

## Simulating agents utilizing a homeostatic reinforcement learnign algorithm in an anticipatory responding experiment

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
