import os
import cv2 as cv

def create_dir(main_dir):
    for i in range(10):
        directory = os.path.join(main_dir, str(i))
        if not os.path.exists(directory):
            os.makedirs(directory)

def save_digits(image_path, output_dir):
    
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    rows, cols = image.shape

    create_dir(output_dir)

    digit_height = 20
    digit_width = 20
    num_rows_per_digit = 5

    digit_label = 0
    image_counter = 0

    for i in range(0, rows, digit_height):
        for c in range(0, cols, digit_width):
            image_counter += 1
            cropped_digit = image[i:i + digit_height, c:c + digit_width]
            digit_path = os.path.join(output_dir, str(digit_label), f'{image_counter}.png')
            cv.imwrite(digit_path, cropped_digit)
        
        if (i // digit_height + 1) % num_rows_per_digit == 0:
            digit_label += 1
            image_counter = 0  


save_digits('image (1).png', 'Dataset')
