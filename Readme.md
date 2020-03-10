## Installation  

Install Python3 if it's not yet there.  
To do this on Ubuntu, run:  

sudo apt-get update  
sudo apt-get -y install python3.7  

For more details or other OSs please follow the documentation:  
https://docs.python.org/3/using/unix.html  
https://docs.python.org/3/using/windows.html  

Install PIP if it's not yet there. To do this on Ubuntu, run:  

sudo apt-get update  
sudo apt-get -y install python3-pip  

For more details please follow the documentation:  
https://pip.pypa.io/en/stable/installing/  

Install matplotlib, sklearn, yfinance if they are not yet there.  
To do this on Ubuntu, either run:  

sudo pip3 install sklearn  
sudo pip3 install yfinance  
sudo pip3 install matplotlib  

Or:  

sudo pip3 install -r requirements.txt  

## Running  

To run the program locally, from the current folder, execute:  

python3 simulate_close_price.py  

The output will be shown in the console.  
The chars will be saved in the charts folder.  

To run the program on an image, from the current folder, execute:  

docker build --tag=model_rui .  
docker run model_rui:latest  

The output will be shown in the console.  
