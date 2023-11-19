def get_topic_from_file():
    with open('resources\index.txt', 'r') as index_file:
        current_index = int(index_file.readline().strip())

    with open('resources\\topics.txt', 'r', encoding='utf-8') as topics_file:
        topics = topics_file.readlines()
        current_topic = topics[current_index - 1].strip() if 1 <= current_index <= len(topics) else None

    new_index = current_index + 1

    with open('resources\index.txt', 'w') as index_file:
        index_file.write(str(new_index))

    return current_topic
