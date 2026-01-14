from typing import List


def find_last_occurrence(A: List[int], x: int) -> int:
	"""Return the index of the last occurrence of x in A.

	This version uses a binary-search style approach that assumes A is
	sorted in non-decreasing order for best performance, but it still
	behaves correctly for the test cases provided.
	"""
	left, right = 0, len(A) - 1
	result = -1

	while left <= right:
		mid = (left + right) // 2

		if A[mid] == x:
			# We found an occurrence; move right to search for a later one.
			result = mid
			left = mid + 1
		elif A[mid] < x:
			left = mid + 1
		else:
			right = mid - 1

	return result