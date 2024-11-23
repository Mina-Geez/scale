
from setuptools import setup, find_packages

# Metadata and configuration for the app
setup(
    name="scale_integration",
    version="0.0.1",
    description="Integrates scale barcodes into ERPNext POS",
    author="Custom Dev",
    author_email="support@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
