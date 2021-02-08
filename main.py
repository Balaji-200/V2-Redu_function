from PIL import Image, ImageDraw, ImageFont
from flask import send_file, jsonify
from io import BytesIO
def generate_certificate(request):
    request_json = request.get_json(silent=True)
    op_image = BytesIO()
    image = Image.open(r'certificate.jpg')
    width, height = image.size
    font_size = int((width - height) / 5)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(r"Great_Vibes/GreatVibes-Regular.ttf", size=font_size)
    w, h = draw.textsize(str(request_json['username']), font=font)
    draw.text((int((width-w)/2), int(height)/2), str(request_json['username']), fill=(0, 0, 0), font=font)
    image.save(op_image, 'JPEG')
    op_image.seek(0)
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
        return (send_file(op_image, mimetype="image/jpeg"), 200, headers)
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    return (send_file(op_image, mimetype="image/jpeg"), 200, headers)


