Run a fds case by using evac2020.exe or the latest version of official fds (fds6.7), and ensure you get a .prt5 evac data file which is named by CHID_evac_0001.prt5.  Then run the python script as below
python main.py filename.fds

Here filename.fds is the input file of fds, by which CHID_evac_0001.prt5 is generated.  
The python script needs pygame to enable visualization of evac data.   

If you are using old version of fds you need to slightly modify the main.py as below.  

By using evac2020.exe or the latest version of official fds (fds6.7):

    readPRTfile(CHID+'_evac_0001.prt5')
    visualizeEvac(CHID+'_evac_0001.npz', file1)
	
By using the previous version of fds program:
	
	readPRTfile(CHID+'_000x.prt5')
    visualizeEvac(CHID+'_000x.npz', file1)

000x could be 0001 or 0002... , which is the evac part5 data file.  

Comments and suggestions are welcome.  