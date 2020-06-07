import time
import random
import subprocess
import os

# sudo modprobe pcspkr
# sudo apt install beep

swap_min = int(input("Enter minimum swap-time (seconds): "))
swap_max = int(input("Enter maximum swap-time (seconds): "))
seed = input("Enter a random word: ")
random.seed(seed) 
num_players = int(input("Enter the number of players: "))
player_id = int(input("Enter your player id (0-" + str(num_players - 1) + "): "))
input("Press enter at the same time: ")

swap_num = 1

def run_cmd(cmd):
	sp = subprocess.run(cmd.split())

def init():
	for i in range(0,num_players):
		run_cmd("git checkout -B room_" + i)
	run_cmd("git checkout -B room_" + player_id)

init()

def swap():
	run_cmd("git add -A")
	run_cmd("git commit -m \"swap_\"" + str(swap_num))
	run_cmd("git push")
	run_cmd("git checkout -B room_" + str((swap_num + player_id) % 2))
	swap_num += 1

while True:
	time.sleep(random.uniform(swap_min, swap_max))
	for i in range(1,4):
		print(str(i) + "s UNTIL SWAP")
		run_cmd("beep")
		time.sleep(1)
	swap()






