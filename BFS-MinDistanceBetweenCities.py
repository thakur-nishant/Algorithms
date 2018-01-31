import sys
class BFS:
    distance = {}
    parent = {}
    map = {}
    queue = []
    def findMinDistance(self, data, source, destination):

        visited = []
        self.initCities(data, source)

        self.queue.append(source)

        while self.queue:
            current = self.queue.pop(0)
            visited.append(current)
            try:
                for i in self.map[current].keys():
                    if i not in visited:
                        self.queue.append(i)
                    curDist = self.distance[current] + self.map[current][i]
                    if self.distance[i] > curDist:
                        self.distance[i] = curDist
                        self.parent[i] = current
            except KeyError:
                x = 1
                # print(current, ":no outgoing city")

        s2d = self.distance[destination]
        path = []
        while destination != source:
            path.insert(0, destination)
            destination = self.parent[destination]
        path.insert(0, source)

        return path,s2d


    def initCities(self, data, source):
        scity = []
        dcity = []
        path_dist = []
        for line in data.splitlines():
            path = line.split()
            scity.append(path[0])
            dcity.append(path[1])
            path_dist.append(path[2])

        for i in range(len(scity)):
            if scity[i] in self.map:
                self.map[scity[i]].update({ dcity[i] : int(path_dist[i]) })
            else:
                self.map[scity[i]] = { dcity[i] : int(path_dist[i]) }

        city_list = set(scity + dcity)
        for i in city_list:
            self.parent[i] = None
            self.distance[i] = sys.maxsize

        self.distance[source] = 0



test = BFS()

data = """Luebeck Hamburg 63
Hamburg Bremen 116
Hamburg Hannover 153
Hamburg Berlin 291
Bremen Hannover 132
Bremen Dortmund 234
Hannover Magdeburg 148
Hannover Kassel 165
Magdeburg Berlin 166
Berlin Dresden 204
Dresden Leipzig 119
Leipzig Magdeburg 125
Dortmund Duesseldorf 69
Kassel Frankfurt 185
Frankfurt Dortmund 221
Frankfurt Nuremberg 222
Leipzig Nuremberg 263
Dortmund Saarbruecken 350
Saarbruecken Frankfurt 177
Saarbruecken Karlsruhe 143
Karlsruhe Stuttgart 71
Stuttgart Frankfurt 200
Stuttgart Munich 215
Stuttgart Nuremberg 207
Nuremberg Munich 171
Manchester Birmingham 84
Birmingham Bristol 85
Birmingham London 117
"""

x,y = test.findMinDistance(data, 'Luebeck', 'Munich')

print("Follow following path for shortest distance:", x)
print("Total distance to travel:", y)