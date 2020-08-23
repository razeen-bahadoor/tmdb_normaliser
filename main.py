import csv

def normalise(out_path,in_path,module):

        f_out = open(out_path,'a')
        with open(in_path, mode = 'r',encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                line = module.process_line(line)
                f_out.write(line)

if __name__ == "__main__":
    import config
    import os
    from src.Normalise import normalise as normaliser
    if os.path.exists(config.TARGET["output"]) is False:
        os.mkdir(config.TARGET["output"])

    print("------Normalising dataset------")
    normalise(out_path = config.FILE_NAMES["output"],
                            in_path = config.FILE_NAMES["input"],
                            module = normaliser)
