from PIL import Image, ImageFilter

def load_image(filename):
    try:
        image = Image.open(filename)
        return image
    except FileNotFoundError:
        print("Error: Image file not found.")
        return None

def display_image(image):
    if image:
        image.show()

def convert_to_grayscale(image):
    if image.mode == "RGB":
        grayscale_image = image.convert("L")
        return grayscale_image
    else:
        print("Error: Image is not in RGB mode.")
        return None

def apply_sharpen_filter(image):
    sharpened_image = image.filter(ImageFilter.SHARPEN)
    return sharpened_image

def image_processing_toolbox():
    print("Image Processing Toolbox")
    filename = input("Enter the name of the image file: ")

    # Load the image
    image = load_image(filename)

    # Display the original image
    display_image(image)

    # Convert to grayscale
    grayscale_image = convert_to_grayscale(image)

    # Display the grayscale image
    display_image(grayscale_image)

    # Apply sharpening filter
    sharpened_image = apply_sharpen_filter(image)

    # Display the sharpened image
    display_image(sharpened_image)


if __name__ == "__main__":
    image_processing_toolbox()
