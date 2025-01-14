This is a binary distribution of OpenVDS+.

Documentation is available at:
https://osdu.pages.opengroup.org/platform/domain-data-mgmt-services/seismic/open-vds/

Questions, Issues and Bugs can be reported to the OpenVDS issue system:
https://community.opengroup.org/osdu/platform/domain-data-mgmt-services/seismic/open-vds/-/issues

Python:
================================================================================
Install the python wheel like so:
python3 -m pip install openvds-[version_dependent].whl

Now its possible to start python3 and do:
>>> import openvds
>>> openvds.isCompressionMethodSupported(openvds.CompressionMethod.Wavelet)

The last line is suppose to return True.

Please look in share/openvds/examples/SliceServer for an example of how to use
the Python API.

Linux:
================================================================================
Linux runtime dependencies:

On Ubuntu 20.04 the following packages are required as runtime dependencies:
  python3-pip libcurl4 libuv1 libboost-log1.71.0 libxml2

On RedHat 7 the following packages are required as runtime dependencies:
epel-release is needed for boost and python36:
  epel-release

Once epel-release is installed the following packages are needed:
  boost169-log boost169-random boost169-locale libuv libgomp python36

The shared objects are installed into the lib folder, and the tools into the
bin folder. To quickly test out OpenVDS+ execute the following
command:

$ ./bin/SEGYImport

Wavelet should then be listed in the list of available compression methods under
the --compression-method argument documentation.

To build the examples create a build folder inside share/openvds/examples and
run cmake. For example:

$ mkdir share/openvds/examples/build
$ cd share/openvds/examples/build
$ cmake -DCMAKE_BUILD_TYPE=Debug ..
$ cmake --build .

Then you can run the getting started example by doing:
$ ./GettingStarted/getting-started

Windows:
================================================================================
The dll files are installed in the bin folder together with the tools.

To compile the examples use the "Open Folder" functionality in Visual Studio
and open the share/openvds/examples folder. Its also possible to generate a
Visual Studio solution with cmake using the examples folder as the top level
cmake folder.

