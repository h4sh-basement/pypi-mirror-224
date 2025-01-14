"""
Dictionaries module for Montreal function to hub function
SPDX - License - Identifier: LGPL - 3.0 - or -later
Copyright © 2022 Concordia CERC group
Project Coder Guille Gutierrez Guillermo.GutierrezMorote@concordia.ca
"""

import hub.helpers.constants as cte


class MontrealFunctionToHubFunction:
  """
  Montreal function to hub function class
  """

  def __init__(self):
    self._dictionary = {'1000': cte.RESIDENTIAL,
                        '2089': cte.INDUSTRY,
                        '1921': cte.WAREHOUSE,
                        '1922': cte.NON_HEATED,
                        '9100': cte.NON_HEATED,
                        '6000': cte.MEDIUM_OFFICE,
                        '5010': cte.STAND_ALONE_RETAIL,
                        '9490': cte.WAREHOUSE,
                        '4299': cte.WAREHOUSE,
                        '6379': cte.WAREHOUSE,
                        '5533': cte.WAREHOUSE,
                        '6591': cte.OFFICE_AND_ADMINISTRATION,
                        '6211': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '1511': cte.DORMITORY,
                        '5833': cte.HOTEL,
                        '1532': cte.DORMITORY,
                        '6911': cte.CONVENTION_CENTER,
                        '9510': cte.RESIDENTIAL,
                        '1990': cte.MID_RISE_APARTMENT,
                        '1923': cte.NON_HEATED,
                        '7222': cte.SPORTS_LOCATION,
                        '5002': cte.STRIP_MALL,
                        '6111': cte.COMMERCIAL,
                        '6311': cte.MEDIUM_OFFICE,
                        '6399': cte.MEDIUM_OFFICE,
                        '5812': cte.FULL_SERVICE_RESTAURANT,
                        '4621': cte.WAREHOUSE,
                        '1541': cte.DORMITORY,
                        '7214': cte.EVENT_LOCATION,
                        '4821': cte.NON_HEATED,
                        '9520': cte.NON_HEATED,
                        '7112': cte.EVENT_LOCATION,
                        '6299': cte.OUT_PATIENT_HEALTH_CARE,
                        '5461': cte.RETAIL_SHOP_WITH_REFRIGERATED_FOOD,
                        '4632': cte.NON_HEATED,
                        '7424': cte.EVENT_LOCATION,
                        '5811': cte.FULL_SERVICE_RESTAURANT,
                        '4113': cte.WAREHOUSE,
                        '6821': cte.SECONDARY_SCHOOL,
                        '6920': cte.OFFICE_AND_ADMINISTRATION,
                        '6199': cte.COMMERCIAL,
                        '5899': cte.WAREHOUSE,
                        '5999': cte.STAND_ALONE_RETAIL,
                        '5834': cte.RESIDENTIAL,
                        '2699': cte.INDUSTRY,
                        '6812': cte.SECONDARY_SCHOOL,
                        '6649': cte.WAREHOUSE,
                        '3999': cte.INDUSTRY,
                        '1553': cte.OFFICE_AND_ADMINISTRATION,
                        '6999': cte.WAREHOUSE,
                        '6541': cte.PRIMARY_SCHOOL,
                        '5831': cte.SMALL_HOTEL,
                        '6919': cte.OFFICE_AND_ADMINISTRATION,
                        '9900': cte.WAREHOUSE,
                        '1551': cte.EVENT_LOCATION,
                        '5511': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6231': cte.COMMERCIAL,
                        '6221': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6599': cte.OFFICE_AND_ADMINISTRATION,
                        '7119': cte.EVENT_LOCATION,
                        '6214': cte.COMMERCIAL,
                        '5412': cte.RETAIL_SHOP_WITH_REFRIGERATED_FOOD,
                        '4839': cte.WAREHOUSE,
                        '6994': cte.COMMERCIAL,
                        '6344': cte.WAREHOUSE,
                        '6722': cte.WAREHOUSE,
                        '5111': cte.WAREHOUSE,
                        '6511': cte.OUT_PATIENT_HEALTH_CARE,
                        '5965': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '4631': cte.WAREHOUSE,
                        '7451': cte.SPORTS_LOCATION,
                        '1539': cte.DORMITORY,
                        '6376': cte.WAREHOUSE,
                        '4633': cte.NON_HEATED,
                        '5813': cte.QUICK_SERVICE_RESTAURANT,
                        '6339': cte.COMMERCIAL,
                        '5911': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5651': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5971': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '4550': cte.NON_HEATED,
                        '5620': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '7611': cte.NON_HEATED,
                        '5531': cte.WAREHOUSE,
                        '6629': cte.WAREHOUSE,
                        '6521': cte.MEDIUM_OFFICE,
                        '7639': cte.WAREHOUSE,
                        '3399': cte.INDUSTRY,
                        '3019': cte.WAREHOUSE,
                        '6551': cte.MEDIUM_OFFICE,
                        '5413': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5821': cte.QUICK_SERVICE_RESTAURANT,
                        '6411': cte.WAREHOUSE,
                        '6799': cte.OFFICE_AND_ADMINISTRATION,
                        '5942': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '7111': cte.OFFICE_AND_ADMINISTRATION,
                        '6419': cte.WAREHOUSE,
                        '6534': cte.COMMERCIAL,
                        '5020': cte.WAREHOUSE,
                        '6594': cte.MEDIUM_OFFICE,
                        '5819': cte.STAND_ALONE_RETAIL,
                        '6823': cte.SECONDARY_SCHOOL,
                        '4990': cte.WAREHOUSE,
                        '6759': cte.WAREHOUSE,
                        '6517': cte.OUT_PATIENT_HEALTH_CARE,
                        '6839': cte.SECONDARY_SCHOOL,
                        '4711': cte.MEDIUM_OFFICE,
                        '4111': cte.WAREHOUSE,
                        '3280': cte.WAREHOUSE,
                        '6721': cte.OFFICE_AND_ADMINISTRATION,
                        '9459': cte.NON_HEATED,
                        '7113': cte.EVENT_LOCATION,
                        '4743': cte.MEDIUM_OFFICE,
                        '7211': cte.EVENT_LOCATION,
                        '6513': cte.HOSPITAL,
                        '6813': cte.SECONDARY_SCHOOL,
                        '5921': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6383': cte.COMMERCIAL,
                        '5711': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6512': cte.OUT_PATIENT_HEALTH_CARE,
                        '1590': cte.OFFICE_AND_ADMINISTRATION,
                        '1890': cte.DORMITORY,
                        '6372': cte.WAREHOUSE,
                        '1600': cte.SMALL_HOTEL,
                        '9451': cte.NON_HEATED,
                        '6359': cte.WAREHOUSE,
                        '2240': cte.INDUSTRY,
                        '1559': cte.OFFICE_AND_ADMINISTRATION,
                        '1543': cte.DORMITORY,
                        '6760': cte.MEDIUM_OFFICE,
                        '4771': cte.MOTION_PICTURE_THEATRE,
                        '1552': cte.DORMITORY,
                        '3994': cte.INDUSTRY,
                        '6243': cte.NON_HEATED,
                        '6835': cte.SECONDARY_SCHOOL,
                        '5004': cte.STRIP_MALL,
                        '6791': cte.OFFICE_AND_ADMINISTRATION,
                        '1510': cte.DORMITORY,
                        '7239': cte.OFFICE_AND_ADMINISTRATION,
                        '5492': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5499': cte.STAND_ALONE_RETAIL,
                        '4413': cte.WAREHOUSE,
                        '5951': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5411': cte.RETAIL_SHOP_WITH_REFRIGERATED_FOOD,
                        '5532': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5252': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6395': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5462': cte.RETAIL_SHOP_WITH_REFRIGERATED_FOOD,
                        '6232': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6641': cte.WAREHOUSE,
                        '7432': cte.SPORTS_LOCATION,
                        '5431': cte.RETAIL_SHOP_WITH_REFRIGERATED_FOOD,
                        '6532': cte.OFFICE_AND_ADMINISTRATION,
                        '6518': cte.OUT_PATIENT_HEALTH_CARE,
                        '5199': cte.WAREHOUSE,
                        '3840': cte.INDUSTRY,
                        '2051': cte.MEDIUM_OFFICE,
                        '7290': cte.OFFICE_AND_ADMINISTRATION,
                        '5253': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5660': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5699': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6579': cte.OUT_PATIENT_HEALTH_CARE,
                        '5173': cte.WAREHOUSE,
                        '6431': cte.WAREHOUSE,
                        '6355': cte.WAREHOUSE,
                        '6263': cte.OUT_PATIENT_HEALTH_CARE,
                        '5610': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5969': cte.RETAIL_SHOP_WITH_REFRIGERATED_FOOD,
                        '5991': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '7219': cte.OFFICE_AND_ADMINISTRATION,
                        '7117': cte.WAREHOUSE,
                        '5005': cte.STAND_ALONE_RETAIL,
                        '4561': cte.NON_HEATED,
                        '5631': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '4623': cte.WAREHOUSE,
                        '4590': cte.WAREHOUSE,
                        '3899': cte.INDUSTRY,
                        '6563': cte.COMMERCIAL,
                        '5399': cte.STAND_ALONE_RETAIL,
                        '6241': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6351': cte.RETAIL_SHOP_WITH_REFRIGERATED_FOOD,
                        '2270': cte.INDUSTRY,
                        '5132': cte.WAREHOUSE,
                        '4221': cte.WAREHOUSE,
                        '6253': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5640': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '3299': cte.INDUSTRY,
                        '6831': cte.SECONDARY_SCHOOL,
                        '2012': cte.INDUSTRY,
                        '3620': cte.INDUSTRY,
                        '6519': cte.OUT_PATIENT_HEALTH_CARE,
                        '2291': cte.INDUSTRY,
                        '5311': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5931': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '4611': cte.WAREHOUSE,
                        '4719': cte.STAND_ALONE_RETAIL,
                        '5693': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '4490': cte.INDUSTRY,
                        '5823': cte.FULL_SERVICE_RESTAURANT,
                        '2045': cte.INDUSTRY,
                        '6542': cte.HOSPITAL,
                        '2014': cte.INDUSTRY,
                        '6375': cte.WAREHOUSE,
                        '2799': cte.INDUSTRY,
                        '6612': cte.WAREHOUSE,
                        '4222': cte.WAREHOUSE,
                        '7191': cte.EVENT_LOCATION,
                        '6352': cte.WAREHOUSE,
                        '5836': cte.COMMERCIAL,
                        '5952': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '1512': cte.DORMITORY,
                        '5948': cte.WAREHOUSE,
                        '3580': cte.INDUSTRY,
                        '5391': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6997': cte.OFFICE_AND_ADMINISTRATION,
                        '6539': cte.OFFICE_AND_ADMINISTRATION,
                        '2899': cte.INDUSTRY,
                        '1100': cte.SINGLE_FAMILY_HOUSE,
                        '6348': cte.WAREHOUSE,
                        '7499': cte.EVENT_LOCATION,
                        '6373': cte.WAREHOUSE,
                        '3539': cte.INDUSTRY,
                        '4922': cte.WAREHOUSE,
                        '6731': cte.OFFICE_AND_ADMINISTRATION,
                        '6132': cte.MEDIUM_OFFICE,
                        '2073': cte.INDUSTRY,
                        '4761': cte.COMMERCIAL,
                        '7312': cte.NON_HEATED,
                        '7425': cte.SPORTS_LOCATION,
                        '6634': cte.INDUSTRY,
                        '6639': cte.WAREHOUSE,
                        '3231': cte.INDUSTRY,
                        '6569': cte.RETAIL_SHOP_WITH_REFRIGERATED_FOOD,
                        '2499': cte.INDUSTRY,
                        '7199': cte.EVENT_LOCATION,
                        '7114': cte.EVENT_LOCATION,
                        '4733': cte.COMMERCIAL,
                        '4112': cte.WAREHOUSE,
                        '7129': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '7620': cte.NON_HEATED,
                        '9390': cte.WAREHOUSE,
                        '1529': cte.OFFICE_AND_ADMINISTRATION,
                        '7417': cte.NON_HEATED,
                        '8221': cte.OUT_PATIENT_HEALTH_CARE,
                        '6598': cte.OUT_PATIENT_HEALTH_CARE,
                        '6515': cte.OUT_PATIENT_HEALTH_CARE,
                        '3719': cte.WAREHOUSE,
                        '2471': cte.INDUSTRY,
                        '7433': cte.NON_HEATED,
                        '6413': cte.WAREHOUSE,
                        '3459': cte.INDUSTRY,
                        '6152': cte.MEDIUM_OFFICE,
                        '2093': cte.INDUSTRY,
                        '3031': cte.INDUSTRY,
                        '5251': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5394': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5141': cte.STRIP_MALL,
                        '7419': cte.SPORTS_LOCATION,
                        '4293': cte.WAREHOUSE,
                        '6834': cte.SECONDARY_SCHOOL,
                        '2092': cte.INDUSTRY,
                        '2072': cte.INDUSTRY,
                        '6712': cte.MEDIUM_OFFICE,
                        '4411': cte.WAREHOUSE,
                        '4562': cte.NON_HEATED,
                        '2096': cte.INDUSTRY,
                        '5997': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '7212': cte.EVENT_LOCATION,
                        '6713': cte.MEDIUM_OFFICE,
                        '9212': cte.NON_HEATED,
                        '6725': cte.OFFICE_AND_ADMINISTRATION,
                        '9410': cte.RESIDENTIAL,
                        '4211': cte.WAREHOUSE,
                        '5230': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6141': cte.MEDIUM_OFFICE,
                        '7512': cte.HEALTH_CARE,
                        '5822': cte.QUICK_SERVICE_RESTAURANT,
                        '5121': cte.STRIP_MALL,
                        '6369': cte.SECONDARY_SCHOOL,
                        '5171': cte.STRIP_MALL,
                        '5003': cte.STRIP_MALL,
                        '3630': cte.INDUSTRY,
                        '5521': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6531': cte.OUT_PATIENT_HEALTH_CARE,
                        '7413': cte.WAREHOUSE,
                        '3239': cte.INDUSTRY,
                        '4715': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6365': cte.UNIVERSITY,
                        '6121': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6611': cte.WAREHOUSE,
                        '3649': cte.INDUSTRY,
                        '2892': cte.INDUSTRY,
                        '6269': cte.OUT_PATIENT_HEALTH_CARE,
                        '2020': cte.INDUSTRY,
                        '6621': cte.WAREHOUSE,
                        '6312': cte.NON_HEATED,
                        '6416': cte.INDUSTRY,
                        '5712': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '2261': cte.INDUSTRY,
                        '2931': cte.INDUSTRY,
                        '3011': cte.INDUSTRY,
                        '6499': cte.STAND_ALONE_RETAIL,
                        '3599': cte.INDUSTRY,
                        '2299': cte.INDUSTRY,
                        '3831': cte.INDUSTRY,
                        '2410': cte.INDUSTRY,
                        '5112': cte.STRIP_MALL,
                        '5941': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6822': cte.SECONDARY_SCHOOL,
                        '6753': cte.WAREHOUSE,
                        '5149': cte.STRIP_MALL,
                        '3190': cte.INDUSTRY,
                        '6414': cte.WAREHOUSE,
                        '6633': cte.WAREHOUSE,
                        '3895': cte.INDUSTRY,
                        '5133': cte.STRIP_MALL,
                        '2082': cte.INDUSTRY,
                        '5512': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '9420': cte.NON_HEATED,
                        '6543': cte.HOSPITAL,
                        '4841': cte.INDUSTRY,
                        '4851': cte.INDUSTRY,
                        '5432': cte.STRIP_MALL,
                        '3711': cte.INDUSTRY,
                        '3460': cte.INDUSTRY,
                        '2087': cte.INDUSTRY,
                        '1522': cte.HALL,
                        '8549': cte.INDUSTRY,
                        '6242': cte.WAREHOUSE,
                        '6412': cte.WAREHOUSE,
                        '6811': cte.SECONDARY_SCHOOL,
                        '6154': cte.WAREHOUSE,
                        '7123': cte.WAREHOUSE,
                        '6993': cte.MEDIUM_OFFICE,
                        '6742': cte.HOSPITAL,
                        '5212': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5211': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '7990': cte.HALL,
                        '3714': cte.INDUSTRY,
                        '6593': cte.SECONDARY_SCHOOL,
                        '5172': cte.STRIP_MALL,
                        '5955': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6635': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '3799': cte.INDUSTRY,
                        '2819': cte.INDUSTRY,
                        '5894': cte.QUICK_SERVICE_RESTAURANT,
                        '9530': cte.NON_HEATED,
                        '3159': cte.INDUSTRY,
                        '3713': cte.WAREHOUSE,
                        '3894': cte.INDUSTRY,
                        '5721': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5169': cte.STRIP_MALL,
                        '5593': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6631': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5731': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '2739': cte.INDUSTRY,
                        '6619': cte.WAREHOUSE,
                        '6815': cte.SECONDARY_SCHOOL,
                        '5320': cte.STRIP_MALL,
                        '3261': cte.INDUSTRY,
                        '6394': cte.WAREHOUSE,
                        '2031': cte.RETAIL_SHOP_WITH_REFRIGERATED_FOOD,
                        '6423': cte.WAREHOUSE,
                        '3162': cte.INDUSTRY,
                        '5814': cte.QUICK_SERVICE_RESTAURANT,
                        '6653': cte.WAREHOUSE,
                        '2213': cte.INDUSTRY,
                        '2046': cte.INDUSTRY,
                        '6251': cte.COMMERCIAL,
                        '3650': cte.INDUSTRY,
                        '4799': cte.NON_HEATED,
                        '5832': cte.SMALL_HOTEL,
                        '4229': cte.WAREHOUSE,
                        '4842': cte.WAREHOUSE,
                        '5163': cte.STRIP_MALL,
                        '5148': cte.STRIP_MALL,
                        '2011': cte.INDUSTRY,
                        '5361': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '2999': cte.INDUSTRY,
                        '6522': cte.MEDIUM_OFFICE,
                        '7121': cte.MUSEUM,
                        '7221': cte.SPORTS_LOCATION,
                        '1549': cte.OFFICE_AND_ADMINISTRATION,
                        '5652': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '3331': cte.INDUSTRY,
                        '6219': cte.WAREHOUSE,
                        '5421': cte.RETAIL_SHOP_WITH_REFRIGERATED_FOOD,
                        '3861': cte.INDUSTRY,
                        '3919': cte.INDUSTRY,
                        '6441': cte.WAREHOUSE,
                        '6648': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '8199': cte.INDUSTRY,
                        '6832': cte.SECONDARY_SCHOOL,
                        '6992': cte.MEDIUM_OFFICE,
                        '1521': cte.EVENT_LOCATION,
                        '6349': cte.WAREHOUSE,
                        '4921': cte.WAREHOUSE,
                        '6498': cte.WAREHOUSE,
                        '6415': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '4122': cte.WAREHOUSE,
                        '4219': cte.WAREHOUSE,
                        '9440': cte.NON_HEATED,
                        '4782': cte.DATACENTER,
                        '2619': cte.INDUSTRY,
                        '7229': cte.SPORTS_LOCATION,
                        '2079': cte.INDUSTRY,
                        '2320': cte.INDUSTRY,
                        '3259': cte.INDUSTRY,
                        '3931': cte.INDUSTRY,
                        '5470': cte.RETAIL_SHOP_WITH_REFRIGERATED_FOOD,
                        '4890': cte.WAREHOUSE,
                        '5599': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '3270': cte.INDUSTRY,
                        '5186': cte.STRIP_MALL,
                        '2043': cte.INDUSTRY,
                        '6733': cte.WAREHOUSE,
                        '4311': cte.EVENT_LOCATION,
                        '3451': cte.INDUSTRY,
                        '2812': cte.INDUSTRY,
                        '2130': cte.INDUSTRY,
                        '7449': cte.WAREHOUSE,
                        '2919': cte.INDUSTRY,
                        '4315': cte.WAREHOUSE,
                        '3569': cte.INDUSTRY,
                        '7399': cte.EVENT_LOCATION,
                        '6160': cte.OFFICE_AND_ADMINISTRATION,
                        '7412': cte.NON_HEATED,
                        '2084': cte.INDUSTRY,
                        '3870': cte.INDUSTRY,
                        '5001': cte.STRIP_MALL,
                        '3411': cte.INDUSTRY,
                        '1702': cte.NON_HEATED,
                        '3243': cte.INDUSTRY,
                        '4926': cte.MEDIUM_OFFICE,
                        '3490': cte.INDUSTRY,
                        '2219': cte.INDUSTRY,
                        '2829': cte.INDUSTRY,
                        '4399': cte.WAREHOUSE,
                        '4319': cte.WAREHOUSE,
                        '2039': cte.INDUSTRY,
                        '8139': cte.GREEN_HOUSE,
                        '5146': cte.STRIP_MALL,
                        '3396': cte.INDUSTRY,
                        '5161': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '2091': cte.INDUSTRY,
                        '3850': cte.INDUSTRY,
                        '5241': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '3049': cte.INDUSTRY,
                        '5181': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '2627': cte.INDUSTRY,
                        '3412': cte.INDUSTRY,
                        '5220': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '3699': cte.INDUSTRY,
                        '4929': cte.WAREHOUSE,
                        '3551': cte.INDUSTRY,
                        '5198': cte.STRIP_MALL,
                        '6646': cte.NON_HEATED,
                        '5189': cte.STRIP_MALL,
                        '5312': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '4214': cte.WAREHOUSE,
                        '3410': cte.INDUSTRY,
                        '4859': cte.WAREHOUSE,
                        '2736': cte.INDUSTRY,
                        '6642': cte.WAREHOUSE,
                        '3921': cte.INDUSTRY,
                        '5815': cte.FULL_SERVICE_RESTAURANT,
                        '6514': cte.OUT_PATIENT_HEALTH_CARE,
                        '8399': cte.WAREHOUSE,
                        '2250': cte.INDUSTRY,
                        '6378': cte.WAREHOUSE,
                        '6343': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '2652': cte.INDUSTRY,
                        '3552': cte.INDUSTRY,
                        '2891': cte.INDUSTRY,
                        '6368': cte.SECONDARY_SCHOOL,
                        '3559': cte.INDUSTRY,
                        '5145': cte.STRIP_MALL,
                        '3244': cte.INDUSTRY,
                        '3292': cte.INDUSTRY,
                        '4510': cte.WAREHOUSE,
                        '7423': cte.SPORTS_LOCATION,
                        '5370': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '4824': cte.WAREHOUSE,
                        '4832': cte.INDUSTRY,
                        '6573': cte.HEALTH_CARE,
                        '6623': cte.NON_HEATED,
                        '5162': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '4612': cte.WAREHOUSE,
                        '2629': cte.INDUSTRY,
                        '3291': cte.INDUSTRY,
                        '3229': cte.INDUSTRY,
                        '5829': cte.STAND_ALONE_RETAIL,
                        '2932': cte.INDUSTRY,
                        '5594': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '2722': cte.INDUSTRY,
                        '2811': cte.INDUSTRY,
                        '2235': cte.INDUSTRY,
                        '5953': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '3170': cte.INDUSTRY,
                        '3662': cte.INDUSTRY,
                        '4879': cte.WAREHOUSE,
                        '2074': cte.INDUSTRY,
                        '7429': cte.SPORTS_LOCATION,
                        '4843': cte.WAREHOUSE,
                        '6335': cte.OFFICE_AND_ADMINISTRATION,
                        '4116': cte.WAREHOUSE,
                        '2622': cte.INDUSTRY,
                        '6112': cte.OFFICE_AND_ADMINISTRATION,
                        '4875': cte.WAREHOUSE,
                        '4792': cte.WAREHOUSE_REFRIGERATED,
                        '6391': cte.UNIVERSITY,
                        '6425': cte.WAREHOUSE,
                        '6212': cte.WAREHOUSE,
                        '5147': cte.STRIP_MALL,
                        '2460': cte.INDUSTRY,
                        '4874': cte.WAREHOUSE,
                        '6743': cte.DORMITORY,
                        '3241': cte.INDUSTRY,
                        '5123': cte.STRIP_MALL,
                        '4833': cte.NON_HEATED,
                        '9470': cte.NON_HEATED,
                        '3932': cte.INDUSTRY,
                        '4292': cte.WAREHOUSE,
                        '6424': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '6139': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '2624': cte.INDUSTRY,
                        '3915': cte.WAREHOUSE,
                        '7233': cte.CONVENTION_CENTER,
                        '5184': cte.STRIP_MALL,
                        '2099': cte.INDUSTRY,
                        '5129': cte.RETAIL_SHOP_WITH_REFRIGERATED_FOOD,
                        '5913': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '5717': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '4712': cte.NON_HEATED,
                        '5142': cte.STRIP_MALL,
                        '3210': cte.INDUSTRY,
                        '4834': cte.WAREHOUSE,
                        '3456': cte.INDUSTRY,
                        '2075': cte.INDUSTRY,
                        '3020': cte.INDUSTRY,
                        '3821': cte.INDUSTRY,
                        '6613': cte.MEDIUM_OFFICE,
                        '4826': cte.WAREHOUSE,
                        '5839': cte.MULTI_FAMILY_HOUSE,
                        '4316': cte.WAREHOUSE,
                        '6592': cte.OFFICE_AND_ADMINISTRATION,
                        '3971': cte.INDUSTRY,
                        '3972': cte.INDUSTRY,
                        '2694': cte.INDUSTRY,
                        '3882': cte.INDUSTRY,
                        '3119': cte.INDUSTRY,
                        '2495': cte.INDUSTRY,
                        '4759': cte.MEDIUM_OFFICE,
                        '6439': cte.WAREHOUSE,
                        '6643': cte.WAREHOUSE,
                        '3470': cte.INDUSTRY,
                        '3531': cte.INDUSTRY,
                        '4823': cte.NON_HEATED,
                        '2293': cte.INDUSTRY,
                        '3532': cte.INDUSTRY,
                        '3913': cte.INDUSTRY,
                        '6816': cte.OFFICE_AND_ADMINISTRATION,
                        '3562': cte.INDUSTRY,
                        '6496': cte.COMMERCIAL,
                        '4119': cte.WAREHOUSE,
                        '6533': cte.OUT_PATIENT_HEALTH_CARE,
                        '6814': cte.PRIMARY_SCHOOL,
                        '6353': cte.WAREHOUSE,
                        '3392': cte.INDUSTRY,
                        '5114': cte.STRIP_MALL,
                        '5131': cte.STRIP_MALL,
                        '3641': cte.INDUSTRY,
                        '2614': cte.INDUSTRY,
                        '3661': cte.INDUSTRY,
                        '2081': cte.INDUSTRY,
                        '3340': cte.INDUSTRY,
                        '4928': cte.WORKSHOP,
                        '3712': cte.INDUSTRY,
                        '3253': cte.INDUSTRY,
                        '3860': cte.INDUSTRY,
                        '3892': cte.INDUSTRY,
                        '2992': cte.INDUSTRY,
                        '5598': cte.RETAIL_SHOP_WITHOUT_REFRIGERATED_FOOD,
                        '4825': cte.NON_HEATED,
                        '2071': cte.INDUSTRY,
                        '6495': cte.INDUSTRY,
                        '2914': cte.INDUSTRY,
                        '3182': cte.INDUSTRY,
                        '3791': cte.INDUSTRY,
                        '3992': cte.INDUSTRY,
                        '3114': cte.INDUSTRY,
                        '7920': cte.OFFICE_AND_ADMINISTRATION,
                        '5891': cte.RESTAURANT,
                        '5835': cte.SMALL_HOTEL,
                        '6565': cte.HEALTH_CARE,
                        '3391': cte.INDUSTRY,
                        '6615': cte.INDUSTRY,
                        '3883': cte.INDUSTRY,
                        '2032': cte.INDUSTRY,
                        '2994': cte.INDUSTRY,
                        '4871': cte.INDUSTRY,
                        '5113': cte.WORKSHOP,
                        '3571': cte.INDUSTRY,
                        '2342': cte.INDUSTRY,
                        '3911': cte.INDUSTRY,
                        '7444': cte.EDUCATION,
                        '2221': cte.INDUSTRY,
                        '8192': cte.FARM,
                        '2439': cte.INDUSTRY,
                        '3891': cte.INDUSTRY,
                        '6354': cte.WORKSHOP,
                        '4815': cte.NON_HEATED,
                        '6651': cte.WORKSHOP,
                        '2822': cte.INDUSTRY,
                        '2821': cte.INDUSTRY
                        }

  @property
  def dictionary(self) -> dict:
    """
    Get the dictionary
    :return: {}
    """
    return self._dictionary
