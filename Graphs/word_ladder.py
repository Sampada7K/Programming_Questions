import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList.append(beginWord)
        # print(wordList)

        bucket_dict = {}
        for word in wordList:
            for index, char in enumerate(word):
                bucket = word[:index] + "_" + word[index + 1:]
                if bucket in bucket_dict:
                    bucket_dict[bucket].append(word)
                else:
                    bucket_dict[bucket] = [word]

                    # print(bucket_dict)
        word_dict = {}
        for bucket in bucket_dict:
            connected_words = bucket_dict[bucket]
            if len(connected_words) > 1:
                for word1 in connected_words:
                    for word2 in connected_words:
                        if word1 != word2:
                            if word1 in word_dict:
                                word_dict[word1].append(word2)
                            else:
                                word_dict[word1] = [word2]

        # print(word_dict)

        q = [(beginWord, 1)]
        visited = {beginWord}
        print(q)

        while len(q) > 0:
            begin_word, ladder_length = q.pop(0)
            connected = word_dict[begin_word]
            for connection in connected:
                if connection == endWord:
                    return ladder_length + 1
                if connection not in visited:
                    visited.add(connection)
                    q.append((connection, ladder_length + 1))
        return 0





