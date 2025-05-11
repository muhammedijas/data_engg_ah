from typing import Dict


class ClassMap:
    @staticmethod
    def get_class_map() -> Dict:
        # import the transformation class
        # this dict maps the module_name from config to class name that will be instantiated and executed
        class_map_dict = {}
        return class_map_dict
