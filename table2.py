
<style>
@import url('https://fonts.googleapis.com/css?family=Roboto+Mono');
html{
   display:flex;
   justify-content:center;
   align-items: center;
   width: 100%;
   height: 100%;
   background-image: url('https://source.unsplash.com/collection/327760/1600x900');
   background-size:cover;
}

body{
   width:55%;
   height:60vh;
   border:1px solid lightgray;
   background-color:white;
   border-radius:8px;
   font-family: 'Roboto Mono', monospace;
   box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
   border-top:32px solid #eee;
   overflow-y:scroll;
}

body > div{
  height: calc(100% - 40px);
  overflow-y:auto;
  padding: 20px;
  font-size: 24px;
  white-space: pre;
}

pre{
  margin:inherit;
  font-family: inherit;
}
</style>

#!/usr/bin/python3
print("Content-type: text/html \n")
import magicwand

def arithmetic_table(num):
    count = 0
    while count < 10:
        print(F" {num} x {count} = {num*count}")
        count = count + 1
        
def arithmetic_table_for(num):
    for c in range(10):
        print(F" {num} x {c} = {num*c}")
        
arithmetic_table(13)

print("")

arithmetic_table(32)

print("")

arithmetic_table(23)

print("")

def get_sum(num):
    total = 0
    for c in range(num):
        total = total + c 
    print("Total is: ", total)
    
get_sum(100)
