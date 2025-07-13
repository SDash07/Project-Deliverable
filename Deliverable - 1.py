from collections import defaultdict

class UserProductGraph:
    def __init__(self):
        self.user_items = defaultdict(set)
        self.item_users = defaultdict(set)

    def add_interaction(self, user, product):
        self.user_items[user].add(product)
        self.item_users[product].add(user)

    def get_user_items(self, user):
        return self.user_items[user]

    def get_similar_users(self, user):
        # Return list of users with at least one common item (excluding the user itself)
        return [u for u in self.user_items if u != user and self.user_items[u] & self.user_items[user]]

# Example usage:
if __name__ == "__main__":
    graph = UserProductGraph()
    graph.add_interaction('user1', 'productA')
    graph.add_interaction('user1', 'productB')
    graph.add_interaction('user2', 'productB')
    graph.add_interaction('user2', 'productC')
    graph.add_interaction('user3', 'productD')

    print("Items of user1:", graph.get_user_items('user1'))  # Output: {'productA', 'productB'}
    print("Items of user2:", graph.get_user_items('user2'))  # Output: {'productB', 'productC'}
    print("Items of user3:", graph.get_user_items('user3'))  # Output: {'productD'}

    similar_to_user1 = graph.get_similar_users('user1')
    print("Users similar to user1:", similar_to_user1)  # Output: ['user2'] because both share 'productB'
