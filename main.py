def main() -> None:
    path_to_file : str= r"books/frankenstein.txt"
    file_contents : str = get_book_content(path_to_file)
    word_count : int = get_num_words(file_contents)
    character_count : dict[str, int] = get_chr_count(file_contents)
    print_report(character_count, word_count)


def print_report(chr_count : dict[str, int], word_count : int) -> None:
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document", end="\n\n")

    sorted_dict : dict[str, int] = {k : v for k,v in sorted(chr_count.items(), key=lambda item: item[1], reverse=True)}

    for key, val in sorted_dict.items():
        if ord(key) in range(97, 123):
            print(f"The '{key}' character was found {val} times")

    print("--- End Report ---")



def get_chr_count(content : str) -> dict[str, int]:
    dict_chr_count : dict[str, int] = {}
    for chr in content:
        chr = chr.lower()
        if chr in dict_chr_count.keys():
            dict_chr_count[chr] += 1
        else:
            dict_chr_count[chr] = 1
    return dict_chr_count


def get_num_words(content : str) -> int:
    words : list[str] = content.split()
    return len(words)


def get_book_content(path : str) -> str:
   with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
