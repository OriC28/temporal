
graph_test = [
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]
def are_adjacent(node1, node2, graph_test):
	result: bool
	result = True if graph_test[node1][node2] and graph_test[node2][node1] == 1 else False
	return result

print(are_adjacent(0,2, graph_test))


