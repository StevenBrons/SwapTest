import time
import random
import subprocess
import os

# sudo modprobe pcspkr
# sudo apt install beep

SWAP_NUM = 1
WARNING = 3

swap_min = int(input("Enter minimum swap-time (seconds): "))
swap_max = int(input("Enter maximum swap-time (seconds): "))
seed = input("Enter a random word: ")
random.seed(seed) 
num_players = int(input("Enter the number of players: "))
player_id = int(input("Enter your player id (0-" + str(num_players - 1) + "): "))
input("Press enter at the same time: ")


def run_cmd(cmd):
	sp = subprocess.run(cmd.split())

def init():
	for i in range(0,num_players):
		run_cmd("git checkout -B room_" + str(i))
		run_cmd("git push --set-upstream origin room_" + str(i))
	run_cmd("git checkout -B room_" + str(player_id))

init()

def swap(swap_num):
	print("SWAP #" + str(swap_num) + " is occuring!")
	run_cmd("git add -A")
	run_cmd("git commit -m \"swap_\"" + str(swap_num))
	run_cmd("git push")
	run_cmd("git checkout room_" + str((swap_num + player_id) % num_players))
	input("Press enter to pull")
	run_cmd("git pull")


while True:
	run_cmd("beep")
	time.sleep(0.1)
	run_cmd("beep")
	time.sleep(random.uniform(swap_min, swap_max))
	for i in range(1,WARNING + 1):
		print(str(WARNING - i) + "s UNTIL SWAP")
		run_cmd("beep")
		time.sleep(1)
	swap(SWAP_NUM)
	SWAP_NUM += 1






