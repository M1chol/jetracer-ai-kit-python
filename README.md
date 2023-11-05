# Python examples for JetRacer robot car
This repository contains python files and Jupyter notebooks for JetRacer car,
## In this repo I provide you with 
Jupyter Notebooks for:   
1. steering car with controller using pygame
2. steering car with controller using ipwidgets
3. controlling LIDAR and simple mapping
examples are provided in english and polish in thier respective folders.
   
Python files for:
1. steering car with controller using pygame   
coming:
2. controlling LIDAR and simple mapping

## Instructions  
Here is the translation of the provided Markdown file:

## Running in a Jupyter Notebook Environment
The advantage of this method is the speed of preparing the robot.

1. Turn on the robot.
   Note: If you want to work from a computer other than the robot, it is necessary to connect the robot to the network.
2. Log in to Jupyter Notebook.
   If you are working on the robot, open a web browser and connect to the address `localhost:8888` or `127.0.0.1:8888`.
   If you are working from another computer in the same network, connect to the robot's IP address (displayed on the screen) at port `8888`.
3. Log in to the notebook using the password `jetson`.
4. Download notebook files from the repository at https://github.com/M1chol/jetracer-ai-kit-python.
5. Add the files to `/Jetracer/notebooks` in the `Files` tab.
6. Run the files.

## Running the robot directly
The advantage of this method is skipping the visual environment of Jupyter, which allows for full visual libraries like matplotlib or cv2.

1. Turn on the robot.
2. Install the VS Code development environment. Instructions can be found [here](https://code.visualstudio.com/docs/setup/linux).
3. Install the Python extension - Extensions can be directly downloaded in the VS Code application in the `Extensions` tab.
4. Go to the Source Control tab.
5. Click on `Clone Repository` and paste the link `https://github.com/M1chol/jetracer-ai-kit-python.git`.
6. Choose the folder where the repository will be cloned.
7. Select Python 3 as the environment in the lower right corner.
8. Run the files.


## Why not use provided examples?
1. my robot bought on Botland didn't come with working examples on teleoperation
2. I provided more examples - like LIDAR

---
![image](https://cdn1.botland.com.pl/118347/jetracer-ros-ai-kit-a-4-kolowa-platforma-robota-wyscigowego-al-nvidia-jetson-nano-developer-kit-b01-waveshare-23756.jpg)   
