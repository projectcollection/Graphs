from util import Stack

def get_path_to_ancestor(fam_tree, child, ancestors, v = set(), path = [], level = 0):
	v.add(child)
	path.append(child) 

	if len(fam_tree[child]) == 0:
		ancestors.append((level,child))
	else:
		for parent in fam_tree[child]:
			get_path_to_ancestor(fam_tree, parent, ancestors, v, path, level + 1)

def earliest_ancestor(graph_init, child):
	fam_tree = {}
	#populate fam_tree
	for rel in graph_init:
		if rel[0] not in fam_tree:
			fam_tree[rel[0]] = set()
		if rel[1] not in fam_tree:
			fam_tree[rel[1]] = set()
		fam_tree[rel[1]].add(rel[0])

	ancestors = []

	if len(fam_tree[child]) == 0:
		return -1

	get_path_to_ancestor(fam_tree, child, ancestors)
	
	earliest = 0
	for ancestor in ancestors:
		if ancestor[0] > earliest:
			earliest = ancestor[0]

	return min([ancestor[1] for ancestor in ancestors if ancestor[0] == earliest])


