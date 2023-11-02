import tkinter as tk
from tkinter import ttk
from searcher import ThesaurusSearcher


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Thesaurus Searcher")

        # Load custom styles from styling.css
        style = ttk.Style()
        style.theme_use("alt")

        window_width = 500
        window_height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.resizable(False, False)

        self.entry_label = ttk.Label(root, text="Enter word:")
        self.entry_label.pack(padx=20, pady=10, anchor="w")
        self.entry_input = ttk.Entry(root)
        self.entry_input.pack(fill=tk.X, padx=20, pady=5)

        self.pos_label = ttk.Label(root, text="Select word type:")
        self.pos_label.pack(padx=20, pady=10, anchor="w")
        self.pos_var = tk.StringVar()
        self.pos_combobox = ttk.Combobox(root, textvariable=self.pos_var,
                                         values=["Noun", "Verb", "Adjective", "Adverb"], state="readonly")
        self.pos_combobox.pack(fill=tk.X, padx=20, pady=5)

        self.info_check_var = tk.IntVar()
        self.info_checkbutton = ttk.Checkbutton(root, text="Include additional info", variable=self.info_check_var)
        self.info_checkbutton.pack(padx=20, pady=10, anchor="w")

        self.search_button = ttk.Button(root, text="Search", command=self.search_synonyms)
        self.search_button.pack(padx=20, pady=20)

        self.result_label = ttk.Label(root, text="Synonyms:")
        self.result_label.pack(padx=20, pady=10, anchor="w")
        self.result_text = tk.Text(root, wrap=tk.WORD, font=("Arial", 10))
        self.result_text_scrollbar = ttk.Scrollbar(root, command=self.result_text.yview)
        self.result_text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=self.result_text_scrollbar.set)

        self.result_text.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

    def search_synonyms(self):
        entry = self.entry_input.get().strip()
        pos = self.pos_var.get().lower()

        if not entry:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please enter a word.")
            return

        thesaurus_searcher = ThesaurusSearcher(include_informal=bool(self.info_check_var.get()))

        if pos not in ['noun', 'verb', 'adjective', 'adverb']:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please select a valid word type.")
            return

        if self.info_check_var.get():
            synonyms = thesaurus_searcher.get_synonyms_with_info(entry, pos)
            if synonyms:
                self.result_text.delete(1.0, tk.END)
                for idx, synonym_info in enumerate(synonyms, 1):
                    self.result_text.insert(tk.END, f"{idx}. Term: {synonym_info['term']}, "
                                                    f"POS: {synonym_info['pos']}, "
                                                    f"Similarity: {synonym_info['similarity']}, "
                                                    f"Is Informal: {synonym_info['is_informal']}, "
                                                    f"Is Vulgar: {synonym_info['is_vulgar']}\n")
            else:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, "No synonyms found for the given word and word type.")
        else:
            synonyms = thesaurus_searcher.get_synonyms(entry, pos)
            if synonyms:
                self.result_text.delete(1.0, tk.END)
                for idx, synonym in enumerate(synonyms, 1):
                    self.result_text.insert(tk.END, f"{idx}. {synonym}\n")
            else:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, "No synonyms found for the given word and word type.")


def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
