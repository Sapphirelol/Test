import json

step1_in = 'example1.json'
step1_out = ""

def jsonToHtml(step1_in, step1_out):
    try:
        with open(step1_in, 'r') as x:
            data = json.load(x)
            for i in range(len(data)):
                title = str(data[i]['title'])
                body = str(data[i]['body'])
                step1_out = step1_out + "<h1>" + title + "</h1> <p>" + body +"</p>"
            print(step1_out)
    except Exception:
        print("json is empty")
