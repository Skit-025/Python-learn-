# read a file and print whether it contains a targeted word or not if word found print the line number
def find_word_in_file(file_path, target_word):
    try:
        with open(file_path,'r') as f:
            lines=f.readlines()
            L=[]
            for Lines in lines:
                L.append(Lines.lower())
            for i,line in enumerate(L ,start=1):
                if target_word in line:
                    print(f"Word '{target_word}' found in line {i}: {line.strip()}")
                    return
            print(f"Word '{target_word}' not found in the file.")
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
# Example usage
find_word_in_file(r"C:\Users\codes\Desktop\Times of india.txt", target_word=input("Enter the word to be searched: ").lower())