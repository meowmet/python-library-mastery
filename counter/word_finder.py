from collections import Counter
import pydoc

def load_wordlist(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        words = []
        for line in f:
            w = line.strip().strip('"').lower()
            if w.isalpha():
                words.append(w)
        return words

def find_possible_words(letters, wordlist):
    letters_count = Counter(letters)
    possibles = []
    for word in wordlist:
        wc = Counter(word)
        if all(wc[ch] <= letters_count.get(ch, 0) for ch in wc):
            possibles.append(word)
    return possibles

def main():
    wordlist = load_wordlist("wordlist.txt") 
    while True:
        print("\nOptions:")
        print("1. Show possible words in terminal")
        print("2. Save possible words to 'matches.txt'")
        print("3. Page through possible words")
        print("Type 'exit' (or 'quit') to quit.")
        choice = input("\nEnter your choice (1/2/3): ").strip().lower()

        if choice == "1":
            letters = input("Enter your letters: ").lower()
            matches = sorted(find_possible_words(letters, wordlist), key=len)
            print(f"\nWords that can be formed from '{letters}':")
            for w in matches:
                print(w)

        elif choice == "2":
            letters = input("Enter your letters: ").lower()
            matches = sorted(find_possible_words(letters, wordlist), key=len)
            with open("matches.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(matches))
            print(f"{len(matches)} words saved to 'matches.txt'.")

        elif choice == "3":
            letters = input("Enter your letters: ").lower()
            matches = sorted(find_possible_words(letters, wordlist), key=len)
            if not matches:
                print("No matches found.")
            else:
                pydoc.pager("\n".join(matches))

        elif choice in ("exit", "quit"):
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, 3, or 'exit'.")

if __name__ == "__main__":
    main()
