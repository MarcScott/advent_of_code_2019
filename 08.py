def get_image(file_name):
    with open(file_name) as f:
        image = [int(i) for i in f.readline().rstrip().split()[0]]
    return image

def get_row(image, start_index, width):
    row = [image[start_index:][pixel] for pixel in range(width)]
    return row

def get_layer(image, start_index, width, height):
    layer = [[] for i in range(height)]
    for i in range(height):
        layer[i] = get_row(image, start_index, width)
        start_index += width
    return layer, start_index

def get_all_layers(image, start_index, width, height):
    num_layers = int(len(image) / (width * height))
    all_layers = [[] for i in range(num_layers)]
    for layer in range(num_layers):
        all_layers[layer], start_index = get_layer(image, start_index, width, height)
    return all_layers

def count_digit(layer, digit):
    flattened = []
    for row in layer:
        flattened += row
    return flattened.count(digit)

def merge_layers(all_layers):
    final_image = all_layers[0].copy()
    for l, layer in enumerate(all_layers):
        for r, row in enumerate(layer):
            for p, pixel in enumerate(row):
                if pixel == 0 or pixel == 1:
                    final_image[r][p] = pixel
                    
                
    return final_image
                
                

image = get_image("08.txt")
all_layers = get_all_layers(image, 0, 25, 6)
num_zeros = [count_digit(layer, 0) for layer in all_layers]
num_ones = [count_digit(layer, 1) for layer in all_layers]
num_twos = [count_digit(layer, 2) for layer in all_layers]

position = num_zeros.index(min(num_zeros))
total = num_ones[position] * num_twos[position]
print(total)

all_layers.reverse()

for i in merge_layers(all_layers):
    print(i)
