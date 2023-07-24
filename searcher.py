import re
import requests
import logging

from synonym import Synonym

class ThesaurusSearcher:
    def __init__(self, include_informal=False, include_vulgar=False, required_similarity=100):
        self.include_informal = include_informal
        self.include_vulgar = include_vulgar
        self.required_similarity = required_similarity
        self.logger = logging.getLogger(__name__)

    def get_html(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx errors
        except requests.exceptions.RequestException as err:
            self.logger.error(f"Error fetching thesaurus data: {err}")
            return None

        return response.text

    def get_synonyms(self, entry, pos):
        try:
            if not entry.strip():
                print("Provide a non-null input word")
                return []

            valid_pos = ['noun', 'verb', 'adjective', 'adverb']

            if pos not in valid_pos:
                raise ValueError(f"Invalid part of speech: {pos}")

            url = f'http://www.thesaurus.com/browse/{entry}'
            html = self.get_html(url)

            if not html:
                return []

            synonyms_result = self.analyze_thesaurus_html(html, entry, pos)
            synonyms_result = self.filter_synonyms(synonyms_result)
            synonyms_result.sort(key=lambda x: x.similarity, reverse=True)

            return self.extract_synonyms(synonyms_result)

        except ValueError as err:
            print(err)
            return []
        except Exception as err:
            print(f"Unexpected error: {err}")
            return []

    def analyze_thesaurus_html(self, html, given_entry, target_pos):
        pattern = r'"entry":"(.*?)","pos":"(.*?)","synonyms":\[(.*?)\]'
        matches = re.findall(pattern, html)

        synonyms_result = []
        for idx, match in enumerate(matches, 1):
            entry, pos, synonyms = match
            entry = entry.split('"')[0]
            pos = pos.split('"')[0]

            if pos == target_pos:
                synonyms = synonyms.split('},{')
                for synonym in synonyms:
                    synonym_object = self.build_synonyms(synonym, entry, pos)
                    if synonym_object and synonym_object.term != given_entry:
                        synonyms_result.append(synonym_object)

        return synonyms_result

    def build_synonyms(self, string, entry, pos):
        pattern = r'"similarity":"(.*?)","isInformal":"(.*?)","isVulgar":"(.*?)","term":"(.*?)","targetTerm":"(.*?)",' \
                  r'"targetSlug":"(.*?)"'
        matches = re.findall(pattern, string)

        if matches:
            similarity, is_informal, is_vulgar, term, target_term, target_slug = matches[0]
            return Synonym(entry, term, pos, similarity, is_informal, is_vulgar)

    def extract_synonyms(self, synonyms_result):
        return [synonym.term for synonym in synonyms_result]

    def filter_synonyms(self, synonyms_result):
        filtered_synonyms = []
        for synonym in synonyms_result:
            if synonym.is_similar_enough(self.required_similarity):
                if self.include_informal or not synonym.is_informal:
                    if self.include_vulgar or not synonym.is_vulgar:
                        filtered_synonyms.append(synonym)
        return filtered_synonyms

    def get_synonyms_with_info(self, entry, pos):
        try:
            if not entry.strip():
                print("Provide a non-null input word")
                return []

            valid_pos = ['noun', 'verb', 'adjective', 'adverb']

            if pos not in valid_pos:
                raise ValueError(f"Invalid part of speech: {pos}")

            url = f'http://www.thesaurus.com/browse/{entry}'
            html = self.get_html(url)

            if not html:
                return []

            synonyms_result = self.analyze_thesaurus_html(html, entry, pos)
            synonyms_result = self.filter_synonyms(synonyms_result)
            synonyms_result.sort(key=lambda x: x.similarity, reverse=True)

            return self.extract_synonyms_with_info(synonyms_result)

        except ValueError as err:
            print(err)
            return []
        except Exception as err:
            print(f"Unexpected error: {err}")
            return []

    def extract_synonyms_with_info(self, synonyms_result):
        synonyms_info = []
        for synonym in synonyms_result:
            synonyms_info.append({
                'term': synonym.term,
                'pos': synonym.pos,
                'similarity': synonym.similarity,
                'is_informal': synonym.is_informal,
                'is_vulgar': synonym.is_vulgar
            })
        return synonyms_info
