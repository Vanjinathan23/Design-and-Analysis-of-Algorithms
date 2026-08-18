def string_matching(words):
    result = []

    for i, word in enumerate(words):
        for j, other in enumerate(words):
            if i != j and word in other:
                result.append(word)
                break

    return result

test_cases = [
    ["mass", "as", "hero", "superhero"],
    ["leetcode", "et", "code"],
    ["blue", "green", "bu"]
]

for words in test_cases:
    print("Input:", words)
    print("Output:", string_matching(words))
    print()
