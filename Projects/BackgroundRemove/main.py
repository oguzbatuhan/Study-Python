from rembg import remove

path_input = 'squirrel-1.jpg'
path_output = 'output.png'

with open(path_input, 'rb') as i:
    with open(path_output, 'wb') as o:
        input_data = i.read()
        output_data = remove(input_data)
        o.write(output_data)