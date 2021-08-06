c = get_config()
c.CourseDirectory.course_id = '*'
c.Exchange.timezone = 'Hongkong'
c.Exchange.path_includes_course = True

# Without kubernetes
# from nbgrader.auth import JupyterHubAuthPlugin
# c.Authenticator.plugin_class = JupyterHubAuthPlugin

# With kubernetes
# from ngshare_exchange import configureExchange
# configureExchange(c, 'http://ngshare1:8080/services/ngshare')