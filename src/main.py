import sys


class Main:
    def __init__(self, arg_list, logger=None):
        pass
        # add logging config
        # parse input args
        # update the sys path variable to set up working directory


    def execute(self):
        # extract the required class from config manager and hand off execution to it
        # import the required class from class map
        from class_map import ClassMap
        class_map = ClassMap.get_class_map()
        # log checkpoints
        # set spark run time env
        # create instance of class name from config and call its execute method
        pass


if __name__ == "__main__":
    main_obj = Main(sys.argv)
    main_obj.execute()
