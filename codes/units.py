from enum import Enum

class UnitLevel(Enum):
    UFMS = {'code':0,'name':'УФМС'}
    REGION_UNIT = {'code':1,'name':'ГУВД или МВД'}
    CITY_UNIT = {'code':2,'name':'ГУВД или МВД'}
    VILLAGE_UNIT = {'code':3,'name':'отделение'}

    def get_unit_code(self):
        """ @:return unit code 0,1,2,3 """
        return self.value['code']

    def get_unit_name(self):
        """ @:return unit name УФМС, ГУВД, МВД, ОТДЕЛЕНИЕ """
        return self.value['name']

