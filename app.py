"""
Driver License Generator Application
အင်္ဂလိပ်/မြန်မာ Driver License ဖန်တီးပေးသည့် Flask Application
"""

from flask import Flask, render_template, request, send_file, jsonify
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta
import os
import io
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    """Main page - Driver License Generator Form"""
    return render_template('index.html')

@app.route('/api/generate-license', methods=['POST'])
def generate_license():
    """Generate Driver License Image"""
    try:
        # Get form data
        data = request.form
        
        # Get uploaded photo
        if 'photo' not in request.files:
            return jsonify({'error': 'No photo uploaded'}), 400
        
        photo = request.files['photo']
        
        # Extract form data
        first_name = data.get('first_name', 'N/A')
        last_name = data.get('last_name', 'N/A')
        license_number = data.get('license_number', str(uuid.uuid4())[:12].upper())
        dob = data.get('dob', '01/01/1990')
        gender = data.get('gender', 'M')
        address = data.get('address', 'Myanmar')
        state = data.get('state', 'Myanmar')
        
        # Create license image (Credit Card size: 3.375 x 2.125 inches at 300 DPI)
        width, height = 1012, 637  # pixels (300 DPI)
        
        # Create new image with gradient background
        license_img = Image.new('RGB', (width, height), color=(0, 102, 204))
        draw = ImageDraw.Draw(license_img)
        
        # Load or create fonts (try common system fonts, fallback to default)
        try:
            title_font = ImageFont.truetype("arial.ttf", 32)
            header_font = ImageFont.truetype("arial.ttf", 24)
            normal_font = ImageFont.truetype("arial.ttf", 18)
            small_font = ImageFont.truetype("arial.ttf", 14)
        except:
            title_font = ImageFont.load_default()
            header_font = ImageFont.load_default()
            normal_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
        
        # Add white rectangle for main content area
        draw.rectangle([(20, 20), (width-20, height-20)], fill='white', outline='black', width=3)
        
        # Add title
        draw.text((width//2 - 100, 30), "DRIVER'S LICENSE", fill='black', font=title_font)
        
        # Add country/state flag area
        draw.rectangle([(30, 70), (250, 150)], outline='black', width=2)
        draw.text((40, 80), "MYANMAR", fill='black', font=header_font)
        draw.text((40, 115), state.upper(), fill='blue', font=normal_font)
        
        # Add photo placeholder (if photo uploaded, use it)
        photo_x, photo_y = 30, 160
        photo_size = 150
        
        try:
            img = Image.open(photo)
            img.thumbnail((photo_size, photo_size))
            license_img.paste(img, (photo_x, photo_y))
        except:
            # Draw placeholder if photo fails
            draw.rectangle([(photo_x, photo_y), (photo_x + photo_size, photo_y + photo_size)], 
                          outline='gray', width=2)
            draw.text((photo_x + 40, photo_y + 60), "PHOTO", fill='gray', font=normal_font)
        
        # Add personal information
        info_x = 250
        info_y = 70
        line_height = 35
        
        draw.text((info_x, info_y), f"NAME: {first_name} {last_name}", fill='black', font=normal_font)
        draw.text((info_x, info_y + line_height), f"LICENSE NO: {license_number}", fill='black', font=normal_font)
        draw.text((info_x, info_y + 2*line_height), f"DOB: {dob}", fill='black', font=normal_font)
        draw.text((info_x, info_y + 3*line_height), f"GENDER: {gender}", fill='black', font=normal_font)
        
        # Add address
        draw.text((30, 330), f"ADDRESS: {address}", fill='black', font=small_font)
        
        # Add issue and expiry dates
        issue_date = datetime.now().strftime('%m/%d/%Y')
        expiry_date = (datetime.now() + timedelta(days=365*5)).strftime('%m/%d/%Y')
        
        draw.text((30, 370), f"ISSUE DATE: {issue_date}", fill='black', font=small_font)
        draw.text((500, 370), f"EXPIRY DATE: {expiry_date}", fill='red', font=small_font)
        
        # Add hologram/security pattern (simple diagonal lines)
        for i in range(0, width, 20):
            draw.line([(i, height-60), (i+40, height-20)], fill=(200, 200, 200), width=1)
        
        # Add signature area
        draw.text((30, height-50), "SIGNATURE", fill='gray', font=small_font)
        draw.line([(30, height-25), (200, height-25)], fill='black', width=2)
        
        # Convert to bytes
        img_io = io.BytesIO()
        license_img.save(img_io, 'PNG', quality=95)
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png', as_attachment=True, 
                        download_name=f"license_{license_number}.png")
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'OK', 'message': 'Driver License Generator is running'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)