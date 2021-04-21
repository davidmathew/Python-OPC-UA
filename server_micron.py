from opcua import ua, uamethod, Server
from opcua.server.user_manager import UserManager
from time import sleep

#Create Database for User Credentials
users_db = {"admin":"qwerty@123"}
def user_manager(isession, username, password):
    isession.user = UserManager.User
    return username in users_db and password == users_db[username]

#Setting up OPC-UA Server
if __name__ == "__main__":
    server = Server()
    
    url = "opc.tcp://192.168.43.60:4848"
    server.set_endpoint(url)
    
    name = "OPC-UA Simulation Server"
    server.set_server_name(name)
    
    uri ="urn:CustomOPCUA_Server"
    idx = server.register_namespace(uri)
    
    server.set_application_uri(uri)
    
    server.set_security_policy([ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt])
    # load server certificate and private key. This enables endpoints
    # with signing and encryption.
    server.load_certificate("cert1.pem")
    server.load_private_key("key1.pem")

    
    policyIDs = ["Username"]
    server.set_security_IDs(policyIDs)
    server.user_manager.set_user_manager(user_manager)
    
    root_node = server.get_root_node()
    object_node = server.get_objects_node()
    
    inst1 = object_node.add_object(idx,"F10-1-F8T-SPCW3-SEP-00-TIT-101")
    inst2 = object_node.add_object(idx,"F10-1-F8T-SPCW3-SEP-00-TIT-102")
    inst3 = object_node.add_object(idx,"F10-1-F8T-SPCW3-SEP-00-PIT-101")
    inst4 = object_node.add_object(idx,"F10-1-F8T-SPCW3-SEP-00-PIT-102")
    
    
    V1 = inst1.add_variable("ns=5;s=DB_GW1.DB101.DBD8", "TIT101.PV" , 0 , ua.VariantType.Float)
    V2 = inst1.add_variable("ns=5;s=DB_GW1.DB101.DBD16", "TIT101.TV" , 0 , ua.VariantType.Float)
    V3 = inst2.add_variable("ns=5;s=DB_GW1.DB101.DBD26", "TIT102.PV" , 0 , ua.VariantType.Float)
    V4 = inst2.add_variable("ns=5;s=DB_GW1.DB101.DBD34", "TIT102.TV" , 0 , ua.VariantType.Float)
    
    
    V5 = inst3.add_variable("ns=5;s=DB_GW1.DB101.DBD566", "PIT101.PV" , 0 , ua.VariantType.Float)
    V6 = inst3.add_variable("ns=5;s=DB_GW1.DB101.DBD574", "PIT101.TV" , 0 , ua.VariantType.Float)
    V7 = inst4.add_variable("ns=5;s=DB_GW1.DB101.DBD584", "PIT102.PV" , 0 , ua.VariantType.Float)
    V8 = inst4.add_variable("ns=5;s=DB_GW1.DB101.DBD592", "PIT102.TV" , 0 , ua.VariantType.Float)
    
    #Set node as writable by clients. A node is always writable on server side
    V1.set_writable()
    V2.set_writable()
    V3.set_writable()
    V4.set_writable()
    
    V5.set_writable()
    V6.set_writable()
    V7.set_writable()
    V8.set_writable()

    server.start()
    print("starting the server on", format(url))
    
    while True:
        V1.set_value(0.25,ua.VariantType.Float)
        V8.set_value(0.25,ua.VariantType.Float)
        

