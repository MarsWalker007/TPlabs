import time
import io

def kmp(text, pattern):
    n = len(pattern)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    
    m = len(text)
    j = 0
    count = 0
    contexts = []
    for i in range(m):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == n:
            count += 1
            context = text[max(0, i-n+1-10):min(m, i+1+10)]
            contexts.append(context)
            j = pi[j-1]
            
    return count, contexts

def naive(text, pattern):
    m = len(text)
    n = len(pattern)
    count = 0
    contexts =[]
    for i in range(m-n+1):
        if text[i:i+n] == pattern:
            count += 1
            context = text[max(0, i-10):min(m, i+n+10)]
            contexts.append(context)
            
    return count, contexts

if __name__ == '__main__':
    with open('war_and_peace.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    names = ['Анна Павловна', 'Пьер Безухов', 'Андрей Болконский',
             'Наташа Ростова', 'Николай Ростов', 'Илья Ростов']
    with io.open('results.txt', 'w', encoding='utf-8') as f:
        start_time = time.time()
        for name in names:
        
            count, contexts = kmp(text, name)
            kmp_time = time.time() - start_time
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-")
            f.write("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-" + "\n")
            print("----------------> Количество упоминаний героя", name, "(КМП):", count, " <----------------")
            f.write("----------------> Количество упоминаний героя " + name + "(КМП):" + str(count) + " <----------------" + "\n")
            print("----------------> Контексты упоминания героя", name, "(КМП):", " <----------------")
            f.write("----------------> Контексты упоминания героя " + name + "(КМП):" + " <----------------" + "\n")
            for context in contexts:
                print(context)
                f.write(context + "\n")

        
            count, contexts = naive(text, name)
            naive_time = time.time() - start_time
            
            print("----------------> Количество упоминаний героя", name, "(наивный алгоритм):", count, " <----------------")
            f.write("----------------> Количество упоминаний героя " + name + "(наивный алгоритм):" + str(count) + " <----------------" + "\n")
            print("----------------> Контексты упоминания героя", name, "(наивный алгоритм):", " <----------------")
            f.write("----------------> Контексты упоминания героя " + name + "(наивный алгоритм):" + " <----------------" + "\n")
            for context in contexts:
                print(context)
                f.write(context + "\n")

            print("----------------> Время выполнения (КМП):", kmp_time, " <----------------")
            f.write("----------------> Время выполнения (КМП): " + str(kmp_time) + " <----------------" + "\n")
            print("----------------> Время выполнения (наивный алгоритм):", naive_time, " <----------------")
            f.write("----------------> Время выполнения (наивный алгоритм): " + str(naive_time) + " <----------------" + "\n")
            print()
            f.write("\n")
