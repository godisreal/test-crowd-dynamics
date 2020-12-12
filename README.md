# test-fds-evac
Testing Result of FDS+Evac.  Thank Timo Korhonen for his kindly help and guidance.  

The simulation results are demonstrated in this repo.  Some of them are compressed in .7z files.  Please unzip .7z files to check the simulation results.  Some of them are output data from FDS+Evac, please use Smokeview to visualize the result.  The major test results include
(1) Group Model and Herding Effect
(2) Pre-Evacuation 
(3) Escape in Hazardous Condition
(4) Falling-Down Model and Faster-Is-Slower Effect

If you would like to run the input file, please use fds6_dump205.exe to run examples.  
If you would like to compile the executable by yourself, please use the source code in the following repo.  
https://github.com/godisreal/fds-smv/tree/dev_653

If you you have any comment or suggestion, please feel free to send me a message or directly start an issue here.  Your comments are much appreciated.  

![](https://github.com/godisreal/test-group-dynamics/blob/master/img/groups.PNG)
![](https://github.com/godisreal/test-group-dynamics/blob/master/img/Ex2018Test-SmokeFED_0036.png)

Major revision of source code is evac.f90, and it is from the original source in FDS repository.  If you would like to compile a version yourself, please take a look at the instruction in code folder.  
https://github.com/firemodels/fds/