class Blog:
    def __init__(self):
        self.users =[]
        self.posts = []
        self.current_user = None
        
    def create_new_user(self):
        username = input('Please enter a username: ')
        password = input("Please enter a password: ")
        new_user = User(username, password)
        self.users.append(new_user)
        print(f"{new_user} has been created.")
    
    def log_user_in(self):
        username = input("What is your username? ")
        password = input("What is your password? ")
        for user in self.users:
            if username == user.username and user.check_password(password):
                self.current_user = user 
                print(f"{user} has been logged in")
                break
            else:
                print("Username and/or Password is incorrect")

    def log_user_out(self):
        self.current_user = None
        print("You have successfully logged out.")

    def create_a_post(self):
        if self.current_user:
            title = input("what would you like to title your post? ")
            body = input("What is the body of your post? ")
            new_post = Post(title, body, self.current_user)
            self.posts.append(new_post)
            print(f"{new_post.title} has been created. ")
        else: 
            print("You must be logged in to perform this action. ")

    def view_posts(self):
        if self.posts:
            for post in self.posts:
                print(post)
        else:
            print("There are currently no posts for this blog :(")
        
class User:
    
    id_counter = 1 
    
    def __init__(self, username, password):
        self.id = User.id_counter              # Assign title to id and show list in option to access posts 
        User.id_counter += 1 
        self.username = username 
        self.password = password
        self.posts = [] 
        
    def __str__(self):
        return self.username
        
    def __repr__(self):
        return f"User {self.id} | {self.username}>"
    
    def check_password(self, password):
        return self.password == password
            
    
        
class Post:
    id_counter = 1

    def __init__(self, title, body, author):
        # Docstring (for developers in the future)
        """
        PARAMS: 
        title  -> Str
        body   -> Str
        author -> User
        """

        self.id = Post.id_counter
        Post.id_counter += 1
        self.title = title
        self.body = body
        self.author = author

    def __str__(self):
        formatted_post = f"""
        {self.id} - {self.title.title()}
        By: {self.author}
        {self.body}
        """

        return formatted_post

def run_blog():
    # create an instance of the Blog Class 
    my_blog = Blog()
    while True:
        if not my_blog.current_user:
            print("1. Sign up\n2. Log In\n3. View All Posts\n4. Quit")
            to_do = input("Which option which you like to do? ")
            while to_do not in {'1', '2', '3', '4'}:
                to_do = input("Please choose either 1, 2, 3, or 4: ")
            if to_do == '4':
                break
            elif to_do == '1':
                my_blog.create_new_user()
            elif to_do == '2':
                my_blog.log_user_in()
            elif to_do == '3':
                my_blog.view_posts()
        else:
            print("1. Log Out\n2. Create a Post\n3. View all Posts\n4. Quit")
            to_do = input("Which option would you like to do? ")
            while to_do not in {'1', '2', '3', '4'}:
                to_do = input("Please choose 1, 2, 3 or 4 ")
            if to_do == '1':
                my_blog.log_user_out()
            elif to_do == '2':
                my_blog.create_a_post()
            elif to_do == '3':
                my_blog.view_posts()   
            elif to_do == '4':
                my_blog.log_user_out()
                print("Deleting myself. Goodbye.")
                break
run_blog()