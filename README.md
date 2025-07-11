# 🖼️ Watermarking Desktop Application

A professional Python desktop application for adding watermarks to images with a user-friendly GUI built using Tkinter and PIL (Pillow).

## 📋 Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **User-Friendly GUI**: Clean and intuitive desktop interface built with Tkinter
- **Image Loading**: Browse and select PNG images from your computer
- **Live Preview**: View your original and watermarked images in real-time
- **Professional Watermarking**: Adds both text and pattern watermarks with transparency
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Smart Centering**: Automatically centers the application window on screen
- **One-Click Save**: Save watermarked images with automatic file naming
- **Auto-Open**: Automatically opens the saved watermarked image after saving
- **Responsive Design**: Image preview automatically resizes to fit the interface

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Quick Setup

1. **Clone or download the repository**

   ```bash
   git clone https://github.com/nbence-dev/watermarking_tkinter_python.git
   cd watermarking_tkinter_python
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

### Alternative Installation

If you prefer to install dependencies manually:

```bash
pip install pillow
```

## 🎯 Usage

### Step-by-Step Guide

1. **Launch the Application**

   - Run `python main.py` from the project directory
   - The application window will open and center on your screen

2. **Load an Image**

   - Click the "Add Image" button
   - Browse to your desired PNG image file
   - Select and open the image
   - The image will appear in the preview area

3. **Add Watermark**

   - Click the "Add Watermark" button (enabled after loading an image)
   - The watermark will be applied with:
     - Diagonal line pattern overlay
     - "Watermark" text in the center
     - Semi-transparent effects for professional appearance

4. **Save Your Image**

   - Click "Save New Image" (enabled after adding watermark)
   - The watermarked image is automatically saved in the same folder as the original
   - Filename format: `watermarked_[original_filename].png`
   - The saved image opens automatically

5. **Close Application**
   - Click "Close Application" to exit

### Supported Formats

- **Input**: PNG files only
- **Output**: PNG format with transparency support

## 🔧 Technical Details

### Watermark Features

- **Pattern Overlay**: Diagonal lines across the entire image
- **Text Watermark**: Centered "Watermark" text
- **Transparency**: Configurable opacity levels
- **Color**: White with alpha transparency
- **Font**: Arial, 80pt size for text
- **Quality**: High-quality resampling using LANCZOS filter

### Cross-Platform File Operations

The application includes smart file opening that works across different operating systems:

- **Windows**: Uses `os.startfile()`
- **macOS**: Uses `subprocess.run(["open", filepath])`
- **Linux**: Uses `subprocess.run(["xdg-open", filepath])`

### GUI Architecture

- **Framework**: Tkinter (Python's standard GUI library)
- **Layout**: Grid-based layout system
- **Responsive**: Dynamic window centering and image resizing
- **Icon**: Custom application icon (`watermark.ico`)
- **Dimensions**: 445x500 pixels main window

## 📁 Project Structure

```
Watermarking_App/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── watermark.ico       # Application icon
├── README.md           # Project documentation
├── .gitignore          # Git ignore rules
└── [watermarked images] # Output folder for processed images
```

### Key Files

- **`main.py`**: Core application with GUI and watermarking logic
- **`requirements.txt`**: Lists all required Python packages
- **`watermark.ico`**: Custom icon for the application window
- **`.gitignore`**: Excludes temporary files and processed images from version control

## 📦 Requirements

### Python Packages

- **Pillow (PIL)**: Image processing and manipulation
- **tkinter**: GUI framework (included with Python)
- **os**: File system operations (built-in)
- **platform**: Cross-platform compatibility (built-in)
- **subprocess**: External process execution (built-in)

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.6 or higher
- **Memory**: Minimum 256MB RAM
- **Storage**: 50MB free space for installation

## 🎨 Customization

### Modifying Watermark Text

To change the watermark text, edit line in the `add_watermark()` function:

```python
draw.text(position, "Your Custom Text", fill=watermark_color_text, font=font)
```

### Adjusting Transparency

Modify the alpha values in the watermark colors:

```python
watermark_color_pattern = (255, 255, 255, 30)  # Pattern transparency
watermark_color_text = (255, 255, 255, 80)     # Text transparency
```

### Changing Supported File Types

Update the file dialog filter in the `openFile()` function:

```python
filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Images", "*.png;*.jpg")]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Known Issues

- Currently supports PNG files only
- Watermark text is hardcoded (can be customized in code)
- Font path assumes Arial is available on the system

## 🔮 Future Enhancements

- [ ] Support for JPEG, GIF, and other image formats
- [ ] Customizable watermark text input
- [ ] Multiple watermark positioning options
- [ ] Batch processing capabilities
- [ ] Watermark opacity slider
- [ ] Custom font selection
- [ ] Image rotation and scaling options

## 👨‍💻 Author

**Nicholas** - [nbence-dev](https://github.com/nbence-dev)

## 🙏 Acknowledgments

- Python Software Foundation for the amazing Python language
- Pillow team for the excellent image processing library
- Tkinter developers for the GUI framework

---

_Built with ❤️ using Python and Tkinter_
