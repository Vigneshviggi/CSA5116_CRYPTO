# EXP-29: SHA-3 State Lanes and Capacity Calculation
# The question says to ignore the permutation and track the original
# zero capacity lanes, even after they would have changed position.

state_size = 1600
block_size = 1024
lane_size = 64

capacity = state_size - block_size
rate_lanes = block_size // lane_size
capacity_lanes = capacity // lane_size

print("SHA-3 state size:", state_size, "bits")
print("Block (rate) size:", block_size, "bits")
print("Capacity:", capacity, "bits")
print("Rate lanes:", rate_lanes)
print("Capacity lanes:", capacity_lanes)

print("\\nInitially, all", capacity_lanes, "capacity lanes are zero.")
print("The message block is XORed into the rate portion only.")
print("Therefore, with the permutation ignored, the capacity lanes")
print("remain zero forever. They never become nonzero.")
