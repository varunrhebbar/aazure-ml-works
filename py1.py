from azureml.core import Workspace

ws = Workspace.get(name='mlworkspace',
                   subscription_id='6e99ca61-74f6-4e81-b1ae-3283db0a36cd',
                   resource_group='vaurnresource')

az ml computetarget list -g 'vaurnresource' -w 'mlworkspace'