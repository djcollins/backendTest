from nameko.rpc import rpc
import dahuffman
codec=dahuffman.load_shakespeare()

class Microservice:
    name = "micro_service"
    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)
    @rpc
    def encode_strings(self,str_list):
        string_encoded={}
        for string in str_list: 
            string_encoded[s]=codec.encode(s)
        return string_encoded[s]
    @rpc
    def decode_string(self,s):
        return codec.decode(s)
    @rpc
    def square_odd(self, num_list):
        return [x**2 for x in num_list]
    #encode_string_list =lambda xs: {x:this.encode_string(x) for x in xs}
