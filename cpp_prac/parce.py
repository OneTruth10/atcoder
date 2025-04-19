import pandas as pd
def print_grid(given_url):
    url = given_url
    df = pd.read_html(url, encoding='utf-8')
    table = df[0]
    max_x = 1
    max_y = 1
    coordinates = []
    for i in range(1, len(table)):
        row = table.iloc[i]
        x = int(row[0])
        y = int(row[2])
        character = row[1]
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        coordinates.append(tuple([x,y,character]))
    grid = [[" " for i in range(max_x+1)] for i in range(max_y+1)]
    for coor in coordinates:
        x = coor[0]
        y = coor[1]+1
        grid[-y][x] = coor[2]
        
    for i in range(len(grid)):
        print("".join(grid[i]))

print_grid("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")
