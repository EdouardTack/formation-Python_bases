#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crée une fenêtre permétant de gérer des épisodes d'une série télévisée. Les widgets sont dans un
module dédié. Les épisodes sont gérés sous forme d'une collection dans une liste dans ce module.

"""

from tkinter import Tk, Button, Frame, LEFT, RIGHT, BOTTOM

from training.projects.mediamanager import mediamodel
from training.projects.mediamanager import media_widgets

fenetre = Tk()

episode_list = []


def add_episode(title, number):
    """
    Ajoute un épisode à la collection gérée. Ajoute également cet épisode au
    composant `episode_frame`.

    :param title: Titre de l'épisode à ajouter
    :param number: Numéro de l'épisode à ajouter
    """

    episode = mediamodel.Episode(title, number)
    episode_list.append(episode)
    episode_list.sort(key=lambda x: x.number)
    ep_index = episode_list.index(episode)

    episodes_frame.add_element(title, ep_index)


def select_episode(ep_index):
    """
    Communique les informations d'un épisode à la `form_frame`.

    :param ep_index: indice d'un épisode dans la collection.
    """
    form_frame.set_values(episode_list[ep_index].title, episode_list[ep_index].number)


def delete_episode(ep_index):
    """
    Supprime un épisode de la liste des épisodes.

    :param ep_index: indice de l'épisode à supprimer.
    """
    episode_list.pop(ep_index)

fenetre.title('Episode Manager')

buttons_frame = Frame(fenetre)
Button(buttons_frame, text='Quit', command=fenetre.quit).pack(side=RIGHT)
buttons_frame.pack(side=BOTTOM)

form_frame = media_widgets.EpisodeEntry(fenetre, add_episode, "Titre", "N°")
episodes_frame = media_widgets.CollectionFrame(fenetre, select_callback=select_episode,
                                               delete_callback=delete_episode)
episodes_frame.pack(side=LEFT)
form_frame.pack()

fenetre.mainloop()