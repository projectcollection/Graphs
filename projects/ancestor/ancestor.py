from util import Stack

def get_ancestor(fam_tree, child, ancestors, level = 0):
	if len(fam_tree[child]) == 0:
		ancestors.append((level,child))
	else:
		for parent in fam_tree[child]:
			get_ancestor(fam_tree, parent, ancestors, level + 1)

def earliest_ancestor(graph_init, child):
	fam_tree = {}
	#populate fam_tree
	for rel in graph_init:
		if rel[0] not in fam_tree:
			fam_tree[rel[0]] = set()
		if rel[1] not in fam_tree:
			fam_tree[rel[1]] = set()
		fam_tree[rel[1]].add(rel[0])

	if len(fam_tree[child]) == 0:
		return -1
	else:
		ancestors = []
		get_ancestor(fam_tree, child, ancestors)

		earliest = 0
		#get earliest ancestor
		for ancestor in ancestors:
			if ancestor[0] > earliest:
				earliest = ancestor[0]

		return min([ancestor[1] for ancestor in ancestors if ancestor[0] == earliest])