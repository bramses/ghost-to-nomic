# ghost-to-nomic
Upload your Ghost blog posts as a Nomic Map

![Screenshot 2024-02-12 19-47-02](https://github.com/bramses/ghost-to-nomic/assets/3282661/c8f4e237-7126-429c-998d-9c75ab626e55)


## in ghost

export your content

![Screenshot 2024-02-12 19-54-59](https://github.com/bramses/ghost-to-nomic/assets/3282661/1d417753-dc13-45f4-9d5c-ffb4a8cd6855)
![Screenshot 2024-02-12 19-55-02](https://github.com/bramses/ghost-to-nomic/assets/3282661/c2ef905d-d3a2-402c-990d-8ca9c971d771)

## in terminal

run `python main.py {YOUR_FILENAME}`

## in nomic

upload and use `plaintext` or `html` as index (html will include image links and stuff but will introduce noise) or `title`

![Screenshot 2024-02-12 19-51-44](https://github.com/bramses/ghost-to-nomic/assets/3282661/6f7076e5-bde7-4f5d-90e9-9366c9d809f6)

### or in python

start a poetry shell 

`poetry shell`

poetry install

`poetry install`

login to nomic

`nomic login [YOUR_API_KEY]` ([Nomic Atlas Quickstart | Nomic Atlas Documentation](https://docs.nomic.ai/atlas/introduction/quick-start))

![Screenshot 2024-02-13 10-04-34](https://github.com/bramses/ghost-to-nomic/assets/3282661/e5d8b9e3-fff5-4469-8bae-0cd6130538ba)


run the atlas script

`python atlas.py`
