from math import log

def convert_even_to_odd(num):
	"""Converts even number to odd number by dividing by 2.
	First step:
		Finding number of bits to shift to make it odd number.
		Logic to calculate number of bits to shift is
		number bit-wise AND operation with 2's complement of same number
		and taking log of result with base 2.
	Second step:
		Bit-wise right shift operation with the number of bits to shift.
	"""
	bits_to_shift = log(num & (~num + 1), 2)
	if bits_to_shift == 0:
		return num
	return num >> int(bits_to_shift)

array = [100, 132, 113, 874, 109375, 1093752, 565656747848938,
1465965158748588, 777874988455151878784841846622, 222222222222222222228888888888888444444444]


print([convert_even_to_odd(i) for i in array])
