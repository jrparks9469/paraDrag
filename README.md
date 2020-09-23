# Component Drag Buildup

The Drag Package contains the classes and methods necessary for performing a component drag buildup using the methods found in *Aircraft Design: A Conceptual Approach* by. Daniel Raymer.

## Usage

The package reads data regarding the aircraft from a csv file using a format specified in the docs

```python
from Drag import drag_in
from Drag import drag_out

plane = drag_in.read_aircraft_file()
drag_out.write_output(plane)
```

This script asks for the location of the aircraft file and writes the output to a csv files, specifying drag contributions and the total parasite drag.

---

## Input File

The input file specifies the following flight characteristics:

* Freestream Velocity (fps)
* Altitude (ft)
* Reference Area (sq. ft)

The specified components on the aircraft may be one of:

* Airfoil (wing / stabilizers)
* Fuselage
* Store / Nacelle
* Flow Diverter
* Flap
* Spoiler

## Output File

THe output file is placed in a folder titled *drag_results*. The csv file name is *aircraftName_altitude_mach*.csv.  It specifies the following:

* Parasite drag for each component
* Form factor for each component
* Interference factor for each component
* Percent Contribution of eac hcomponent
* Total parasite drag
