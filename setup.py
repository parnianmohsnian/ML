from setuptools import find_packages, setup

hyphen = '-e .'
def get_requirmetns(file_path:str)->list[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments=[req.replace("\n", "") for req in requirments]
        
        if hyphenin requirments:
            requirments.remove(hyphen)
            
    return requirments
    
        

setup(
    name='mlproject',
    version='0.1.1',
    author='parnian',
    author_email='parnianmoh3nian@gmail.com',
    packages=find_packages(),
    intall_requires=get_requirmetns('requirments.txt')
    
)