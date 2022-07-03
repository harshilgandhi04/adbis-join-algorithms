import sys

class DataPartitioning:

    def __init__(self):

        self.properties = {}

    def preprocess_data(self, file_name):

        with open(file_name, "r", encoding='utf-8') as file:

            for line in file:
                line = line.split(".")[0].lower()

                words = line.split("\t")
                subject = words[0].split(":")[1].strip()
                property = words[1].split(":")[1].strip()
                object = words[2].split(":")[1].strip() if len(words[2].split(":")) > 1 else words[2].strip()

                if property not in self.properties:
                   self.properties[property] = [(subject, object)]
                else:
                    self.properties[property].append((subject, object))


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Incorrect Arguments")
        exit(1)

    #file_name = sys.argv[1]
    file_name = "100k.txt"
    dpObj = DataPartitioning()
    dpObj.preprocess_data(file_name)
    print(len(dpObj.properties))
