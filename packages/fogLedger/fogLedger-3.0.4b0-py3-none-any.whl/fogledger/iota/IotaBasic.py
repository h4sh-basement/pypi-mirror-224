from fogbed import (
    Container, VirtualInstance, FogbedExperiment
)
from .NodeConfig import NodeConfig
from .CoordConfig import CoordConfig
from .SpammerConfig import SpammerConfig
from .ApiConfig import ApiConfig
from .WebAppConfig import WebAppConfig
from typing import List
from typing import Dict
import os
import json
import time
import subprocess
import pkg_resources


class IotaBasic:
    def __init__(
        self,
        exp: FogbedExperiment,
        prefix: str = 'cloud',
        conf_nodes: List[NodeConfig] = [],
        conf_coord: CoordConfig = None,
        conf_spammer: SpammerConfig = None,
        conf_api: ApiConfig = None,
        conf_web_app: WebAppConfig = None
    ) -> None:
        self.ledgers: List[VirtualInstance] = []
        self.nodes: Dict[str, Container] = {}
        self.api:Container
        self.exp = exp
        self.prefix = prefix
        self.conf_nodes = conf_nodes
        self.conf_coord = conf_coord
        self.conf_spammer = conf_spammer
        self.conf_api = conf_api
        self.conf_web_app = conf_web_app
        self.web_app:Container
        self.coo_public_key:str
        self.installPrivateTangle()
        self.createContainers()

    def add_ledger(self, prefix: str):
        ledger = self.exp.add_virtual_instance(f'{prefix}')
        self.ledgers.append(ledger)
        return ledger

    def _create_node(self, ledger: VirtualInstance, node:Container):
        self.exp.add_docker(
            container=node,
            datacenter=ledger)
        self.nodes[f'{self.prefix}_{ledger.label}_{node.name}'] = node
        return node

    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def installPrivateTangle(self):
        print("install tangle")
        path_script = pkg_resources.resource_filename('fogledger', 'data')
        #path_script = os.path.abspath('data')
        path_private_tangle = os.path.join(path_script, "private-tangle.sh")
        subprocess.run(["chmod", "+x", path_private_tangle])
        subprocess.run(["/bin/bash", path_private_tangle, "install"], check=True, cwd=path_script)
        print("finished script...")

    def createContainers(self):
        ### NODES ###
        for index, node_conf in enumerate(self.conf_nodes):
            name = node_conf.name
            ip = node_conf.ip
            port_bindings = node_conf.port_bindings
            
            node = Container(
                name=name,
                dimage='larsid/fogbed-iota-node:v3.0.4-beta',
                ip=ip,
                port_bindings=port_bindings,
                ports=['14265', '8081', '1883', '15600', '14626/udp']
            )
            ledger = self.add_ledger(f'ledger-{name}{index}')
            self._create_node(ledger,node)

        ### COO ###
        coo = Container(
            name=self.conf_coord.name,
            ip = self.conf_coord.ip,
            port_bindings = self.conf_coord.port_bindings,
            dimage='larsid/fogbed-iota-node:v3.0.4-beta',
            environment={'COO_PRV_KEYS': ''},
            ports=['15600']
        )
        ledger = self.add_ledger(f'ledger-{coo.name}')
        self._create_node(ledger,coo)

        ### spammer ###
        spammer = Container(
            name= self.conf_spammer.name,
            ip = self.conf_spammer.ip,
            port_bindings = self.conf_spammer.port_bindings,
            dimage='larsid/fogbed-iota-node:v3.0.4-beta',
            ports=['15600', '14626/udp']
        )
        ledger = self.add_ledger(f'ledger-{spammer.name}')
        self._create_node(ledger,spammer)

        ### API ###
        api = Container(
            name= self.conf_api.name,
            ip = self.conf_api.ip,
            port_bindings = self.conf_api.port_bindings,
            dimage='larsid/fogbed-iota-api:v3.0.4-beta',
            ports=['4000']
        )
        ledger = self.add_ledger(f'ledger-{api.name}')
        self.exp.add_docker(
            container=api,
            datacenter=ledger)
        self.api = api

        ### WebApp ###
        web_app = Container(
            name= self.conf_web_app.name,
            ip = self.conf_web_app.ip,
            port_bindings = self.conf_web_app.port_bindings,
            dimage='larsid/fogbed-iota-web-app:v3.0.4-beta',
            ports=['4200']
        )
        ledger = self.add_ledger(f'ledger-{web_app.name}')
        self.exp.add_docker(
            container=web_app,
            datacenter=ledger)
        self.web_app = web_app

    def searchNode(self, node_name: str):
        for node in self.nodes.values():
            if node.name == node_name:
                return node
    
    def configureApi(self):
        print("\nConfiguring api...")
        file_path = os.path.join("/tmp", "iota")
        config_file_network_api = json.loads(IotaBasic.read_file(f"{file_path}/config/my-network.json"))
        config_file_api = json.loads(IotaBasic.read_file(f"{file_path}/config/api.config.local.json"))
        node_name = self.conf_nodes[0].name
        node = self.searchNode(node_name)
        if(self.coo_public_key is not None):
            config_file_network_api["coordinatorAddress"] = self.coo_public_key
            config_file_network_api["provider"] = f"http://{node.ip}:14265"
            config_file_network_api["feedEndpoint"] = f"mqtt://{node.ip}:1883"
            updated_data_config_file = json.dumps(config_file_network_api)
            self.api.cmd(f"mkdir -p /app/data/.local-storage/network")
            self.api.cmd(f"echo \'{updated_data_config_file}\' | jq . > /app/data/.local-storage/network/private-network.json")
            self.api.cmd(f"echo \'{json.dumps(config_file_api)}\' | jq . > /app/src/data/config.local.json")
        print("Api configured! ✅")

    def configureWebApp(self):
        print("\nConfiguring web app...")
        file_path = os.path.join("/tmp", "iota")
        config_file_api = json.loads(IotaBasic.read_file(f"{file_path}/config/api.config.local.json"))
        config_file_web_app = json.loads(IotaBasic.read_file(f"{file_path}/config/webapp.config.local.json"))
        self.web_app.cmd("mkdir -p /app/api/src/data")
        self.web_app.cmd("mkdir -p /app/client/src/assets/config")
        self.web_app.cmd(f"echo \'{json.dumps(config_file_api)}\' | jq . > /app/api/src/data/config.local.json")
        self.web_app.cmd(f"echo \'{json.dumps(config_file_web_app)}\' | jq . > /app/client/src/assets/config/config.local.json")
        self.web_app.cmd(f"mv /app/public/env.js.template /app/public/env.js")
        self.web_app.cmd(f"echo 'window.env = {{API_ENDPOINT: \"http://{self.api.ip}:4000/\"}};' > ./public/env.js")
        self.web_app.cmd(f"rm app/client/package-lock.json")
        print("WebApp configured! ✅")

    def configureNodes(self):
        print("\nConfiguring nodes...")
        file_path = os.path.join("/tmp", "iota")
        config_file_coor = json.loads(IotaBasic.read_file(f"{file_path}/config/config-coo.json"))
        config_file_spammer = json.loads(IotaBasic.read_file(f"{file_path}/config/config-spammer.json"))
        config_file_node = json.loads(IotaBasic.read_file(f"{file_path}/config/config-node.json"))
        for node in self.nodes.values():
            json_data = {}
            if(node.name == self.conf_coord.name):
                json_data = config_file_coor
                json_data["coordinator"]["interval"] = self.conf_coord.interval
            elif(node.name == self.conf_spammer.name):
                json_data = config_file_spammer
                json_data["spammer"]["message"] = self.conf_spammer.message
            else:
                json_data = config_file_node
            json_data["node"]["alias"] = node.name
            updated_data = json.dumps(json_data)
            node.cmd(f"echo \'{updated_data}\' | jq . > /app/config.json")
        print("Nodes configured! ✅")

    # P2P identities are generated for each node
    def setupIdentities(self):
        print("\nGenerating P2P identities for each node")
        for node in self.nodes.values():
            node.cmd(f'./hornet tool p2pidentity-gen > {node.name}.identity.txt')
        print("P2P identities generated! ✅")

    # Extracts the peerID from the identity file
    def extractPeerID(self):
        print("\nExtracting peerID from the identity file")
        for node_ext in self.nodes.values():
            peerID = node_ext.cmd(
                f'cat {node_ext.name}.identity.txt | awk -F : \'{{if ($1 ~ /PeerID/) print $2}}\' | sed "s/ \+//g" | tr -d "\n" | tr -d "\r"').strip("> >")
            for node_int in self.nodes.values():
                if node_int.name != node_ext.name:
                    json_data = node_int.cmd(f'cat /app/peering.json').strip("> >")
                    json_data = json.loads(json_data)
                    json_data["peers"].append({"alias": node_ext.name, "multiAddress": f"/dns/{node_ext.ip}/tcp/15600/p2p/{peerID}"})
                    updated_data = json.dumps(json_data)
                    node_int.cmd(f"echo \'{updated_data}\' | jq . > /app/peering.json")
        print("peerID extracted! ✅")

    # Sets the Coordinator up by creating a key pair
    def setupCoordinator(self):
        print("\nSetting up the Coordinator")
        coo_key_pair_file = "coo-milestones-key-pair.txt"
        coo = self.searchNode(self.conf_coord.name)
        if coo is not None:
            coo.cmd('mkdir -p /app/coo-state')
            coo.cmd(f'./hornet tool ed25519-key > {coo_key_pair_file}')
            COO_PRV_KEYS = coo.cmd(
                f'cat {coo_key_pair_file} | awk -F : \'{{if ($1 ~ /private key/) print $2}}\' | sed "s/ \+//g" | tr -d "\n" | tr -d "\r"').strip("> >")
            coo.cmd(f'export COO_PRV_KEYS={COO_PRV_KEYS}')
            self.coo_public_key = coo.cmd(
                f'cat {coo_key_pair_file} | awk -F : \'{{if ($1 ~ /public key/) print $2}}\' | sed "s/ \+//g" | tr -d "\n" | tr -d "\r"').strip("> >")
            file_path = os.path.join("/tmp", "iota")
            command = f'echo {self.coo_public_key} > {file_path}/coo-milestones-public-key.txt'
            os.system(command)
            for node in self.nodes.values():
                json_data = node.cmd(f'cat /app/config.json').strip("> >")
                json_data = json.loads(json_data)
                json_data["protocol"]["publicKeyRanges"][0]["key"] = self.coo_public_key
                updated_data = json.dumps(json_data)
                node.cmd(f"echo \'{updated_data}\' | jq . > /app/config.json")
            print("Coordinator set up! ✅")
        else:
            print("Coordinator not found! ❌")

    def copySnapshotToNodes(self):
        print("\nCopying snapshot to each node")
        # Executar o comando base64 no arquivo full_snapshot.bin e capturar a saída
        file_path = os.path.join("/tmp", "iota", "snapshots", "private-tangle","full_snapshot.bin")
        command = f"base64 {file_path}"
        output = subprocess.run(command, capture_output=True, text=True, shell=True).stdout
        # Salvar a saída em uma variável
        output_b64 = output.strip()
        for node in self.nodes.values():
            node.cmd("mkdir -p /app/snapshots/private-tangle")
            node.cmd(f"echo '{output_b64}' | base64 -d > /app/snapshots/private-tangle/full_snapshot.bin")

        print("Snapshot copied! ✅")

    # Bootstraps the coordinator
    def bootstrapCoordinator(self):
        print("Bootstrapping the Coordinator...")
        # Need to do it again otherwise the coo will not bootstrap
        coo = self.searchNode(self.conf_coord.name)
        if coo is not None:
            coo.cmd(
                f'./hornet --cooBootstrap --cooStartIndex 0 > coo.bootstrap.log &')
            print("Waiting for $bootstrap_tick seconds ... ⏳")
            time.sleep(30)
            bootstrapped = coo.cmd(
                'grep "milestone issued (1)" coo.bootstrap.log | cat')
            if (bootstrapped):
                print("Coordinator bootstrapped successfully! ✅")
                coo.cmd(f'pkill -f "hornet --cooBootstrap --cooStartIndex 0"')
                coo.cmd('rm ./coo.bootstrap.container')
                time.sleep(10)
            else:
                print("Error. Coordinator has not been boostrapped.")
        else:
            print("Coordinator not found! ❌")

    def startContainers(self):
        print("\nStarting the containers...")
        for node in self.nodes.values():
            node.cmd(f'./hornet > {node.name}.log &')
            print(f"\nStarting {node.name}... ⏳")
            time.sleep(3)
            print(f"{node.name} is up and running! ✅")
        print(f"\nStarting {self.api.name}... ⏳")
        self.api.cmd(f'npm install && npm run build-compile && npm run build-config && npm prune --production && node dist/index &')
        print(f"{self.api.name} is up and running! ✅")
        print(f"\nStarting {self.web_app.name}... ⏳")
        self.web_app.cmd(f'npm run build && nginx -g "daemon off;" &')
        print(f"{self.web_app.name} is up and running! ✅")

    def start_network(self):
        print("\nStarting the network...")
        self.configureNodes()
        self.setupIdentities()
        self.extractPeerID()
        self.copySnapshotToNodes()
        self.setupCoordinator()
        self.bootstrapCoordinator()
        self.configureApi()
        self.configureWebApp()
        self.startContainers()
        print("Network is up and running! ✅")
