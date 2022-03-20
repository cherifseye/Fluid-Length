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
      
      
-GET WATER LEVEL

     Fonction: __waterlevel__(pin, unity)
     Argument: 
            -pin: The number of the Analog pin
     As a output this function will return the value of the water level 
     An example is provide in the file example.py(Example8: get water level ADC.
     Please read the comment on file to understand how it's working)
