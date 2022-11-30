helm upgrade --cleanup-on-fail \
  --install zlab jupyterhub/jupyterhub \
  --namespace hub \
  --version=2.0.0 \
  --values config.yaml
