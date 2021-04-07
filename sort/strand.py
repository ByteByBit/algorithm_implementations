def merge_list(a: list, b: list) -> list:
	out = []
	while len(a) and len(b):
		if a[0] < b[0]:
			out.append(a.pop(0))
		else:
			out.append(b.pop(0))
	out += a
	out += b
	return out
 
def strand(a: list) -> list:
	i, s = 0, [a.pop(0)]
	while i < len(a):
		if a[i] > s[-1]:
			s.append(a.pop(i))
		else:
			i += 1
	return s
 
def strand_sort(a: list) -> list:
    """ 
    Strand sort algorithm.
    
    Parameters
    ----------
    a : list
        Set of numbers to search in.

    Returns
    -------
    list
        The sorted list.

    """

    # Sublist.
	out = strand(a)

	while len(a):
		out = merge_list(out, strand(a))
	return out