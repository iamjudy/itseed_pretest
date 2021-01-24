import nltk
import re

file_name = "/Users/chanchu-ting/Desktop/python_data/text.txt"

lines_count = 0
lines_list = []
newList = []

with open(file_name, 'r', encoding="utf-8") as f:
    for line in f:
        lines_count = lines_count + 1
        match = re.findall(r'[^a-zA-Z0-9]+', line)
        for i in match:
            # 只留下英文單字
            line = line.lower()
            line = line.replace(i, ' ')
        lines_list = line.split()

        #print(lines_list)

# Create  bigrams
        tokens = nltk.word_tokenize(line)
        bgs = nltk.bigrams(tokens)

# compute frequency distribution for all the bigrams in the text
        fdist = nltk.FreqDist(bgs)
        for k, v in fdist.items():
            print(k, v)

        newList.append(fdist)
        #X = vector.fit_transform(newList)
        #df1 = pd.DataFrame(X.toarray(), columns=vector.get_feature_names())  # to DataFrame

    after_list = []
    while True:
        str = input('輸入單字，統計其在文本中 “ 後一個字 ” 的所有單字機率：') #找不到此單字則要求重新輸入
        str2 = str.lower()

        for section in newList:
            for name1, name2 in section:
                if str2 == name1:
                    after_list += [name2]
        myDict = nltk.FreqDist(after_list)
        for k, v in myDict.items():
            print(k, v/len(after_list))

