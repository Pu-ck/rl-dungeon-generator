# rl-dungeon-generator
Roguelike random dungeon generator

Random roguelike dungeon generator made from scratch and visualised with tcod library. Generates a set of randomized rooms, separated or connected with each other, and fills the map with tiles (.) and decorative objects like grass ("), columns (I), rocks (o) or water (≈). The number and postition of doors (═, ║) in each rooms is random and they are not interactable, only filling the hole between walls. Contains a simple movement and player-walls collision for visualisation purpose, as well as the option to generate a new dungeon by stepping on a stairs/exit object (↓).

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<img src = example.png width=600>
