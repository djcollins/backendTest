from nameko.rpc import rpc
import dahuffman
codec=dahuffman.load_shakespeare()
encoded_strings={} #the dictionary of string: compressed string
encoded_string_to_string={} #dictionary of compressed string bytes as a string : the bytes
class Microservice:
    
    name = "micro_service"
    @rpc
    def hello(self, name):#From a tutorial. thought I'd leave it here
        return "Hello, {}!".format(name)
    @rpc
    def encode_strings(self,str_list):

        for string in str_list:
            #adding the encoded string to a dictionary, the key is the string, the value is the compressed string
            encoded_strings[string]=codec.encode(string)
            encoded_string_to_string[str(encoded_strings[string])]=encoded_strings[string]
        return str(encoded_strings)
    @rpc
    def decode_string(self,s):
        return str(codec.decode(encoded_string_to_string[s]))
    @rpc
    def square_odd(self, num_list):
        return [x*x if x%2==1 else x for x in num_list]



