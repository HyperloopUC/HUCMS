# Introduction
Here is where we will be storing all our code to simulate the sensor data
generated in a pod run. All our software will be written in Python for now.
Reach out to Wayne Stegner or Dival Banerjee in Slack if you have any questions
or are interested in contributing.

Our objective is to emulate sensor data to play back to the BeagleBone Black
We need to be able test the following cases for each sensor:
- Startup checklist
- Nominal case
 - We will generate the sensor data for a run and store that data as a csv and be
    able to send that data to the FPGA

## Why are we doing this?
We don't have an actual tube or track to test on. Without this, we have no data
for sensors to test the electronics. Thus, we need to emulate the sensor data
with software in order to test our pod accurately and safely.

# Good programming practices
In order to maintain organization over several years, we must follow good
programming habits. Developers at Google and Facebook are good at writing code,
not because of their intellect, but because of their good communication skills
with each other. For most of you, this is your first tine writing code for a
large project with multiple developers. Your code should be clear enough so that
if you did not look at it for 6 months, and began to work on it again, you'd be
able to understand it. I want all contributors to follow these guidelines when
writing code.

- Limit line length, no line of code should be longer than 80 characters
- Use consistent names for variables, try to write out an entire word instead of
  abbreviating or making acronyms. For example,
    don't do this: imgfromfn();   
    do this: imageFromFileName;
- For variable and function names, capitalize the first letter of each word,
  except for the first word
- Use proper indentation
- Split your programs into multiple files and use folders
- Don't hardcode
- Validate method arguments with if tests
- Comment your code thoroughly as you write it, not after
- Don't add comments for obvious things
- Use github effectively(commits, pushing, pulling, branching, merging)
- Commit your code often
- Don't edit files that others are editing. If you want to, make a separate
  branch

# Deadlines:
- Will update soon by Tuesday
# Tasks:
- Will update soon by Tuesday
# Sensors:
- 5 Pneumatic Pressure Sensors M7139-05KPN-5
  - Part number: M7139-05KPN-5
  - Technical details:
    https://www.mouser.com/ProductDetail/Measurement-Specialties/M7139-05KPN-500000?qs=XPZ2fBHvBHJqUi2uui5CLg%3D%3D
- Battery Box Pressure Sensor M3031-000005-100P
  - Part number: M3031-000005-100P
  - Technical details:
  https://www.digikey.com/product-detail/en/te-connectivity-measurement-specialties/M3031-000005-100PG/MSP3101P2-ND/206884

- 1 Emsiso emDrive 500 Motor controller
  - CAN L, CAN H
  - Technical details: https://www.emdrive-mobility.com/emdrive-500
- 1 Orion BMS 2 36 Cell Configuration (CAN Bus)
  - Technical details:
    https://www.orionbms.com/downloads/documents/orionbms2_specifications.pdf
  - IO:
    - 2 Digital signal outputs for enabling charge and discharge
    - 1 Digital signal output to control a battery charger
    - 5 Digital programmable multi-purpose outputs
    - 2 Digital programmable CANBUS (CAN2.0B) interfaces
    - 3 Analog 0-5v outputs that represent the following signals:
      Charge / Discharge Current Limits and State of Charge (SOC)
    - 1 PWM fan output and fan speed feedback monitor(uses MPO4)
    - 8 Thermistor inputs
    - 1 Dual range current sensor input

- 5 Ambient temperature sensors Blaze Technical 112118-R-120-BATT RTD
  - Can't find data sheet yet :C
- 3 Accelerometers ADXL326
  - Part number: ADXL326
  - Technical details:
    https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL326.pdf
- 2 QS30 Diffuse-Mode Laser(Reflective tape sensor)
  - Technical details:
    https://www.bannerengineering.com/us/en/products/sensors/photoelectric-sensors/qs30-series.html?sort=4#all
  - Use timestamps
- Optical encoders  OJ5028
  - Part number:  OJ5028
  - Technical datasheet:  https://www.ifm.com/us/en/product/oj5028
  - Use raw bitsteam

# Helpful links:
- If you don't know Python or need a refresher, check out this site:
  https://www.pythonforbeginners.com/basics/python-quick-guide
- If you need help with Github:
  https://help.github.com/en/desktop/getting-started-with-github-desktop
- UIUC Hyperloop Github Repo: https://github.com/IlliniHyperloopComputing/Pod
  - This is a good example of how large teams use Github
- Competition 4 FDP:
  https://docs.google.com/document/d/1VyZiGVuFcsHgQypDGP2s--6cPAQ8PxP53GrLnEdr3SY/edit?usp=sharing
- What is CAN BUS(Well explained)
  - https://www.quora.com/What-is-a-CAN-bus

You can also reach out to me, Wayne or Heath on Slack if you have any questions!
