# test-fds-evac
Testing Result of FDS+Evac.  Thank Timo Korhonen for his helpful guidance.  

The simulation results are demonstrated in this repo, and most of them are based on fds6.5.3.  Some of the test results are compressed in .7z files.  Please unzip .7z files to check the results.  Some of them are output data from FDS+Evac, please use Smokeview to visualize the data.  The major test results include
(1) Group Model and Herding Effect
(2) Pre-Evacuation 
(3) Escape in Hazardous Condition
(4) Falling-Down Model and Faster-Is-Slower Effect

If you would like to run the input file, please use fds6_dump205.exe to run examples.  
If you would like to compile the executable by yourself, please use the source code in the following repo.  
https://github.com/godisreal/fds-smv/tree/dev_653

Major revision of source code is evac.f90, and it is from the original source in FDS repository.  If you would like to compile a version yourself, please take a look at the instruction in code folder.  Thank Randy McDermott.  
https://github.com/firemodels/fds/

If you you have any comment or suggestion, please feel free to send me a message or directly start an issue here.  Your comments are much appreciated.  Have fun!

![](https://github.com/godisreal/test-group-dynamics/blob/master/img/groups.PNG)
![](https://github.com/godisreal/test-group-dynamics/blob/master/img/Ex2018Test-SmokeFED_0036.png)

