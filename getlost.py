#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 09:38:10 2018

@author: policratus
"""
import sys

import numpy as np
from PIL import Image, ImageDraw
import networkx as nx

def pathfinder():
    """
    Executes the game
    """
    print("Creating universe")
    width, height, depth = 800, 800, 3
    graph = nx.DiGraph()

    universe = np.zeros((width, height, depth), dtype=np.uint8)

    wall_factor = .01
    star = np.array([255, 255, 255], dtype=np.uint8)

    print("My god, it's full of stars!")
    for _ in range(int((width * height) * wall_factor)):
        universe[np.random.randint(width)][np.random.randint(height)] = star

    print("Creating origin planet")
    starting_star_h, starting_star_w = np.random.randint(height), \
        np.random.randint(width)

    print("Creating target planet")
    target_star_h, target_star_w = np.random.randint(height), \
        np.random.randint(width)

    print("Contracting universe for FTL travel")
    reduction = np.mean(universe, axis=-1, dtype=np.int8)

    print("Mapping observable and void universe")
    for node_height, node_width in np.argwhere(reduction != -1):
        graph.add_node(str(node_height) + '|' + str(node_width))

        if node_width + 1 < width:
            if reduction[node_height][node_width + 1] == 0:
                graph.add_edge(str(node_height) + '|' + str(node_width), str(node_height) + '|' + str(node_width + 1))
        if node_height + 1 < height:
            if reduction[node_height + 1][node_width] == 0:
                graph.add_edge(str(node_height) + '|' + str(node_width), str(node_height + 1) + '|' + str(node_width))
        if node_width - 1 > width:
            if reduction[node_height][node_width - 1] == 0:
                graph.add_edge(str(node_height) + '|' + str(node_width), str(node_height) + '|' + str(node_width - 1))
        if node_height - 1 > height:
            if reduction[node_height - 1][node_width] == 0:
                graph.add_edge(str(node_height) + '|' + str(node_width), str(node_height - 1) + '|' + str(node_width))
        if node_height - 1 > height and node_width - 1 > width:
            if reduction[node_height - 1][node_width - 1] == 0:
                graph.add_edge(str(node_height) + '|' + str(node_width), str(node_height - 1) + '|' + str(node_width - 1))
        if node_height + 1 < height and node_width + 1 < width:
            if reduction[node_height + 1][node_width + 1] == 0:
                graph.add_edge(str(node_height) + '|' + str(node_width), str(node_height + 1) + '|' + str(node_width + 1))
        if node_height + 1 < height and node_width - 1 > width:
            if reduction[node_height + 1][node_width - 1] == 0:
                graph.add_edge(str(node_height) + '|' + str(node_width), str(node_height + 1) + '|' + str(node_width - 1))
        if node_height - 1 > height and node_width + 1 < width:
            if reduction[node_height - 1][node_width + 1] == 0:
                graph.add_edge(str(node_height) + '|' + str(node_width), str(node_height - 1) + '|' + str(node_width + 1))

    print(
        "Universe mapped. Found {} traversable spaces and {} paths".format(
            graph.number_of_nodes(),
            graph.number_of_edges()
        )
    )

    try:
        print("Finding best path")
        points = [
            list(map(int, visited.split('|')))
            for visited in nx.algorithms.astar_path(
                graph,
                str(starting_star_h) + '|' + str(starting_star_w),
                str(target_star_h) + '|' + str(target_star_w)
            )
        ]
    except nx.exception.NetworkXNoPath:
        print("The worlds are not on the same space-time grid. Try another parallel reality.")
        sys.exit()

    print("Travelling! FTL speed reached")
    for point in points:
        universe[point[0]][point[1]] = [143, 188, 150]

    print("We achieved target planet. Generating report.")
    universe_picture = Image.fromarray(universe)

    draw = ImageDraw.ImageDraw(universe_picture)

    draw.ellipse(
        (
            starting_star_w - 20,
            starting_star_h - 20,
            starting_star_w,
            starting_star_h
        ),
        fill=(244, 167, 66)
    )

    draw.ellipse(
        (
            target_star_w - 20,
            target_star_h - 20,
            target_star_w,
            target_star_h
        ),
        fill=(66, 86, 244)
    )

    del draw

    universe_picture.save('galaxy.png')
    print("Report generated. Exploration initiated.")


if __name__ == '__main__':
    pathfinder()
