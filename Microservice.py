#Daniel Collins 
from nameko.rpc import rpc
from dahuffman import load_shakespeare
codec=load_shakespeare()
encoded_strings={} #the dictionary of string: compressed string
encoded_string_to_string={} #dictionary of compressed string bytes as a string : the bytes
class Microservice:
    #Standard python microservice class
    name = "micro_service"
    @rpc
    def encode_strings(self,str_list):

        for string in str_list:
            #adding the encoded string to a dictionary, the key is the string, the value is the compressed string
            encoded_strings[string]=codec.encode(string)
            encoded_string_to_string[str(encoded_strings[string])]=encoded_strings[string]
        return str(encoded_strings)
    @rpc
    def decode_string(self,string):
        return str(codec.decode(encoded_string_to_string[string])) #because terminal doesn't usually allow bytes
    @rpc
    def square_odd(self, num_list):
        return [x*x if x%2==1 else x for x in num_list]


#a case for each function
a=Microservice()
print(a.encode_strings(["Daniel","Is","Cool", "is" , "Is"]))
print(a.square_odd([1,2,3,4,5,6,7,8,9,10]))
print(a.decode_string("b'\\xfa _\\xa4'"))



