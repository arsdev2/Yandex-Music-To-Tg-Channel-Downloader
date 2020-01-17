import setuptools

with open("README.rst", "r", encoding='utf8') as fh:
    long_description = fh.read()
print(long_description)
setuptools.setup(
    name="ya-music-to-tg-channel-downloader-pkg-arsdev", # Replace with your own username
    version="0.0.3",
    author="Arsen Denisuk",
    author_email="senjka4@gmail.com",
    description="Script for downloading yamusic to tg channel",
    long_description=long_description,
    long_description_content_type="text/x-rst; charset=UTF-8",
    url="https://github.com/arsdev2/Yandex-Music-To-Tg-Channel-Downloader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)