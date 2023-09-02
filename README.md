## Overview

This repository contains code for a semi-automated image annotation routine and potato beetle detection system using YOLOv4. The system is designed to detect potato beetles in high-resolution images, assisting researchers and farmers in pest monitoring and management.

## Getting Started

Follow these steps to set up your environment and start using the system:

### 1. Create and Activate Your Environment

You can use `conda` or `pip` to create a virtual environment. Replace `<env_name>` with your desired environment name.

#### Using Conda

```bash
conda create --name <env_name> python=3.7
conda activate <env_name>
```

#### Using Pip

```bash
python -m venv <env_name>
source <env_name>/bin/activate  # On Windows, use `<env_name>\Scripts\activate`
```

### 2. Install Dependencies

Navigate to the project directory and use `pip` to install the required packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. Start Testing

Now that you have set up your environment and installed the dependencies, you are ready to test the potato beetle detection system.

## Usage

To use the system, follow these steps:

1. **Dataset Preparation**: Gather a dataset of high-resolution images containing potato beetles.

2. **Image Annotation**: Develop a semi-automated image annotation routine (not included in this repository) to label potato beetle instances in the dataset.

3. **Training**: Train the YOLOv4 model using your annotated dataset. Fine-tune the model to improve potato beetle detection performance.

4. **Inference**: Use the trained model to detect potato beetles in new images.

5. **User Interface (Optional)**: Implement a user-friendly interface (not included in this repository) to facilitate semi-automated image annotation and detection.

## Directory Structure (this is not the current structure but we aim to follow it in the final application development)

- `data/`: Placeholder for dataset and annotations (not included in this repository).
- `model/`: Store your trained YOLOv4 model here.
- `src/`: Source code for the potato beetle detection system.
- `requirements.txt`: List of required packages.

## Contribution

Contributions to this project are welcome. You can contribute by:

- Reporting issues or suggesting improvements.
- Adding new features or enhancements.
- Providing documentation updates.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project is inspired by the YOLOv4 object detection model and aims to address the challenges in potato beetle detection in agriculture.
