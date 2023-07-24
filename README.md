# Thesaurus Searcher 📚🔍

Thesaurus Searcher is a Python command-line and GUI tool that allows users to search for synonyms of a given word. It fetches data from an online thesaurus and provides a list of synonyms based on user input.

## Features 🌟

- Search for synonyms of a word based on its part-of-speech (noun, verb, adjective, or adverb).
- Include or exclude informal and vulgar synonyms based on user preferences.
- Set a minimum similarity score for synonyms to be included in the results.
- Optionally display additional information for each synonym, including similarity, informality, and vulgarity.
- Provides a command-line interface for quick synonym searches.
- Offers a user-friendly GUI interface for a more interactive experience.

## Installation 🚀

1. Clone the repository:

```
git clone https://github.com/yourusername/thesaurus-searcher.git
cd thesaurus-searcher
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage 📝

### Command-Line Interface 💻

```
python thesaurus_searcher_cli.py [word] [--pos PART_OF_SPEECH] [--informal] [--vulgar] [--similarity SIMILARITY] [--with-info]
```

- `word`: The word to search for synonyms.
- `--pos`: Specify the part-of-speech of the word (default: noun).
- `--informal`: Include informal synonyms.
- `--vulgar`: Include vulgar synonyms.
- `--similarity`: Minimum similarity score for synonyms (default: 100).
- `--with-info`: Include additional information for synonyms.

### Graphical User Interface 🖥️

Run the following command to open the GUI application:

```
python main_window.py
```

Enter the word, select the part-of-speech, and choose other options to search for synonyms interactively.

## Examples 🧐

Search for synonyms of the word "happy" (adjective) with additional information:

```
python thesaurus_searcher_cli.py happy --pos adjective --with-info
```

Search for synonyms of the word "run" (verb) without additional information:

```
python thesaurus_searcher_cli.py run --pos verb
```

## Future Enhancements 🚀🔮

- Convert Thesaurus Searcher into a reusable library, allowing easy integration into other Python projects.
- Implement additional language support to fetch synonyms from multiple language thesauri.
- Enhance the GUI with more features, such as suggestions for similar words and saving favorite words for future reference.
- Improve search performance and efficiency by optimizing data retrieval from the online thesaurus.
- Provide support for custom thesaurus sources for users to integrate their preferred thesaurus APIs.

## Contributing 🤝🌟

Contributions are welcome! If you have any bug fixes, enhancements, or new features to propose, feel free to submit a pull request.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Yufannnn/Thesaurus-Searcher/blob/main/LICENSE) file for details.

## More to Come! 🎉🚀

Stay tuned for exciting updates and new features. I will continuously work on improving Thesaurus Searcher in my free time from school works. Follow this project on GitHub and join the community to be the first to know about the latest developments! 🌟🎉
