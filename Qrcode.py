import segno
from torchvision.utils import make_grid, save_image
import os
from torchvision.io import read_image
from torchvision import torch
from torchvision.transforms import transforms
def search(array,index):
    for element in array:
        if index in element:
            return element
        else:
            continue
    return ""

transform = transforms.Compose([
    transforms.CenterCrop(360),
    transforms.ConvertImageDtype(dtype=torch.float),
])

links_dict = {
    "Statia040": "https://forms.gle/yV329HHmrwggD9Jr5",
    "Statia027": "https://forms.gle/ThsiwQEWrqkqX7Je7",
    "Statia041": "https://forms.gle/kePSj5M9eg1FDRuw7",
    "Statia023": "https://forms.gle/6Rvc6amAT1KsuvGPA",
    "Statia039": "https://forms.gle/3Mn9SyKv7RTQZiEd9",
    "Statia005": "https://forms.gle/dLja1sd8GCLmbRGZ6",
    "Statia001": "https://forms.gle/ckdZVfkgajjjNv6K9",
    "Statia004": "https://forms.gle/jHubw6XMiRWnQWrr8",
    "Statia028": "https://forms.gle/9sHbVskAW1biWRWz6",
    "Statia024": "https://forms.gle/uQTgLncruCd19iTf7",
    "Statia043": "https://forms.gle/LW9kgtDNsRJWARNR6",
    "Statia044": "https://forms.gle/jkERoLk1Jua8yqqP8",
    "Statia053": "https://forms.gle/kPCdu79BgYyrobjh7",
    "Statia063": "https://forms.gle/JFqT514URV34jXUA9",
    "Statia064": "https://forms.gle/oRg7bGf9w7QSCSUM8" 
}
qr_codes = []
files= []
text_list = []
table = [['1/1','1/2','1/3'],
         ['2/1','2/2','2/3'],
         ['3/1','3/2','3/3'],
         ['4/1','4/2','4/3']]
str_table = ''
for row in range(4):
    for column in range(3):
        print(table[row][column], end=" ")
        str_table += table[row][column] + ' '
    print()
    str_table += '\n'
print(str_table)
print("Order is (column value(1-3)/row value(1-4)):")

row = 1
column = 0
for link in range(len(list(links_dict.keys()))):
    qr_code = segno.make_qr(list(links_dict.values())[link])
    column += 1
    if column > 3:
        column = 1
        row += 1
    text = 'Column value(' +str(row)+ ')/' + 'row value(' + str(column) + ') = ' + list(links_dict.keys())[link]    
    print(text)
    text_list.append(text)
    if list(links_dict.keys())[link] in ['Statia053', 'Statia063','Statia064']:
          qr_photo = qr_code.save(
        "qrcode" + str(link) +".png",
        scale=10)
    else:
        qr_photo = qr_code.save(
        "qrcode" + str(link) +".png",
        scale=10)


index = 0
files = []
for file_number in range(len(links_dict)):
        image = "qrcode" + str(file_number) + ".png"
        transformed_tensor = transform(read_image(image))
        qr_codes.append(transformed_tensor)
        index += 1

grid = make_grid(qr_codes, nrow=3, padding=5)
save_image(grid, "grid.jpg")
file = open('order.txt', 'w+')
file.write('example > \n')
file.write(str_table)
for line in text_list:
    
    file.write(line + '\n')
file.close()