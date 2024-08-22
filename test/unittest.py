def extract_topics(data):
    lines = data.split("\n")
    topics = set()
    
    for line in lines:
        # Assuming topics are the ones that appear multiple times and have more than one word
        if line.strip() and len(line.split()) > 1:
            topics.add(line.strip())
    
    return list(topics)

# Example usage
data = """
Trans Express Services Lanka
No
Date
Waybill 
Id
Customer Name
Phone 
Number
Address
COD
Delivery 
Progress
Rider Name
1
2024-
08-22
41722772
Ramani Renuka 
Hettiarachchi
...
"""

topics = extract_topics(data)
print(topics)
