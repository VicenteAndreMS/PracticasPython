file = "texto2.txt"
def overwrite(file):
    overwritten_file = open(file,'w')

    overwritten_file.write("Eliminated content")

    overwritten_file.close()

overwrite(file)

