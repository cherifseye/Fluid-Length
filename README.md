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
   
   
 -Diaphragm modeling:
 
 <img src="https://github.com/cherifseye/Fluid-Length/blob/master/diaphragme.jpg" alt="drawing" width="200"/>
 
    Given the operating principle of the device we wanted to design, we needed a membrane that could be deformed under pressure. 
    Thus, we choose thin atex as the membrane. In order for a deformation to be observable when the device is in water, the latter must 
    be watertight so that a pressure difference is observable between the interior and the exterior and that the membrane deforms under
    this pressure. pressure difference. We therefore choose to glue microscope slides with QuickSeal to the two holes of the device.
    The structure of the device is itself printed with a 3D printer.
   
    

-Final support modeling:

<img src="https://github.com/cherifseye/Fluid-Length/blob/master/support_lentille.jpg" alt="drawing" width="200"/>

    Finally, we designed a support with a lens in the center and we positioned the fibers at exactly 2f from the lens in order 
    to have a magnification of 1. This support is larger than the first, but it offers much greater precision. bigger. 
    A guide for the placement of the diaphragm has been drawn there in order to position it in the right place and to ensure 
    the passage of the greatest possible quantity of light.
                                                
                                                
                                      
-Membrane
   
    We chose the membrane so that the material is both very stretchy and waterproof,
    so as to make the device waterproof. The most accessible material fulfilling these two criteria is latex.
    thin like surgical gloves, so that's what we used.
   
-Fibers
    
    For the fibers, we had to maximize the amount of light captured and transmitted. Like injecting
    in the first fiber was more precise, we could have a smaller heart, which made it possible to have a
    higher output intensity. However, in order to capture enough light on the other side of the diaphragm,
    the second fiber had to be much larger to compensate for the low precision of the device. The fiber
    at the largest core we found was 2mm, which allowed us to increase the amount of captured light.
    
    
-Assembly

<img src="https://github.com/cherifseye/Fluid-Length/blob/master/montage1.jpg" alt="drawing" width="200"/>
<img src="https://github.com/cherifseye/Fluid-Length/blob/master/montage2.jpg" alt="drawing" width="200"/>

      A laser beam is injected into a highly multimode fiber of 100 micron core, then is 
      guided to the device acting as an iris diaphragm. Depending on the external pressure, a quantity of 
      different light will pass through to the other side and be converged by a biconvex lens with a focal length of
      35mm. The image of the lens is then located directly on a highly multimode fiber of 2mm core,
      which guides the beam to a det-110 detector. This detector emits a signal indicating the intensity of light
      captured and this signal is read by by using an Arduino UNO and the software Fluid Length that we develop.
      
      
-Arduino

<img src="https://github.com/cherifseye/Fluid-Length/blob/master/circuit.jpg" alt="drawing" width="200"/>

    after having received the light which passes through our flexible membrane, the latter is connected to our
    sensor. Thanks to banana wires, one pin of the photo-diode is connected to the ground and the other to a pin of the
    10kΩ resistor and its other pin connected to ground
    
    -Optical Fiber:

    Fiber optics is a cable used to propagate light waves between two places. The light
    is conducted without loss to the core of the cable. The maximum amount of light the fiber can accept is
    the numerical aperture NA which corresponds to the product of the refractive index of the medium by the sine of
    the angle of the extreme ray in this medium.
    So the larger the diameter of the fiber core, the greater the ability to capture light.
    
-Embedded Software FLuid Length:
The software is composed of three parts:

    Configuration:
    This part is mainly composed of four frames.
    — Port Name(1) must contain the information of the name of the port where the arduino is connected(1) for example
    COM3 for windows computers, dev/cu/usbmodem111111 for mac and /dev/tty/USB0 in linux
    — Digital Pin(2) This section contains the pin number to be used at the level of the Arduino connected to a
    LED to do the test part. a spinbox is available ranging from 1 to 13 constituting the digital pins
    available on the Arduino Uno.
    — Analog Pin(3) it is through this pin that the information on the intensity of the light will be received, a
    combo box is available allowing to choose between the analog pins of the available arduino (A0. A1,
    A2, A3, A4, A5)
    — The last frame contains the test(4) and setup(5) buttons. The setup button allows you to connect the device
    plication with the arduino while the test button allows you to check the assembly and the pins have been correctly
    chosen by lighting the led accompanying the assembly. If the system is not properly connected, or the port or
    the wrong pins, an error message will appear.
<img src="https://github.com/cherifseye/Fluid-Length/blob/master/config.png" alt="drawing" width="400"/>
    
    Measures and computations:
    This part consists of taking the intensity values ​​and calculating the corresponding gauge pressure,
    fluid level, and accuracy. It is mainly composed of two frames
    — Liquid Properties:
           — Density: Takes as value the density of the liquid
           — Gravity: takes as input the value of the acceleration due to gravity
           — Specific weight: This button is used to calculate the corresponding specific weight.
    — Measurements:
          — Intensity: This button is used to recover the value of the intensity captured by the photodiode at
          when the user clicked the button.
          — Pressure 0: The user enters the atmospheric pressure, 105000 in the open air and 0 for tank closed.
          — Gauge: This field is directly filled when the user has already clicked on the intensity button,
          the gauge pressure calculation is done automatically.
          — Pressure abs: This button is used to calculate the absolute pressure (Gauge + pressure0)
          — Height This button is used to calculate the height of the liquid by taking the information contained
          in the fields of specific weight and Pressure abs
          — Real height: This field takes as input the real height of the liquid
          — Precision: By pressing this button, the user obtains the precision of his measurement system.
<img src="https://github.com/cherifseye/Fluid-Length/blob/master/Mesures%2520et%2520calcul.png" alt="drawing" width="200"/>

    Graphics:
    In this part the user is able to display in a graph the intensity values according to time.
    By pressing the plot button, the graph shows in real time the value of the intensity captured by the
    photodiode as a function of time for 150 values.
    The clear button allows you to erase the graph and reactivate the plot button
    
<img src="https://github.com/cherifseye/Fluid-Length/blob/master/graphics.png" alt="drawing" width="200"/>
    
    Saving data and Graphics:
    After making the measurements, it is quite possible to save the image of the graph or recover
    the data in a csv file it is also possible to open the image in a matplotlib window or in format
    SVG(Support Vector Graphics)
    To do this, here are the steps to follow:
         — right-click on the part where the graph is displayed, a small window appears and click on
         export.
         
<img src="https://github.com/cherifseye/Fluid-Length/blob/master/export.png" alt="drawing" width="200"/>
    
    — By pressing export a new window opens automatically and you can choose under which
    format you want to export your chart or data with the ability to edit multiple
    settings.
    
<img src="https://github.com/cherifseye/Fluid-Length/blob/master/save.png" alt="drawing" width="200"/>

