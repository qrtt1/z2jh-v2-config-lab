from jupyterhub.auth import DummyAuthenticator
from oauthenticator.generic import GenericOAuthenticator
from traitlets.config.loader import Config


class MyAuthenticator(GenericOAuthenticator):

    async def pre_spawn_start(self, user, spawner):
        print("run pre_spawn_start")
        super().pre_spawn_start(user, spawner)


class MyDummyAuthenticator(DummyAuthenticator):

    async def pre_spawn_start(self, user, spawner):
        print("run pre_spawn_start", user, spawner)
        spawner.environment['XDXDXD'] = "ABC"
        super().pre_spawn_start(user, spawner)


def execute(c: Config):
    # c.JupyterHub.log_level = 'DEBUG'
    print("my customization is executed in the hub pod")

    # c.JupyterHub.authenticator_class = MyAuthenticator
    c.JupyterHub.authenticator_class = MyDummyAuthenticator


if "c" in locals():
    execute(locals()["c"])
