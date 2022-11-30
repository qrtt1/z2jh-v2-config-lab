This repoistory is a development evironment for [Arbitrary extra code and configuration in jupyterhub_config.py](https://z2jh.jupyter.org/en/stable/administrator/advanced.html#arbitrary-extra-code-and-configuration-in-jupyterhub-config-py)

## A lab for customization z2jh

Steps:
1. create `hub` namespace if needed
2. install `my-hub` chart 
3. install z2jh

### Details

Create the hub namespace

```
kubectl create namespace hub
```

install `my-hub` chart

```
./customize.sh
```

install `z2jh` chart

```
./install.sh
```

### Check the customization 

```bash
$ kubectl -n hub logs deploy/hub | head
Loading /usr/local/etc/jupyterhub/secret/values.yaml
No config at /usr/local/etc/jupyterhub/existing-secret/values.yaml
Loading extra config: primehub_config_main.py
my customization is executed in the hub pod
[I 2022-11-30 01:49:06.606 JupyterHub app:2775] Running JupyterHub version 3.0.0
[I 2022-11-30 01:49:06.606 JupyterHub app:2805] Using Authenticator: jupyterhub.auth.DummyAuthenticator-3.0.0
[I 2022-11-30 01:49:06.606 JupyterHub app:2805] Using Spawner: kubespawner.spawner.KubeSpawner-4.2.0
```

This line is put by our python script:

```
my customization is executed in the hub pod
```

### Check the hub

Make a port-forward at `http://127.0.0.1:8080`

```
kubectl --namespace=hub port-forward service/proxy-public 8080:http
```