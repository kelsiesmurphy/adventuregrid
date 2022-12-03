from models.experience import Experience
from models.user import User
from models.users_experiences import Users_Experiences

import repositories.experience_repository as experience_repository
import repositories.user_repository as user_repository
import repositories.users_experience_repository as users_experience_repository


user1  = User("John Jones", "johnjones987", "johnjones@email.com")
user_repository.save(user1)

user2  = User("Jaida Shōta", "jaidashota453", "jaidashota@email.com")
user_repository.save(user2)

user3  = User("Viktor Atanasio", "viktoratan202", "viktoratan@email.com")
user_repository.save(user3)

user4  = User("Anni Eskil", "annieskil245", "annieskil@email.com")
user_repository.save(user4)


experience1 = Experience("The Highland Trail", "Take in the Scottish highlands as you travel on the Jacobite Steam Train over the Glenfinnan Viaduct.", "West Highlands, Scotland", "https://ibb.co/WGv6L8b", 5, False)
experience_repository.save(experience1)

experience2 = Experience("Obscure Edinburgh", "From the old town of Edinburgh to the hidden gems of Leith, explore the city and learn about its rich history.", "Edinburgh, Scotland", "https://ibb.co/Q8zMZN2", 5, True)
experience_repository.save(experience2)

experience3 = Experience("The Devils Pulpit", "Get your boots on and stay safe as you explore this deep sandstone gorge hidden in the middle of a forest", "Loch Lomond, Scotland", "https://ibb.co/6RbM5qg", 5, False)
experience_repository.save(experience3)

experience4 = Experience("Glencoe Valley", "Carved out centuries ago by icy glaciers and volcanic explosions, Glencoe is a beautiful place to explore.", "Glencoe, Scotland", "https://ibb.co/5v4z33v", 5, False)
experience_repository.save(experience4)

experience5 = Experience("Hidden Glasgow", "From the Glasgow Necropolis to the life of the Glasgow architect Charles Rennie Mackintosh, there's plenty to do in Glasgow.", "Glasgow, Scotland", "https://ibb.co/JzGNbSM", 0, False)
experience_repository.save(experience5)

experience6 = Experience("Skye's Secret", "Skye is a truly magical place to visit and home to some of Scotland’s most inspiring landscapes. A land of mystery, intrigue and natural beauty, Skye is a fantastic place to spend some time in Scotland.", "Skye, Scotland", "https://ibb.co/bQ3Qqrj", 5, False)
experience_repository.save(experience6)