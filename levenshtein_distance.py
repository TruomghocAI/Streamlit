import streamlit as st

def load_vocab(data_file):
    with open(data_file, 'r') as f:
        lines = f.readlines()
    word = sorted(set([line.strip().lower() for line in lines]))
    return word
vocabulary = load_vocab('C:\\Users\\admin\\OneDrive\\Documents\\Streamlit\\Streamlit\\data\\vocab.txt')


def levenshtein_distance(s1, s2):
        m, n = len(s1), len(s2)
        distance = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            distance[i][0] = i
        for j in range(n + 1):
            distance[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0 if s1[i - 1] == s2[j - 1] else 1
                distance[i][j] = min(
                    distance[i - 1][j] + 1,
                    distance[i][j - 1] + 1,
                    distance[i - 1][j - 1] + cost
                )
        return distance[len(s1)][len(s2)]

def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word :')
    if st.button (" Compute ") :
        leven_distances = dict ()
        for vocab in vocabulary:
            leven_distances[vocab] = levenshtein_distance (word,vocab)
        sorted_distences = dict (sorted(leven_distances.items(), key = lambda item :item [1]))
        correct_word = list ( sorted_distences . keys () ) [0]
        st.write ('Correct word : ', correct_word )
        col1 , col2 = st . columns (2)
        col1.write('Vocabulary :')
        col1.write (vocabulary)
        
        col2.write('Distances :')
        col2.write( sorted_distences )

if __name__ == '__main__':
    main()
        