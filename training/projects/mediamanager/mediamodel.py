#!/usr/bin/env python 
# -*- coding: utf-8 -*-


class TvShow:
    """
    Représente une série et permet de gérer les saisons associées ainsi que les informations
    générales de la série.
    """
    def __init__(self, name):
        self.name = name
        self._seasons = []

    def _add_season(self, season):
        """
        On ne gère pas de saison directement, cette méthode est donc privée. Il est préférable de
        passer par cette méthode qui s'assure le tri.

        :param season:
        :return: None
        """
        if season not in self:
            self._seasons.append(season)
            self._sort()
        else:
            raise ValueError('Season exists')

    def add_episode(self, episode, season_number):
        for season in self._seasons:
            if season.number == season_number:
                season.add(episode)
                break
        else:
            season = Season(season_number)
            season.add(episode)
            self._add_season(season)

    @property
    def seasons(self):
        """return a copy of this object's seasons list"""
        return list(self._seasons)

    def _sort(self):
        """
        Tri les saisons par ordre *naturel* (numéro de saison).

        La méthode est privée car la collection en elle même est privée et de ce fait, le tri de la
        liste appatient à l'objet.
        :return: None
        """
        self._seasons.sort(key=lambda x: x.number)

    def __len__(self):
        return len(self._seasons)

    def __contains__(self, item):
        """
        Un TvShow peut être considéré comme un conteneur de saisons. Cette méthode permet donc
        d'interroger un TvShow à la manière `saison in show`

        :param item:
        :return:
        """
        if hasattr(item, "number"):
            cmp_value = item.number
        else:
            cmp_value = item

        for element in self._seasons:
            if element.number == cmp_value:
                return True

        return False

    def __str__(self):
        return "{} <{}>".format(self.name, len(self._seasons))


class Season:
    """
    Définit une saison caractérisée par son *numéro* et la liste des épisodes.
    """
    def __init__(self, number):
        self.number = int(number)
        self._episodes = []

    def add(self, episode):
        if episode not in self:
            self._episodes.append(episode)
            self.sort()
        else:
            raise ValueError("Episode exists")

    def episode(self, number):
        """
        Retourne un épisode en fonction de son numéro. Une exception est levée si aucun épisode ne correspond.

        :param number: Numéro de l'épisode.
        :return: Un épisode si la saison contient un épisode avec ce numéro ou None.
        :raises ValueError: If there is no episode with the given number.
        """
        for element in self._episodes:
            if element.number == int(number):
                return element

        raise ValueError('Episode {} does not exist'.format(number))

    @property
    def episodes(self):
        """
        Cet *accesseur* retourne une copie de la liste des épisodes, évitant ainsi une modification accidentelle.
        :return: La liste des épisodes
        """
        return list(self._episodes)

    def sort(self):
        self._episodes.sort(key=lambda x: x.number)

    def __lt__(self, other):
        return self.number < other.number

    def __len__(self):
        return len(self._episodes)

    def __contains__(self, item):
        """
        Fonction *avancée* permétant d'interroger un objet Season pour savoir il possède un objet de
        type Episode avec l'instruction *episode in season*
        
        :param item: un objet de type Episode ou du moins qui contient un attribut *number* 
        :return: vrai si un élément de la collection contient un attribut *number* égal à l'attribut
        *number* de l'objet.
        """
        for element in self._episodes:
            if element.number == item.number:
                return True

        return False

    def __iter__(self):
        """
        Fonction *avancée*, permet de retourner un itérateur sous la forme d'un générateur qui sera
        utilisé pour la fonction for et permet de d'itérer sur les épisodes.

        :return: un générateur sur les épisodes
        """
        for episode in self._episodes:
            yield episode

    def __str__(self):
        return "Season {} <{}>".format(self.number, len(self._episodes))


class Episode:
    """
    Définit un épisode qui est un objet de type média.

    Le titre et le numéro sont considérés comme pouvant être modifés.
    """
    def __init__(self, title, number, duration=0):
        self.number = int(number)
        self.title = title
        self._duration = int(duration)

    @property
    def duration(self):
        """Duration of the episode."""
        if self._duration == 0:
            raise ValueError("Duration not set")
        else:
            return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = int(value)

    @duration.deleter
    def duration(self):
        self._duration = 0

    def __str__(self):
        return "ep.{} - {}".format(self.number, self.title)


if __name__ == '__main__':
    pass
