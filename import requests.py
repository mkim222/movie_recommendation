import requests

file_url = 'https://drive.google.com/file/d/1IV7hw3jWCZ2G5FVF1D-yzl6dLCytFSty/view?usp=sharing'
response = requests.get(file_url)
with open('cosine_sim.pickle', 'wb') as f:
    f.write(response.content)
    
file_url = 'https://drive.google.com/file/d/1oADuqC0TyAjvsIPy-0gbMmDOMzg4tn2m/view?usp=sharing'
response = requests.get(file_url)
with open('movies.pickle', 'wb') as f:
    f.write(response.content)
    
    