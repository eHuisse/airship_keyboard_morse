# Airship software

This is a school project to make an autonomous indoor airship. This package contain the first simulation file. This simulation is only used to make sure ROS package work fine.

## Getting Started

We choose to use morse simulator your can find the install instruction on :
* [Morse](https://www.openrobots.org/morse/doc/1.2/user/installation.html) - The simulator used

### Installing

Create a file named morse_ws in your root directory :
```sh
mkdir morse_ws
```
When it done copy the morse_train directory containing 3D environnement in :
```sh
/usr/share/morse/data/environments/
```
Then you need to copy all this package in your brend new morse_ws.

Then import the project
[Import morse project](http://manpages.ubuntu.com/manpages/trusty/man1/morse-import.1.html) - Import the project

## Running the tests
If you type :
```sh
morse run airship_keyboard
```
It should display the simulation.
