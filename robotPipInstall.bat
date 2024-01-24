echo "checking if pip is installed ...."
if ! command -v pip &> /dev/null; then
	echo "You need to installed pip to use this script"
	exit 1
else
	echo "Staring to install package, Hoopa...."
	pip install torch, torchvision, torchaudio 
fi

if [ $? -eq 0 ]; then
    echo "Packages installed successfully."
else
    echo "Error: Failed to install packages. Please check the error messages above."
fi