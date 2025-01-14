"""
City Object repository with database CRUD operations
SPDX - License - Identifier: LGPL - 3.0 - or -later
Copyright © 2022 Concordia CERC group
Project Coder Guille Gutierrez Guillermo.GutierrezMorote@concordia.ca
"""
import datetime
import logging

from sqlalchemy import select, or_
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from hub.city_model_structure.building import Building
from hub.persistence.repository import Repository
from hub.persistence.models import CityObject as Model


class CityObject(Repository):
  """
  City object repository
  """
  _instance = None

  def __init__(self, db_name: str, dotenv_path: str, app_env: str):
    super().__init__(db_name, dotenv_path, app_env)

  def __new__(cls, db_name, dotenv_path, app_env):
    """
    Implemented for a singleton pattern
    """
    if cls._instance is None:
      cls._instance = super(CityObject, cls).__new__(cls)
    return cls._instance

  def insert(self, city_id: int, building: Building):
    """
    Inserts a new city object
    :param city_id: city id for the city owning this city object
    :param building: the city object (only building for now) to be inserted
    return Identity id
    """
    city_object = self.get_by_name_or_alias_and_city(building.name, city_id)
    if city_object is not None:
      raise SQLAlchemyError(f'A city_object named {building.name} already exists in that city')
    try:
      city_object = Model(city_id=city_id,
                          building=building)
      self.session.add(city_object)
      self.session.flush()
      self.session.commit()
      self.session.refresh(city_object)
      return city_object.id
    except SQLAlchemyError as err:
      logging.error('An error occurred while creating city_object %s', err)
      raise SQLAlchemyError from err

  def update(self, city_id: int, building: Building):
    """
    Updates an application
    :param city_id: the city id of the city owning the city object
    :param building: the city object
    :return: None
    """
    try:
      object_usage = ''
      for internal_zone in building.internal_zones:
        for usage in internal_zone.usages:
          object_usage = f'{object_usage}{usage.name}_{usage.percentage} '
      object_usage = object_usage.rstrip()
      self.session.query(Model).filter(Model.name == building.name, Model.city_id == city_id).update(
        {'name': building.name,
         'alias': building.alias,
         'object_type': building.type,
         'year_of_construction': building.year_of_construction,
         'function': building.function,
         'usage': object_usage,
         'volume': building.volume,
         'area': building.floor_area,
         'updated': datetime.datetime.utcnow()})
      self.session.commit()
    except SQLAlchemyError as err:
      logging.error('Error while updating city object %s', err)
      raise SQLAlchemyError from err

  def delete(self, city_id: int, name: str):
    """
    Deletes an application with the application_uuid
    :param city_id: The id for the city owning the city object
    :param name: The city object name
    :return: None
    """
    try:
      self.session.query(Model).filter(Model.city_id == city_id, Model.name == name).delete()
      self.session.commit()
    except SQLAlchemyError as err:
      logging.error('Error while deleting application %s', err)
      raise SQLAlchemyError from err

  def get_by_name_or_alias_and_city(self, name, city_id) -> Model:
    """
    Fetch a city object based on name and city id
    :param name: city object name
    :param city_id: a city identifier
    :return: [CityObject] with the provided name or alias belonging to the city with id city_id
    """
    try:
      # search by name first
      city_object = self.session.execute(select(Model).where(Model.name == name, Model.city_id == city_id)).first()
      if city_object is not None:
        return city_object[0]
      # name not found, so search by alias instead
      city_objects = self.session.execute(
        select(Model).where(Model.aliases.contains(name), Model.city_id == city_id)
      ).all()
      self.session.close()
      self.session = Session(self.engine)
      for city_object in city_objects:
        aliases = city_object[0].aliases.replace('{', '').replace('}', '').split(',')
        for alias in aliases:
          if alias == name:
            # force the name as the alias
            city_object[0].name = name
            return city_object[0]
      return None
    except SQLAlchemyError as err:
      logging.error('Error while fetching city object by name and city: %s', err)
      raise SQLAlchemyError from err
    except IndexError as err:
      logging.error('Error while fetching city object by name and city, empty result %s', err)
      raise IndexError from err
