GROWTH_COEFFICIENT = 45

tree = lambda species, height, width, vitality: (species, height, width, vitality)

isLeafy = lambda tree: tree[1] > 6 and tree[1] < 15 and tree[2] > tree[1] and tree[3] > 1

lifeExpectancy = lambda tree: tree[3] * GROWTH_COEFFICIENT / 2

rain = lambda mm, tree: (tree[0], tree[1] + 1, tree[2], tree[3] + (tree[3] * mm / 100))

hail = lambda tree: (tree[0], tree[1] - 2, tree[3], tree[4]) if tree[1] >= 3 else tree

storm = lambda tree: hail(rain(100, tree))

isDayGood = lambda tree: rain(150, tree)[3] > 5

newBaobab = tree("baobab", 5, 10, 1.7)