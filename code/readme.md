The file evac.f90 is compiled with FDS+Evac 6.5.3.  Here I attach the file to track the code changes.  
The entire program is in FDS repository.  
You may download an execuable file here.  If you need all the source files, please feel free to send me an email or use issue tracker to submit a request, or use the source code in the following repo.  
https://github.com/godisreal/fds-smv/tree/dev_653

The latest two versions of execuable are fds6_dump205.exe and fds6_tmpg.exe
In particular fds6_dump205.exe enables users to visualize both evac data and fire data in smokeview when multiple evac simulations are run with the same fire scenario.  

The execuable requires .dll for gcc and gfortran runtime library.  The required .dll files are included in gcc-4.9-win32.7z.  You can also use the gfortran in the gcc-4.9-win32.7z compile the execuable by yourself on Microsoft Windows platform.  Have fun!