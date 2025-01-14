import setuptools
import captchaOCR

with open("README.md", "r", encoding='utf-8') as fp:
    long_description = fp.read()

setuptools.setup(
    name = captchaOCR.__title__,
    version = captchaOCR.__version__,
    author = captchaOCR.__author__,
    author_email = captchaOCR.__author_email__,
    description = captchaOCR.__description__,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = captchaOCR.__url__,
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ['numpy', 'onnxruntime', 'Pillow'],
    python_requires = '<3.11',
    include_package_data=True,
    install_package_data=True,
)
