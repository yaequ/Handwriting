from PIL import Image, ImageDraw, ImageFont
import textwrap

# Replace 'your_font.ttf' with the path to your TTF font file.
font_path = r"C:\Users\Lennard Serocka\Desktop\Handwriting python\Font1-Regular.ttf"

# Replace 'your_text.txt' with the path to your text file.
text_file_path = "your_text.txt"

# Read the content of the text file, preserving line breaks.
try:
    with open(text_file_path, "r") as file:
        text = file.read()
except FileNotFoundError as e:
    print(f"Error reading the text file: {e}")
    exit()

# Define the font size and image size.
font_size = 36
image_size = (1920, 1080)  # Updated image size to 1920x1080

# Create a new image with a white background.
image = Image.new("RGB", image_size, color="white")

# Load your custom font.
try:
    font = ImageFont.truetype(font_path, font_size)
except OSError as e:
    print(f"Error loading the font: {e}")
    exit()

# Create a drawing context.
draw = ImageDraw.Draw(image)

# Set the text color (black in this example).
text_color = (0, 0, 0)

# Initialize variables for text placement.
x = 100  # Starting x-coordinate (adjust as needed)
y = 50   # Starting y-coordinate

# Split the text into paragraphs (lines) based on the existing line breaks.
paragraphs = text.splitlines()

# Draw the text on the image, one paragraph (line) at a time.
for paragraph in paragraphs:
    # Preserve empty lines
    if not paragraph.strip():
        y += font_size  # Move to the next line
        continue

    # Wrap the paragraph to fit within the maximum character limit per line.
    max_characters_per_line = 150  # Adjust as needed
    wrapped_paragraph = textwrap.fill(paragraph, width=max_characters_per_line)

    # Draw the wrapped paragraph on the image.
    text_width, text_height = draw.textsize(wrapped_paragraph, font=font)
    draw.text((x, y), wrapped_paragraph, fill=text_color, font=font)
    y += text_height  # Move to the next line

# Save the image as a PNG file.
image.save("output.png")

# Display a success message.
print('Image saved as "output.png"')
