# Loupe
A Network on Chip Visualization Tool
# Installation
- Requirements:
  - For Source Code Installation:
    - Python 3.4.4
    - PyQt4
  - For Packaged Installations:
    - No prequisites!
- Process:
  - For Source Code:
    - Download the source code using a github clone
    - Execute `py driver.py` in the source directory
  - For Packaged Code:
    - Download the package appropriate to the operating system
    - Run the package

# General Work Flow:
1. Generate a trace file using GARNET
2. Start Loupe
3. `File` -> `Load Trace`
4. Begin visualizing mesh networks!

# Features:
Loupe:
  - Animation Features
    - Adjust the inverval + start/stop the animation
  - Go To Cycle
    - Instead of manually clicking next cycle, go to a cycle!
  - Buffer Information
    - View the flit characteristics in each VC
![Alt text](https://raw.github.com/dhcabinian/Loupe/Screenshots/window picture.PNG "Main Window")

- Core Picture Shows:
  - Directional Input Buffers
  - Core Input Buffer
  - Input and Ouptut Links

![Alt text](https://raw.github.com/dhcabinian/Loupe/Screenshots/core.PNG "What a core looks like")

- Loupe also supports any 2-ary n-cube mesh

![Alt text](https://raw.github.com/dhcabinian/Loupe/Screenshots/2x2mesh.PNG "2x2 Mesh")

![Alt text](https://raw.github.com/dhcabinian/Loupe/Screenshots/4x4 mesh.PNG "4x4 Mesh")

# Known Bugs:
1. State is not maintained on any pevious cycle or go-to-cycle transition
  - This means that in order to get a 100% accurate state, next cycle button must be used
