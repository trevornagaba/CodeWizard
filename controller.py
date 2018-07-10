import web
from Models import RegisterModel, LoginModel, PostContent

web.config.debug = False

urls = (
    "/", "Home",
    "/register", "Register",
    "/postregistration", "PostRegistration",
    "/login", "Login",
    "/checklogin", "CheckLogin",
    "/logout", "Logout",
    "/postactivity", "PostActivity",
    "/settings", "Settings",
    "/profile", "Profile"
)


app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={"user": None})
session_data = session._initializer


render = web.template.render("Views/Templates", base="MainLayout", globals = {"session":session_data, "current_user":session_data["user"]})


#ClassesRoutes


class Home:
    def GET(self):
        data = type("obj",(object,),{"username": "Jordan","password":"qwertyuiop"})
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect

        post_model = PostContent.PostContent()
        posts = post_model.get_all_posts()

        return render.Home(posts)


class Register:
    def GET(self):
        return render.Register()


class Login:
    def GET(self):
        return render.Login()


class Settings:
    def GET(self):
        return render.Settings()


class Profile:
    def GET(self):
        return render.Profile()


class PostRegistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.name


class CheckLogin:
    def POST(self):
        data = web.input()
        login_model = LoginModel.LoginModel()
        isCorrect = login_model.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect
            return isCorrect

        return "error"


class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']
        posted_content = PostContent.PostContent()
        posted_content.post_content(data)


class Logout:
    def GET(self):
        session["user"] = None
        session_data["user"] = None

        session.kill()
        return "success"


if __name__== "__main__":
    app.run()
