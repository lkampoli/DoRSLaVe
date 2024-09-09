import fitz  # PyMuPDF
from PIL import Image
import io
import os

# Function to save images as PNG
def save_image(image_bytes, image_index, output_folder):
    # Convert bytes to a Pillow image
    image = Image.open(io.BytesIO(image_bytes))
    # Create an output file path
    output_path = os.path.join(output_folder, f'image_{image_index}.png')
    # Save the image as PNG
    image.save(output_path)
    print(f"Saved: {output_path}")

# Function to extract images from PDF
def extract_images_from_pdf(pdf_path, output_folder):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_index = 0

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        image_list = page.get_images(full=True)

        # Iterate through the images on the page
        for img in image_list:
            xref = img[0]
            # Extract the image bytes
            image_bytes = pdf_document.extract_image(xref)["image"]
            # Save the image
            save_image(image_bytes, image_index, output_folder)
            image_index += 1

    pdf_document.close()
    print(f"Extraction complete! {image_index} images were saved.")

# Input and output paths
pdf_path = "chapt4.pdf"  # Replace with the path to your PDF file
output_folder = "extracted_images"  # Folder where images will be saved

# Run the extraction
extract_images_from_pdf(pdf_path, output_folder)

