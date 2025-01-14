[![PyPi](https://img.shields.io/pypi/v/opaw)](https://pypi.org/project/opaw/)


# openai-pw
Unofficial python wrapper of [OpenAI](https://openai.com/) API.


# Features
- Wrapped models (chat, audio, image, embeddings ...)
- History(conversations) save and load


# Quick start
You can also play with in [this colab](https://colab.research.google.com/drive/1nJ1-YwLMSxSVx092uBVoarvuVUyt65xC?usp=drive_link). Or

1. Download `openai` and [`opaw`](https://pypi.org/project/opaw/) using pip. 
```cmd
pip install openai opaw
```
2. Create a `open-api-key.txt` file and insert [your api key](https://platform.openai.com/account/api-keys) into the file. Or set an environment variable with the name `OPENAI_API_KEY`.
3. Write a demo code and play with ChatGPT.
```py
from opaw.examples.basic import loop_chat 
from opaw import util

util.setup() # api key setup
loop_chat() # start chat
```


# Examples
Try to run something in [examples](opaw/examples) after downloaded this repo.


# OpenAI links
- [API](https://platform.openai.com/docs/api-reference/introduction)
- [model list](https://platform.openai.com/docs/models)
- [community](https://community.openai.com/)
- [usage](https://platform.openai.com/account/usage)
- [api key](https://platform.openai.com/account/api-keys)


# License
MIT