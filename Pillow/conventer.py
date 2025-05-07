from PIL import Image


demand =input("What is ur location of file\n")
came = Image.open(demand)


'''
formats={
    "JPEG","output.jpg"
    "GIF", "output.gif "
    "PNG", "output.png"
    "ICO", "outputs.ico"
    "PDF", "output.pdf"
}
'''

format_name = input("""write type format
                        JPEG,"output.jpg"
                        "GIF", "output.gif "
                        "PNG", "output.png"
                        "ICO", "outputs.ico"
                        "PDF", "output.pdf\n""")

icon=(format_name[len(format_name)-3:]).upper()

# iconimg = came.resize((256,256))

came.save(format_name,format=icon)




