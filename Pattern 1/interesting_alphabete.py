n = int(input())
if __name__ == '__main__':

	for i in range(n, 0, -1):
		for j in range(i, n + 1, 1):
			print(chr(ord('A') + j - 1),
							end = "");

		print("");

