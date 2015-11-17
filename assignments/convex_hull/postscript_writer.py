


def write_hull(points:list, filename:str):
    with open(filename, "w") as file_hull:
        file_hull.write("0.9 setgray\n0.1 setlinewidth\n")
        file_hull.write(points[0].name + " moveto\n")
        for p in points[1:]:
            file_hull.write(p.name + " lineto\n")
        file_hull.write("closepath fill\n0 setgray\n\n")
        file_hull.write("0.1 setlinewidth\n")
        file_hull.write(points[0].name + " moveto\n")
        for p in points[1:]:
            file_hull.write(p.name + " lineto\n")
        file_hull.write("closepath stroke\n\n")
