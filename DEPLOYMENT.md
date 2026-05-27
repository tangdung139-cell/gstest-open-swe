# Deployment Guide for Python Image Resizer Application

This guide explains how to deploy the Python image resizer application that resizes JPG and PNG images.

## Prerequisites

- **Python Environment**:
  - Install Python 3.7 or higher.
  - Ensure `pip` is installed for managing Python packages.
- **Libraries**:
  - The application relies on the `Pillow` library. Install it by running:
    ```bash
    pip install pillow
    ```

## Steps to Deploy

1. **Clone the Repository**:
   Clone the project repository to your local machine:
   ```bash
   git clone https://github.com/tangdung139-cell/gstest-open-swe.git
   cd gstest-open-swe
   ```

2. **Set Up Virtual Environment (Optional)**:
   It is recommended to use a virtual environment for Python dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   Use the `pip` command to install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   If the `requirements.txt` file is missing, manually install `Pillow` as shown earlier.

4. **Prepare Input Images**:
   Place the JPG and PNG images you want to resize in a directory (e.g., `input_images`).

5. **Run the Application**:
   Execute the script with the following command:
   ```bash
   python image_resizer.py <input_dir> <output_dir> <width> <height>
   ```
   Replace `<input_dir>` with the path to your input images directory, `<output_dir>` with the directory to save resized images, and `<width>` & `<height>` with the desired dimensions.

   Example:
   ```bash
   python image_resizer.py input_images resized_images 800 600
   ```

6. **Verify Resized Images**:
   Check the `output_dir` to confirm that the images have been resized.

7. **Deployment on Server (Optional)**:
   - Upload the project files to your server.
   - Install all dependencies on the server environment.
   - Set up a scheduled job or API endpoint if you plan to integrate this utility into other services.

## Notes

- Make sure to test the application with a variety of image formats and sizes to validate its functionality.
- For large-scale usage, consider using a job queue system to handle batch resizing tasks.

## Support

For any issues or questions, please raise them in the project repository's issue tracker.