"""
Dictionaries module saves all transformations of functions and usages to access the catalogs
SPDX - License - Identifier: LGPL - 3.0 - or -later
Copyright © 2023 Concordia CERC group
Project Coder Pilar Monsalvete Alvarez de Uribarri pilar.monsalvete@concordia.ca
"""

from hub.helpers.data.hft_function_to_hub_function import HftFunctionToHubFunction
from hub.helpers.data.montreal_custom_fuel_to_hub_fuel import MontrealCustomFuelToHubFuel
from hub.helpers.data.montreal_function_to_hub_function import MontrealFunctionToHubFunction
from hub.helpers.data.eilat_function_to_hub_function import EilatFunctionToHubFunction
from hub.helpers.data.alkis_function_to_hub_function import AlkisFunctionToHubFunction
from hub.helpers.data.pluto_function_to_hub_function import PlutoFunctionToHubFunction
from hub.helpers.data.hub_function_to_nrel_construction_function import HubFunctionToNrelConstructionFunction
from hub.helpers.data.hub_function_to_nrcan_construction_function import HubFunctionToNrcanConstructionFunction
from hub.helpers.data.hub_function_to_eilat_construction_function import HubFunctionToEilatConstructionFunction
from hub.helpers.data.hub_usage_to_comnet_usage import HubUsageToComnetUsage
from hub.helpers.data.hub_usage_to_hft_usage import HubUsageToHftUsage
from hub.helpers.data.hub_usage_to_nrcan_usage import HubUsageToNrcanUsage
from hub.helpers.data.hub_usage_to_eilat_usage import HubUsageToEilatUsage
from hub.helpers.data.montreal_system_to_hub_energy_generation_system import MontrealSystemToHubEnergyGenerationSystem
from hub.helpers.data.montreal_demand_type_to_hub_energy_demand_type import MontrealDemandTypeToHubEnergyDemandType
from hub.helpers.data.hub_function_to_montreal_custom_costs_function import HubFunctionToMontrealCustomCostsFunction


class Dictionaries:
  """
  Dictionaries class
  """

  @property
  def hub_usage_to_hft_usage(self) -> dict:
    """
    Hub usage to HfT usage, transformation dictionary
    :return: dict
    """
    return HubUsageToHftUsage().dictionary

  @property
  def hub_usage_to_comnet_usage(self) -> dict:
    """
    Hub usage to Comnet usage, transformation dictionary
    :return: dict
    """
    return HubUsageToComnetUsage().dictionary

  @property
  def hub_usage_to_nrcan_usage(self) -> dict:
    """
    Get hub usage to NRCAN usage, transformation dictionary
    :return: dict
    """
    return HubUsageToNrcanUsage().dictionary

  @property
  def hub_usage_to_eilat_usage(self) -> dict:
    """
    Hub usage to Eilat usage, transformation dictionary
    :return: dict
    """
    return HubUsageToEilatUsage().dictionary

  @property
  def hub_function_to_nrcan_construction_function(self) -> dict:
    """
    Get hub function to NRCAN construction function, transformation dictionary
    :return: dict
    """
    return HubFunctionToNrcanConstructionFunction().dictionary

  @property
  def hub_function_to_eilat_construction_function(self) -> dict:
    """
    Get hub function to NRCAN construction function, transformation dictionary
    :return: dict
    """
    return HubFunctionToEilatConstructionFunction().dictionary

  @property
  def hub_function_to_nrel_construction_function(self) -> dict:
    """
    Get hub function to NREL construction function, transformation dictionary
    :return: dict
    """
    return HubFunctionToNrelConstructionFunction().dictionary

  @property
  def pluto_function_to_hub_function(self) -> dict:
    """
    Get Pluto function to hub function, transformation dictionary
    :return: dict
    """
    return PlutoFunctionToHubFunction().dictionary

  @property
  def hft_function_to_hub_function(self) -> dict:
    """
    Get Hft function to hub function, transformation dictionary
    :return: dict
    """
    return HftFunctionToHubFunction().dictionary

  @property
  def montreal_function_to_hub_function(self) -> dict:
    """
    Get Montreal function to hub function, transformation dictionary
    """
    return MontrealFunctionToHubFunction().dictionary

  @property
  def alkis_function_to_hub_function(self) -> dict:
    """
    Get Alkis function to hub function, transformation dictionary
    """
    return AlkisFunctionToHubFunction().dictionary

  @property
  def montreal_system_to_hub_energy_generation_system(self):
    """
    Get montreal custom system names to hub energy system names, transformation dictionary
    """
    return MontrealSystemToHubEnergyGenerationSystem().dictionary

  @property
  def montreal_demand_type_to_hub_energy_demand_type(self):
    """
    Get montreal custom system demand type to hub energy demand type, transformation dictionary
    """
    return MontrealDemandTypeToHubEnergyDemandType().dictionary

  @property
  def hub_function_to_montreal_custom_costs_function(self) -> dict:
    """
    Get hub function to Montreal custom costs function, transformation dictionary
    :return: dict
    """
    return HubFunctionToMontrealCustomCostsFunction().dictionary

  @property
  def eilat_function_to_hub_function(self) -> dict:
    """
    Get Eilat's function to hub function, transformation dictionary
    """
    return EilatFunctionToHubFunction().dictionary

  @property
  def montreal_custom_fuel_to_hub_fuel(self) -> dict:
    """
    Get hub fuel from montreal_custom catalog fuel
    """
    return MontrealCustomFuelToHubFuel().dictionary
