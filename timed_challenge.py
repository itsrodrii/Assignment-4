# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 3. Remove Duplicates (Keep Order)
# Return the values in the order they first appeared, without duplicates.
# Input: ["apple", "banana", "apple", "kiwi", "banana"]
# Output: ["apple", "banana", "kiwi"]

def remove_duplicates_keep_order(values):
    """
    I used a set to remember which items already showed up and a list to keep the order. 
    Each item is checked once, and if it’s new, it goes into the result list. 
    This way the output has no repeats but stays in the same order.
    """
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


print(remove_duplicates_keep_order(["apple", "banana", "apple", "kiwi", "banana"]))



"""
For the timed problem I solved the problem of getting rid of duplicates but preserving the original order. 
I decided to use a set and a list together. The set helps me remember what I've already come across, 
and the list helps me keep everything in the proper order. This appeared to be the easiest way of doing 
it without having to resort to writing extra checks or spending too much time.

The time limit definitely made me pick the simplest solution that I could think of instead of completely 
trying out different options. To begin with, I thought I would just use a list, but this would mean reading 
the list every time that I was adding new information, which would take time. Because the timer was set, 
I did not want to waste valuable minutes on a more time-consuming or complicated approach. Choosing a set 
to provide for fast lookups was sensible and easy to write down in a hurry.

One compromise in doing so is that a set doesn't keep things in order by itself, so I also needed to have 
the list. That means that I had to work with two structures instead of one. However, the payoff was well 
worth it because the solution still kept simplicity and clarity. Overall, I think I made the right choice 
in a pinch: it works, it's effective, and it was easy to finish on time.
"""
