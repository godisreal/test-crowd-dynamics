# test-fds-evac
Testing Result of FDS+Evac.  Thank Timo Korhonen for his helpful guidance.  

The simulation results are demonstrated in this repo, and most of them are based on fds6.5.3.  Some of the test results are compressed in .7z files.  Some of them are output data from FDS+Evac, please use Smokeview to visualize the data.  The major test results include
(1) Pre-Evacuation 
(2) Escape in Hazardous Condition
(3) Falling-Down Model and Faster-Is-Slower Effect

If you would like to run the input file, please use fds6_dump205.exe to run examples.  

Major revision of source code is evac.f90, and it is from the original source in FDS repository.  If you would like to compile a version by yourself, please take a look at the instruction in FDS official websit.  

Since 2022 evac module has been decoupled from fds, and Timo is trying to provide a new version of evac and it may become a new independent project from fds. If you you have any valuable comment or suggestion, please feel free to send a message to Timo or me, or directly start an issue here.  Your comments are much appreciated.  Have fun!

![](https://github.com/godisreal/test-group-dynamics/blob/master/img/groups.PNG)
![](https://github.com/godisreal/test-group-dynamics/blob/master/img/Ex2018Test-SmokeFED_0036.png)

