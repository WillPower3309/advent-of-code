import networkx # graph library
from itertools import combinations

networkGraph = networkx.Graph()
with open('input/day23.txt', 'r') as f:
    networkGraph = networkx.Graph()
    for line in f:
        nodes = line.strip().split('-')
        networkGraph.add_edge(nodes[0], nodes[1])

subNetworksContainingT = set()
for clique in networkx.find_cliques(networkGraph):
    for combination in combinations(clique, 3):
        if any(node[0] == "t" for node in combination):
            subNetworksContainingT.add(tuple(sorted(combination)))

print('PART ONE: %d' % len(subNetworksContainingT))

biggestClique = []
for clique in networkx.find_cliques(networkGraph):
    if len(clique) > len(biggestClique):
        biggestClique = clique

print('PART TWO:', ','.join(map(str, sorted(biggestClique))))

