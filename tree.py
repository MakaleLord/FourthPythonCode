
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

print(f"""
{" "*10}{"*"*2}
{" "*9}{"*"*4}
{" "*8}{"*"*6}
{" "*7}{"*"*8}
{" "*6}{"*"*10}
{" "*5}{"*"*12}
{" "*4}{"*"*14}
{" "*3}{"*"*16}
{" "*2}{"*"*18}
{" "*1}{"*"*20}
{" "*10}||
""")

length = 10

for current_line in range(length): 
    space = length - current_line
    print(" "*space,"*"*current_line*2)
    if current_line == 8:
        break
print(" "*length, "||")
