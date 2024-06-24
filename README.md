# wCloud
 The script processes a Chinese interview text to segment words with jieba and generates a word cloud.

# How to use

## Get the repo
```bash
git clone https://github.com/sepinetam/wCloud.git
```

## Create a Virtual Environment and Install Dependencies
```bash
cd wCloud

python -m venv venv
source venv/bin/avtivate

pip install -r requirements.txt
```

## Usage
1. Modify/import txt text files into the in folder.
2. Determine the font to use (default is SimHei).
3. Run the script.

### Example Usage
The example file is ```in/example.txt```.

The returned file is ```out/example.png```.

Font selection is SimSun.

```bash
python main.py example SimSun
```

### Example Explanation
- The input file is ```in/example.txt```.
- The resulting word cloud image is ```out/example.png```.
- The chosen font is ```SimSun.ttf``` in the root directory.

### Parameter Explanation
```bash
python main.py file font
```
- Parameter 1 (file): The name of the input file (".txt" is optional). If not provided, the default is "test".
- Parameter 2 (font): The font (".ttf" is optional). If not provided, the default is "SimHei".

# Acknowledgements
## Chinese Font Provision
Thanks to [@StellarCN](https://github.com/StellarCN) for providing the font ```SimHei```. Wishing StellarCN continued success.

Thanks to Sociology and Political Science student [@Esme](mailto:esme2004dash@163.com) from Shanghai University for the requirements, which inspired me to write this small tool.
