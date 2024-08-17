import hvac
import yaml
import argparse

def get_env_from_vault(vault_url, token, secret_path):
    client = hvac.Client(url=vault_url, token=token)
    secret = client.secrets.kv.v2.read_secret_version(path=secret_path)
    return secret['data']['data']

def update_values_yaml(env_vars, values_path):
    with open(values_path, 'r') as values_file:
        values = yaml.safe_load(values_file)

    values['env'] = env_vars

    with open(values_path, 'w') as values_file:
        yaml.safe_dump(values, values_file)

if __name__ == "__main__":
    try: 
        parser = argparse.ArgumentParser(description='Update values.yaml with environment variables from Vault')
        parser.add_argument('--vault_url', required=True, help='URL of the Vault server')
        parser.add_argument('--token', required=True, help='Vault token')
        parser.add_argument('--secret_path', required=True, help='Path to the secret in Vault')
        parser.add_argument('--values_path', required=True, help='Path to the values.yaml file')

        args = parser.parse_args()

        env_vars = get_env_from_vault(args.vault_url, args.token, args.secret_path)
        update_values_yaml(env_vars, args.values_path)
        print(f"Updated {args.values_path} with environment variables from {args.secret_path}")
    except Exception as e:
        print(f"Error: {e}")
