
class AutoBuild(object):
    def __init__(self,name:str):
        self._name = name
        self._map = {}

    def register(self, key):
        def _register(cls):
            print(f'register cls_name:{self._name} key:{key} cls:{cls}')
            self._map[key] = cls
            return cls
        return _register

    def get_cls(self, key):
        if key not in self._map:
            return None
        print(f'get_cls cls_name:{self._name} key:{key} cls:{self._map[key]}')
        return self._map[key] 


DataCollatorRg = AutoBuild('datacollator')
MetricRg = AutoBuild('metric')
ModelRg = AutoBuild('model')
PreProcessorRg = AutoBuild('preprocessor')
TrainerRg = AutoBuild('trainer')

def auto_build(reg:AutoBuild, key):
    return reg.get_cls(key)
    