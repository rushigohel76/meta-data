from PIL import Image
import pprint  # Optional for cleaner output

def get_image_metadata():
  """
  Extracts and displays image metadata using Pillow library.

  Args:
      image_path: Path to the image file.

  Returns:
      None
  """
  try:
    # Open the image
    img = Image.open(image_path)

    # Extract metadata dictionary
    exif_data = img.info

    # Print metadata in a readable format using pprint (optional)
    print("Image Metadata:")
    pprint.pprint(exif_data)

    # Alternatively, loop through the dictionary and print specific data
    # for key, value in exif_data.items():
    #   print(f"{key}: {value}")

  except FileNotFoundError:
    print(f"Error: Image file not found at '{image_path}'.")

# Example usage
image_path = "path/to/your/image.jpg"  # Replace with your image path
get_image_metadata(image_path)
