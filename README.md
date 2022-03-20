# Pyduino
pyduino is a python module that help to make arduino code using python

-LIGHT ON A LED:

    Fonction: __on__(pin)
    Argument: 
            pin: The number of the digital pin
    As a output this function will turn on the led.
    You can see the exemple in the file example.py (Example1:turn on a led)
    
-SWITCH OFF A LED:

    Fonction: __off__(pin)
    Argument: 
            pin: The number of the digital pin
    As a output this function will turn on the led.
    An example is provide in the file example.py(Example2: blink a LED)
   
   
 -SWITCH BUTTON:
 
    Fonction: __switch__(pin)
    Argument: 
            pin The number of the digital pin
    As a output this function will return the switchstate (1 if if the button is pressed or 0 otherwise).
    An example is provide in the file example.py(Example3: Control 2 LED using a switch button. 
    Please read the comment on file to understand how it's working)
    

-GET THE POTENTIOMETER VALUE:

    Fonction: __pot__(pin)
    Argument: 
            pin: The number of the Analog pin
    As a output this function will return the value of the resistance of the potentiometer.
    An example is provide in the file example.py(Example4: Control LED brightness using a potentiometer.
    Please read the comment on file to understand how it's working)
                                                
                                                
                                      
-GET TEMPERATURE VALUE USING TMP102 SENSOR
   
    Fonction: __tmp102__(pin, unity)
    Argument: 
            -pin: The number of the Analog pin
            -unity: the unity that you want get you temperature (F for farenheit) and (C for celsius)
    As a output this function will return the value of the temperature in farenheit or celsius 
    An example is provide in the file example.py(Example5: The temperature monitor using a tmp102 sensor.
    Please read the comment on file to understand how it's working)
   
   
-GET PIR SENSOR MOVE DETECTION
    
    Fontion: --HC_SR04PIR__(pin):
    Argument:
            pin: The number of the digital pin
    As a output you'll get the the value of the pir sensor.
    An example is provide in the file example.py(Example6: Move dection using pir sensor.
    Please read the comment on file to understand how it's working)
    
    
-GET POSTION USING ANALOG JOYSTICK

      Fonction: __analogJoystick__(pin, unity)
      Argument: 
            -swpin: The number of the digital pin
            -Xpin: The number of analog pin for X position
            -Ypin: The number of analog pin for Y position
      As a output this function will return the position of your analog joystick
      An example is provide in the file example.py(Exampl7: Analog joystick position.
      Please read the comment on file to understand how it's working)
      
      
-GET WATER LEVEL

     Fonction: __waterlevel__(pin, unity)
     Argument: 
            -pin: The number of the Analog pin
     As a output this function will return the value of the water level 
     An example is provide in the file example.py(Example8: get water level ADC.
     Please read the comment on file to understand how it's working)
