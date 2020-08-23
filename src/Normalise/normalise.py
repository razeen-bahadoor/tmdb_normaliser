import json
def process_line(row):
    line = dict()
    line["id"] = row["id"]
    line["title"] = row["original_title"]
    line["overview"] = row["overview"]
    line["genres"] = str(row["genres"]).split('|')
    line["runtime"]=row["runtime"]
    line["release_date"] = row["release_date"]
    line["release_year"] = row["release_year"]
    line["cast"] = str(row["cast"]).split('|')
    line["director"]=row["director"]
    return (json.dumps(line,ensure_ascii=False)+'\n')