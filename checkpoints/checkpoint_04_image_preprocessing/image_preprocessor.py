#!/usr/bin/env python3
"""
Checkpoint 4: Image Preprocessing Utility
Prepares images for Qwen2-VL model:
- Resizes to max 512x512 (keeps aspect ratio)
- Compresses to reduce token count
- Converts to Base64 for API transmission
"""

from PIL import Image
import base64
import io
import os

class ImagePreprocessor:
    """Preprocesses images for vision model inference"""

    def __init__(self, max_size=512, quality=85):
        """
        Args:
            max_size: Maximum width/height in pixels
            quality: JPEG quality (1-100, lower = smaller file)
        """
        self.max_size = max_size
        self.quality = quality

    def resize_image(self, image):
        """Resize image while maintaining aspect ratio"""
        # Get current size
        width, height = image.size

        # Calculate new size
        if width > height:
            if width > self.max_size:
                new_width = self.max_size
                new_height = int((height / width) * self.max_size)
            else:
                new_width, new_height = width, height
        else:
            if height > self.max_size:
                new_height = self.max_size
                new_width = int((width / height) * self.max_size)
            else:
                new_width, new_height = width, height

        # Resize
        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    def compress_image(self, image):
        """Compress image to reduce file size"""
        # Convert to RGB if necessary (handles PNG with alpha)
        if image.mode in ('RGBA', 'LA', 'P'):
            # Create white background
            background = Image.new('RGB', image.size, (255, 255, 255))
            if image.mode == 'P':
                image = image.convert('RGBA')
            background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
            image = background
        elif image.mode != 'RGB':
            image = image.convert('RGB')

        # Compress to bytes
        buffer = io.BytesIO()
        image.save(buffer, format='JPEG', quality=self.quality, optimize=True)
        buffer.seek(0)

        return buffer

    def to_base64(self, image_buffer):
        """Convert image buffer to Base64 string"""
        image_bytes = image_buffer.read()
        base64_string = base64.b64encode(image_bytes).decode('utf-8')
        return base64_string

    def process_file(self, image_path):
        """
        Process an image file end-to-end

        Args:
            image_path: Path to image file

        Returns:
            dict with processed image info
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")

        # Load image
        original_image = Image.open(image_path)
        original_size = os.path.getsize(image_path)
        original_dimensions = original_image.size

        # Process
        resized_image = self.resize_image(original_image)
        compressed_buffer = self.compress_image(resized_image)
        compressed_size = compressed_buffer.getbuffer().nbytes
        base64_string = self.to_base64(compressed_buffer)

        return {
            'original_size_kb': original_size / 1024,
            'original_dimensions': original_dimensions,
            'processed_size_kb': compressed_size / 1024,
            'processed_dimensions': resized_image.size,
            'compression_ratio': original_size / compressed_size,
            'base64_string': base64_string,
            'base64_length': len(base64_string)
        }

    def process_url(self, image_path):
        """
        Process image and return data URL for API

        Args:
            image_path: Path to image file

        Returns:
            Data URL string for API (data:image/jpeg;base64,...)
        """
        result = self.process_file(image_path)
        return f"data:image/jpeg;base64,{result['base64_string']}"


if __name__ == '__main__':
    # Example usage
    print("="*60)
    print("📸 Image Preprocessor - Example Usage")
    print("="*60)
    print()

    # Create preprocessor
    preprocessor = ImagePreprocessor(max_size=512, quality=85)

    # Example: Process a test image
    test_image_path = "../../data/test_images/sample.jpg"

    if os.path.exists(test_image_path):
        print(f"Processing: {test_image_path}")
        result = preprocessor.process_file(test_image_path)

        print(f"\n✅ Processing complete!")
        print(f"   Original: {result['original_dimensions'][0]}x{result['original_dimensions'][1]} ({result['original_size_kb']:.2f} KB)")
        print(f"   Processed: {result['processed_dimensions'][0]}x{result['processed_dimensions'][1]} ({result['processed_size_kb']:.2f} KB)")
        print(f"   Compression: {result['compression_ratio']:.2f}x smaller")
        print(f"   Base64 length: {result['base64_length']:,} characters")
    else:
        print(f"⚠️  Test image not found: {test_image_path}")
        print("   Add a test image to data/test_images/ to try this example")
