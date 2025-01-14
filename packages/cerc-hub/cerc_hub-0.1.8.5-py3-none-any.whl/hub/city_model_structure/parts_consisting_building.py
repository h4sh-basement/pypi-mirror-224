"""
PartsConsistingBuilding module
SPDX - License - Identifier: LGPL - 3.0 - or -later
Copyright © 2022 Concordia CERC group
Project Coder Pilar Monsalvete Alvarez de Uribarri pilar.monsalvete@concordia.ca
"""

from typing import List, TypeVar
from hub.city_model_structure.city_objects_cluster import CityObjectsCluster
CityObject = TypeVar('CityObject')


class PartsConsistingBuilding(CityObjectsCluster):
  """
  PartsConsistingBuilding(CityObjectsCluster) class
  """
  def __init__(self, name, city_objects):
    self._cluster_type = 'building_parts'
    super().__init__(name, self._cluster_type, city_objects)
    self._name = name
    self._city_objects = city_objects

  @property
  def type(self):
    """
    Get type of cluster
    :return: str
    """
    return self._cluster_type

  @property
  def city_objects(self) -> List[CityObject]:
    """
    Get city objects that compose the cluster
    :return: [CityObject]
    """
    return self._city_objects
