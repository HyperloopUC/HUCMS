## Introduction
Here is where we will be storing all our code to simulate the sensor data
generated in a pod run. All our software will be written in Python for now.
Reach out to Wayne Stegner or Dival Banerjee in Slack if you have any questions
or are interested in contributing.

Our objective is to emulate sensor data to play back to the BeagleBone Black
We need to be able test the following cases for each sensor:
- Startup checklist
- Nominal case
- Sensor failure

# Why are we doing this?
We don't have an actual tube or track to test on. Without this, we have no data
for sensors to test the electronics. Thus, we need to emulate the sensor data
with software in order to test our pod accurately and safely.

## Good programming practices
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


## Deadlines:

## Tasks:
- Will update soon
## Sensors:
- 7 Analog pressure sensors
- 5-40 RTD Thermal sensors
- 1 Motor controller
- 1 BMS (CAN Bus)
- 3 Accelerometers
- 4 Contrast sensors
## Helpful links:
- If you don't know Python or need a refresher, check out this site:
  https://www.pythonforbeginners.com/basics/python-quick-guide


You can also reach out to me, Wayne or Heath on Slack if you have any questions!
