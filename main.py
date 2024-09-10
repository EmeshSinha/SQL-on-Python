import file_management as fm
class data_defination_language:
    # def __init__(self):
    #      databases = ["info_schema"]
    #      tables = []
    #      {"databases":{tables:{"default":{"name":["devansh","Ritish","Anubhav","Emesh"]}}}}
    # def create(self,name_new):
    #           pass
    
    # def drop():
    #     pass
    # def alter():
    #     pass
    # def truncate():
    #     pass
    def create(name_new):
        fm.newtable(name_new)

if __name__ == "__main__":
    former = data_defination_language
    former.create("operator")

    