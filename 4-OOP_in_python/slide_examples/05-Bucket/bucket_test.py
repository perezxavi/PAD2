"""
Program that tests the WaterCube class.

Date: 16/09/2023.
"""
from bucket import Bucket

small_bucket = Bucket(2)
big_bucket = Bucket(7, 1)

print(f"Small bucket:\n{small_bucket}\n")
print(f"Big bucket:\n{big_bucket}\n")

print("Filling the small bucket:")
small_bucket.fill()
print(small_bucket)

print(f"\nThe big bucket is nearly empty:\n{big_bucket}\n")
print("Now I'll pour what's in the small bucket into the big bucket.\n")
small_bucket.dump_in(big_bucket)
print(f"Small bucket:\n{small_bucket}\n")
print(f"Big bucket:\n{big_bucket}\n")

print("Now I'll pour what's in the big bucket into the small bucket.\n")
big_bucket.dump_in(small_bucket)
print(f"Small bucket:\n{small_bucket}\n")
print(f"Big bucket:\n{big_bucket}")
