# FLUIDLENGTH
Fiber optics are a well-known tool these days. Its applications are multiple, ranging from
television, internet, decorations and more. As part of this project, we focused on
another of the many uses of fiber optics, we have tried to develop a pressure sensor using
optical fiber. More specifically, we want:
1. Determine the pressure according to the intensity transmitted from one fiber to another
2. Find the depth of a container based on the pressure applied to the diaphragm
3. Develop python software to receive real-time pressure and intensity variations
applied to the device

-Optical Fiber:

    Fiber optics is a cable used to propagate light waves between two places. The light
    is conducted without loss to the core of the cable. The maximum amount of light the fiber can accept is
    the numerical aperture NA which corresponds to the product of the refractive index of the medium by the sine of
    the angle of the extreme ray in this medium.
    So the larger the diameter of the fiber core, the greater the ability to capture light.
    
-Intensity-based pressure sensors:

    he method that seemed the simplest to us for measuring pressure with optical fibers
    was to have an "iris diaphragm" whose aperture would change with pressure. Thus, we have
    developed the device used for this project. The operation of the device is simple: when a pressure
    is applied to the membrane, the latter deforms so that the pressure inside the device is equal to that
    exterior, according to the ideal gas law:
                                       p1v1 = p2v2
    This deformation will partially block the passage of light, which causes a drop in the intensity captured.
    by the detector.
    By finding the relationship between the intensity and the pressure applied to the device, it will be possible to
    determine the pressure with the intensity captured.
   
   
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
