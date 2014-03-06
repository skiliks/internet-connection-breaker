internet-connection-breaker
===========================

Internet connection breaker.

Useful for testing web applications stability with internet connection gaps.

How to use:

1. Download python 3.X from http://www.python.org/downloads/ and install (select all features to install). 

2. Clone internet-connection-breaker as .zip file and unzip it on your computer (example C:/internetConnectionBreaker).

3. Write full path to the project into environment variables (PATH).

4. Press the combination "Win+R", type "cmd" in the window and press Enter (run the console of Windows with administrator rules).

5. When your console opened you type "icb.py" and internet-connection-breaker will run on your computer with standart parameters*.

Internet-connection-breaker works with different parameters. 
Connection presented as the stream of waves.
Wave is a period when internet connection is unstable. 

Parameters of internet-connection-breaker:

brakes_amount - number of internet connection breaks in one wave ([0..n] integer)

rakes_pause - time in seconds between internet connection breaks ([0..n] double)

brakes_duration - time in seconds of internet connection break ([0..n] double)

wave_pause - time in seconds between waves ([0..n] double)

wave_type - type of stream ("const", "up", "down", "heel")


What is wave type?

const - stream of waves looks like sinus

up - stream of waves looks like 

down - stream waves looks like 

heel - stream waves looks like 

The standart values of parameters:

brakes_amount = 4

brakes_pause = 2

brakes_duration = 3

wave_pause = 30

wave_type = "const"

How to run icb.py with unstandart parameters?

In command line type icb.py [--name_option=value_option]

Example:

icb.py --brakes_amount=20 --brakes_pause=100 --brakes_duration=3 --wave_pause=20 --wave_type="up"   

in this situation all parameters will changed

or

icb.py --brakes_amount=15

int this situlation only brakes_amount will changed

If you use wi-fi connection or your connection named on another?

1. Open icb.py

2. Change the name of parameter connection_name

3. Save the file

Standart parameter is connection_name = "Подключение по локальной сети"
