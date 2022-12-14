from abc import abstractmethod
class BaseServiceClient:

    def __init__(self , subject , content  , tokens ,   to_recivers , template):
       
        self.subject = subject
        self.content = content
        self.to_receivers = to_recivers
        self.tokens = tokens
        self.template = template

    @abstractmethod
    def create(self):
        raise Exception('Must implement')

    
    @abstractmethod
    def send(self):
        raise Exception('Must implement')


    def dynamic_data_substitution(self):
        substituted_contents = [] 
        print(' Dynamic Data Substituted')
        
        for item in range(len(self.to_receivers)) : 
            content_to_be_subsitute = self.content
            reciver = self.to_receivers[item]
            try : 
                token = self.tokens[item]

                print('---------------')
                print(reciver)
                print("{")
                print(token)

                for data in token : 
                    value ='{?'+data+"?}"
                    if value in content_to_be_subsitute : 
                        substiuted_content = content_to_be_subsitute.replace(value,token[data])
                substituted_contents.append(substiuted_content)

                print(substiuted_content)
                print("}")
                print('---------------')
            except : 
                substituted_contents.append(content_to_be_subsitute) 
                break 
        self.content=substituted_contents
     
    


