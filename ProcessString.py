class ProcessStrings:
    def stringToList(self,words, separator):
        list = []
        if words == None or words == "" or separator == None or separator == "":
            return list
        try:
            list = words.split(separator)
        except Exception as e:
            print("error : "+ e)
        return list