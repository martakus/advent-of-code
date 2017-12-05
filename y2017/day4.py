def check_passphrase(s):
    words = s.split()
    return len(words) == len(set(words))


def check_anagram_passphrase(s):
    words = [''.join(sorted(i)) for i in s.split()]
    return len(words) == len(set(words))


if __name__ == '__main__':
    with open('inputs/input4.txt') as f:
        phrases = f.read().strip()
        counter = 0
        for phrase in phrases.split('\n'):
            if check_passphrase(phrase):
                counter += 1
        print counter
        counter = 0
        for phrase in phrases.split('\n'):
            if check_anagram_passphrase(phrase):
                counter += 1
        print counter
