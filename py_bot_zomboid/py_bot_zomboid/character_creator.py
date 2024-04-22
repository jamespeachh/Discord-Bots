import random

def character_creator():
    point_counter = 0
    positives = random.randint(5, 10)
    negatives = random.randint(3, 8)
    profession = random_from_json("professions")
    point_counter = point_counter + int(zomboid["professions"][profession])

    neg_final = negative_finder(negatives, point_counter)
    point_counter = neg_final[0]
    pos_final = positive_finder(positives, point_counter)
    point_counter = pos_final[0]
    return [[neg_final[1]],[pos_final[1]],profession]

def negative_finder(negatives, point_counter):
    original_pc = point_counter
    negative_array = []
    for i in range(negatives):
        item = random_from_json("negatives")

        while(item in negative_array):
            item = random_from_json("negatives")

        negative_array.append(item)
        point_counter = point_counter + int(zomboid["negatives"][item])
    if(point_counter<0):
        negative_finder(negatives, original_pc)
    return [point_counter, negative_array]


def positive_finder(positives, point_counter):
    original_pc = point_counter
    positive_array = []
    for i in range(positives):
        item = random_from_json("positives")
        while(item in positive_array):
            item = random_from_json("positives")
        if((point_counter + int(zomboid["positives"][item])) < 0):
            continue

        positive_array.append(item)
        point_counter = point_counter + int(zomboid["positives"][item])

    if(original_pc>=4 and len(positive_array) == 0):
        positive_finder(positives, original_pc)
    return [point_counter, positive_array]



def random_from_json(structure):
    return random.choice(list(zomboid[structure].keys()))