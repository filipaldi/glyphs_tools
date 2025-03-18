# post_close_open_paths.py
import math

def distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

def close_open_paths(font):
    for glyph in font.glyphs:
        for layer in glyph.layers:
            startNodes = list()
            for path in layer.paths:
                if path.closed:
                    continue
                startNodes.append(path.startNode())
                startNodes.append(path.endNode())
            if len(startNodes) < 2:
                continue
            while len(startNodes) > 1:
                node1 = startNodes[0]
                node2 = startNodes[1]
                dist = distance(node1.position, node2.position)
                for i in range(2, len(startNodes), 1):
                    otherNode = startNodes[i]
                    otherDist = distance(node1.position, otherNode.position)
                    if otherDist < dist:
                        node2 = otherNode
                        dist = otherDist
                layer.connectPathsWithNode_andNode_(node1, node2)
                startNodes.remove(node1)
                startNodes.remove(node2)
