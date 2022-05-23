from transformers import pipeline
import sys
 # First line
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B') # Second line


def generate_text(text, length):
    
    res = generator(text, max_length=no_of_characters, do_sample=True, temperature=0.5) # Fourth line
    with open('gpttext.txt', 'w') as f:
        f.writelines(res[0]['generated_text'])


if __name__ == '__main__':
    text = sys.argv[1]
    no_of_characters = int(sys.argv[2])
