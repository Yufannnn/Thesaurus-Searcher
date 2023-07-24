import argparse
from searcher import ThesaurusSearcher

def main():
    parser = argparse.ArgumentParser(description="Thesaurus Searcher CLI")
    parser.add_argument("word", help="The word to search for synonyms")
    parser.add_argument("--pos", choices=["noun", "verb", "adjective", "adverb"], default="noun",
                        help="Specify the part-of-speech of the word (default: noun)")
    parser.add_argument("--informal", action="store_true", help="Include informal synonyms")
    parser.add_argument("--vulgar", action="store_true", help="Include vulgar synonyms")
    parser.add_argument("--similarity", type=int, default=100, help="Minimum similarity score for synonyms (default: 100)")
    parser.add_argument("--with-info", action="store_true", help="Include additional information for synonyms")

    args = parser.parse_args()

    thesaurus_searcher = ThesaurusSearcher(
        include_informal=args.informal,
        include_vulgar=args.vulgar,
        required_similarity=args.similarity
    )

    if args.with_info:
        synonyms_with_info = thesaurus_searcher.get_synonyms_with_info(args.word, args.pos)
        if synonyms_with_info:
            print(f"Synonyms for '{args.word}' ({args.pos}) with information:")
            for idx, synonym_info in enumerate(synonyms_with_info, 1):
                print(f"{idx}. Term: {synonym_info['term']}, POS: {synonym_info['pos']}, "
                      f"Similarity: {synonym_info['similarity']}, "
                      f"Is Informal: {synonym_info['is_informal']}, "
                      f"Is Vulgar: {synonym_info['is_vulgar']}")
        else:
            print(f"No synonyms found for '{args.word}' ({args.pos}).")
    else:
        synonyms = thesaurus_searcher.get_synonyms(args.word, args.pos)
        if synonyms:
            print(f"Synonyms for '{args.word}' ({args.pos}):")
            for idx, synonym in enumerate(synonyms, 1):
                print(f"{idx}. {synonym}")
        else:
            print(f"No synonyms found for '{args.word}' ({args.pos}).")

if __name__ == "__main__":
    main()
