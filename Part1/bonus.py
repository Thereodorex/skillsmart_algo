from LinkedList import LinkedList

def sum_lists(first, second):
		res = LinkedList()
		ptr1 = first.head
		ptr2 = second.head
		if first.len() == second.len():
			while ptr1 is not None:
				res.add_in_tail(ptr1.value + ptr2.value)
				ptr1 = ptr1.next
				ptr2 = ptr2.next
		return res