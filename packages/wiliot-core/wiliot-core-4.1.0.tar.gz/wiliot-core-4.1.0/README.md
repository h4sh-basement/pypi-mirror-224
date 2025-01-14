# PyWiliot: wiliot-core #

wiliot-core is a python library for accessing Wiliot's core functions such as communicating with
Wiliot's local gateway and working on the packets data

## Public Library

### MAC Installation
#### Getting around SSL issue on Mac with Python 3.7 and later versions

Python version 3.7 on Mac OS has stopped using the OS's version of SSL and started using Python's implementation instead. As a result, the CA
certificates included in the OS are no longer usable. To avoid getting SSL related errors from the code when running under this setup you need
to execute Install Certificates.command Python script. Typically you will find it under
~~~~
/Applications/Python\ 3.7/Install\ Certificates.command
~~~~

#### Python 3 on Mac
The default Python version on mac is 2.x. Since Wiliot package requires Python 3.x you should download Python3 
(e.g.  Python3.7) and make python 3 your default.
There are many ways how to do it such as add python3 to your PATH (one possible solution https://www.educative.io/edpresso/how-to-add-python-to-the-path-variable-in-mac) 

#### Git is not working after Mac update
please check the following solution:
https://stackoverflow.com/questions/52522565/git-is-not-working-after-macos-update-xcrun-error-invalid-active-developer-pa


### Installing pyWiliot
````commandline
pip install wiliot-core
````

### Using pyWiliot
Wiliot package location can be found, by typing in the command line:
````commandline
pip show wiliot-core
````
please check out our examples, including:
* [gateway communication](wiliot_core/local_gateway/examples)
* [packet data](wiliot_core/packet_data) (at the end of each script)

For more documentation and instructions, please contact us: support@wiliot.com


## Release Notes:
Version 4.1.0:
-----------------
* add new version for GW FW
* improve socket connection for tcp/ip communication with GW
* improve get df for tag collection class

Version 4.0.13:
-----------------
* improve visualization of GW FW version updates.
* add new version for GW FW

Version 4.0.9:
-----------------
* improve Wiliot Dir
* add support to multiple api keys for the same owner id and environment bud different clients
  
Version 4.0.8:
-----------------
* continuous listener as multi-processes:
    * add option to specify log path and communicate reading error using event
    * connect to gw in a more robust way including printing exceptions if needed
* local gw core:
    * connect only to “Silicon Lab”/"CP210.." ports (Wiliot's gw driver)
    * added a function to check gw response using version command check_gw_responds including is_gw_alive function
    * better handling ACK msg from the GW
    * get reading status function get_read_error_status. 
    * better stop gw app including writing a log if no ACK was received for the cancel command
    * add new GW FW version
* packet:
    * add new function to packet to retrieve basic data: get_adva, get_flow, get_rssi


Version 4.0.6:
-----------------
* First version


The package previous content was published under the name 'wiliot' package.
for more information please read 'wiliot' package's release notes
  
  
   



