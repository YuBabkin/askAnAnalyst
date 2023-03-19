#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 23:37:45 2022

@author: babkin
"""

import random


def analysts_answer():
    """ Спроси аналитика
    """

    list_of_answers = ["Да мне похуй что ты там наговнокодил!",
                       "Да мне по барабану!",
                       "Сам разбирася со своим говном.",
                       "А я ебу, что за хуйню ты тут высрал",
                       "Ну и с какого комита така ебала завелась?!",
                       "И чё, бля?"]

    a = random.randint(0, len(list_of_answers))

    print(list_of_answers[a])


