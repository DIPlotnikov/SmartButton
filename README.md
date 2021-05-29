# SmartButton
Class for determining the type of button click for raspberry pi 2. 
Used to control the device with a single button. 
Different functions can be associated with different types of button clicks.
The program returns one of two possible values: 
- "long_push" (str); 
- amount of clicks (int).

Parameters:
- pin - pin number (BCM)
- time_to_wait - waiting time between short taps, the program counts the taps if the time has passed.
- time_longpush - time " pressed and hold" 
