helm upgrade --cleanup-on-fail \
  --install zlab /Users/qrtt1/temp/primehub/modules/primehub/vendor/zero-to-jupyterhub-k8s/jupyterhub \
  --namespace hub \
  --values config.yaml
