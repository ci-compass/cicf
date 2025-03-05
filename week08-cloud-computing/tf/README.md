1. To use this configuration, set some environment variables:

```bash
export TF_VAR_do_token="dop_v1_xxxxxx"
export TF_VAR_do_spaces_access_id="DO00xxxyyy"
export TF_VAR_do_spaces_secret_key="xyzxyzxyz"
```

2. Then run the OpenTofu commands:

```bash
tofu init
tofu plan -out tofu.plan
tofu apply tofu.plan
```

3. To destroy infra created previously, do:

```bash
tofu destroy
```
